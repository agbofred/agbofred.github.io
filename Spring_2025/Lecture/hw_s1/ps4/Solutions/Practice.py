import math


def is_prime():
    num = int(input('Enter a number: '))
    for n in range(2,num):
        if num % n == 0:
            return False
    return True

def odd_sum(maxnum):
    def add_odd(x,total):
        if x % 2 == 1:
            total += x

    total = 0
    for n in range(maxnum+1):
        add_odd(n,total)
    return total

def test():
    x = 1
    def f():
        x = x + 1
        print(x)
    f()

def num_sym_in_string(symbol, string='Default String'):
    count = 0
    for c in string:
        if c == symbol:
            count += 1
    return count

def eqn_solver(guess, A=2):
    def f(x):
        return (x-1)**A - A*math.cos(x/A)

    def df(x):
        return A*(x-1)**(A-1) + math.sin(x/A)

    epsilon = 0.001
    iteration = 0
    while abs(f(guess)) > epsilon and iteration < 1000:
        guess -= f(guess) / df(guess)
        iteration += 1
    if iteration < 1000:
        return round(guess,4)
    else:
        return None



def cube_pyramid():
    from pgl import GWindow, GPolygon, GCompound

    def draw_cube():
        cube = GCompound()
        # Origin to be at center

        lhs = GPolygon()
        lhs.add_vertex(0,0)
        lhs.add_polar_edge(L, 150)
        lhs.add_polar_edge(L, -90)
        lhs.add_polar_edge(L, -30)
        lhs.set_filled(True)
        lhs.set_fill_color("#222222")
        lhs.set_line_width(2)
        cube.add(lhs)

        rhs = GPolygon()
        rhs.add_vertex(0,0)
        rhs.add_polar_edge(L, 30)
        rhs.add_polar_edge(L, -90)
        rhs.add_polar_edge(L, -150)
        rhs.set_filled(True)
        rhs.set_fill_color("#888888")
        rhs.set_line_width(2)
        cube.add(rhs)

        top = GPolygon()
        top.add_vertex(0,0)
        top.add_polar_edge(L, 30)
        top.add_polar_edge(L, 150)
        top.add_polar_edge(L, -150)
        top.set_filled(True)
        top.set_fill_color("#EEEEEE")
        top.set_line_width(2)
        cube.add(top)

        return cube

    def rotate():
        pyramid.rotate(1)


    gw = GWindow(500,500)
    L = 40
    pyramid = GCompound()
    for row in range(6):
        for col in range(row+1):
            pyramid.add(draw_cube(), -(L/2)*3**0.5*row + 2*(L/2)*3**(0.5)*col, -5*L+(L + L/2)*row)
    gw.add(pyramid, 250, 250)
    gw.set_interval(rotate, 20)


def to_obenglobish(word):
    def is_previous_letter_vowel(index):
        if index == 0:
            return False
        else:
            return word[index-1] in "aeiou"

    def is_final_e(index):
        return (word[index] == "e" and index == len(word)-1)

    translation = ""
    for i in range(len(word)):
        if word[i] in "aeiou":
            if not (is_previous_letter_vowel(i) or is_final_e(i)):
                translation += "ob" + word[i]
            else:
                translation += word[i]
        else:
            translation += word[i]
    return translation

def encrypt(message, key):
    ciphered = ""
    for char in message:
        if char.isalpha():
            alpha_index = "abcdefghijklmnopqrstuvwxyz".find(char.lower())
            if char.isupper():
                ciphered += key[alpha_index].upper()
            else:
                ciphered += key[alpha_index].lower()
        else:
            ciphered += char
    return ciphered

def longest_obenglobish():
    from english import ENGLISH_WORDS

    longest = ""
    for word in ENGLISH_WORDS:
        wobord = to_obenglobish(word)
        if len(wobord) - len(word) > len(to_obenglobish(longest)) - len(longest):
            longest = word
            print(wobord)
    print(f"The longest obenglobish word is {to_obenglobish(longest)}, derived from {longest}")


def longest_word():
    from english import ENGLISH_WORDS

    longest = ""
    for word in ENGLISH_WORDS:
        if len(word) > len(longest):
            longest = word
    print(f"The longest word is {longest}!")

if __name__ == '__main__':
    pass
    # print(is_prime(47))
    # print(odd_sum(10))
    # cube_pyramid()
    # print(to_obenglobish("rot"))
    # longest_obenglobish()
    key = "pyfgcrlaoeuidhtnsqjkxbmwvz"
    print(encrypt("Hello??", key))
    # longest_word()

