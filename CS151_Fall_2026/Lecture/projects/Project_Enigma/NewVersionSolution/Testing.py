
"""
Program to allow quick tests on functionality
of EnigmaModel.
"""

import EnigmaModel
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
from rich.traceback import install
install(show_locals=True)

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def test_key_pressed():
    title = "Testing Key Press"
    msg = ""
    errors = False
    em = EnigmaModel.EnigmaModel()
    for key in ALPHABET:
        em.key_pressed(key)
        for letter in ALPHABET:
            letter_is_pressed = em.is_key_down(letter)
            if letter == key and not letter_is_pressed:
                msg += f"{letter} should have been pressed and isn't\n"
                errors = True
            elif letter_is_pressed and letter != key:
                msg += f"{letter} should not have been pressed and is?\n"
                errors = True
        em.key_released(key)
    if not errors:
        msg = "No errors found"
        print(Panel(Markdown(msg, style='white'), title=title, style='green'))
    else:
        print(Panel(Markdown(msg.strip(), style='white'), title=title, style='red'))


def test_key_released():
    title = 'Testing Key Released'
    msg = ""
    errors = False
    em = EnigmaModel.EnigmaModel()
    for key in ALPHABET:
        em.key_pressed(key)
        em.key_released(key)
        for letter in ALPHABET:
            letter_is_down = em.is_key_down(letter)
            if letter == key and letter_is_down:
                msg += f"- {letter} should have been released and isn't\n"
                errors = True
    if not errors:
        msg = "No errors found"
        print(Panel(Markdown(msg, style='white'), title=title, style='green'))
    else:
        print(Panel(Markdown(msg.strip(), style='white'), title=title, style='red'))

def test_rotors():
    # print('Testing Rotor Methods'.center(60,'-'))
    title = 'Testing Rotor Methods'
    msg = ""
    errors = False
    em = EnigmaModel.EnigmaModel()
    for i,clicks in enumerate([5,0,10]):
        for _ in range(clicks):
            em.rotor_clicked(i)
    if em.get_rotor_letter(0) != 'F':
        msg += '- The slow rotor was clicked 5 times but is not showing F\n'
        # print('The slow rotor was clicked 5 times but is not showing F')
        errors = True
    if em.get_rotor_letter(1) != 'A':
        msg += '- The medium rotor was not advanced but is not showing A\n'
        # print('The medium rotor was not advanced but is not showing A')
        errors = True
    if em.get_rotor_letter(2) != 'K':
        msg += '- The fast rotor was advanced 10 times but is not showing K\n'
        # print('The fast rotor was advanced 10 times but is not showing K')
        errors = True
    if not errors:
        msg = "No errors found"
        print(Panel(Markdown(msg, style='white'), title=title, style='green'))
    else:
        print(Panel(Markdown(msg.strip(), style='white'), title=title, style='red'))

def test_lamps():
    title = 'Testing Simple Lamp with Auto-Advance'
    msg = ''
    errors = False
    em = EnigmaModel.EnigmaModel()
    em.key_pressed('W')
    for letter in ALPHABET:
        lamp_on = em.is_lamp_on(letter)
        if lamp_on and letter != 'K':
            msg += f'- The {letter} lamp is on instead of K\n'
            errors = True
    if not errors:
        msg = "No errors found"
        print(Panel(Markdown(msg, style='white'), title=title, style='green'))
    else:
        print(Panel(Markdown(msg.strip(), style='white'), title=title, style='red'))

def test_rollover():
    title = 'Testing Rotor Rollover'
    msg = ""
    errors = False
    em = EnigmaModel.EnigmaModel()
    for _ in range(30):
        em.rotor_clicked(2)
    rotors = [em.get_rotor_letter(i) for i in range(3)]
    if rotors != ['A', 'A', 'E']:
        msg += f'- After clicking the fast rotor 30 times, the rotor letters should have read [A, A, E] but instead read {rotors}\n'
        errors = True

    em = EnigmaModel.EnigmaModel()
    for _ in range(25):
        em.rotor_clicked(1)
    for _ in range(30):
        em.key_pressed('A')
        em.key_released('A')
    rotors = [em.get_rotor_letter(i) for i in range(3)]
    if rotors != ['B', 'A', 'E']:
        msg += f'- After clicking the medium rotor 25 times, and then pressing the A key 30 times, the rotor letters should have read [B, A, E] but instead read {rotors}\n'
        errors = True

    if not errors:
        msg = "No errors found"
        print(Panel(Markdown(msg, style='white'), title=title, style='green'))
    else:
        print(Panel(Markdown(msg.strip(), style='white'), title=title, style='red'))


def test_full_encryption_string():

    def gather_encryption_string(input:str , sol:str, rotors:str):
        nonlocal msg
        em = EnigmaModel.EnigmaModel()

        for i,l in enumerate(rotors):
            n = ALPHABET.index(l)
            for _ in range(n):
                em.rotor_clicked(i)

        S = input
        encryption_string = ""
        for letter in S:
            if letter not in ALPHABET:
                encryption_string += letter
                continue
            em.key_pressed(letter)
            lamps = [em.is_lamp_on(l) for l in ALPHABET]
            if lamps.count(True) > 1:
                msg += '- Multiple lamps are on at the same time when they should not be?\n'
                # print('Multiple lamps are on at the same time when they should not be?')
                return True
            else:
                encryption_string += ALPHABET[lamps.index(True)]
            em.key_released(letter)
        if encryption_string != sol:
            msg += f"- {S} should have encrypted to {sol} with rotors starting at {rotors}, but was instead {encryption_string}\n"
            # print(f"{S} should have encrypted to\n{sol}\nwith rotors starting at {rotors}, but was instead\n{encryption_string}")
            return True
        return False


    # print('Testing Full Encryptions'.center(60, '-'))
    title = 'Testing Full Encryptions'
    msg = ""
    S = "Frosty the Snowman was a jolly happy soul with a corn cob pipe and a button nose and two eyes made out of coal".upper()
    sol = "QACFWF QKK GICDSSI SCZ R NQUYL BBQNN AXBE XBNC Y DVYV KJV OSWL MLW N FNFMVH KIMG NZZ DJH MVQV SPHF BMI PD BURT"
    errors = gather_encryption_string("F", "J", "AAA")
    errors = gather_encryption_string("FROSTY", "JBVULC", "AAA") or errors
    errors = gather_encryption_string("FROSTY", "QACFWF", "JED") or errors
    errors = gather_encryption_string(S, sol, "JED") or errors

    if not errors:
        msg = "No errors found"
        print(Panel(Markdown(msg, style='white'), title=title, style='green'))
    else:
        print(Panel(Markdown(msg.strip(), style='white'), title=title, style='red'))




if __name__ == '__main__':
    test_key_pressed()
    test_key_released()
    test_rotors()
    test_lamps()
    test_rollover()
    test_full_encryption_string()

