from english import ENGLISH_WORDS, is_english_word
def find_first_vowel(word):
    for i in range(len(word)):
        if word[i].lower() in "aeiou":
            return i
    return -1


def pig_latin(word):
    """
    This function is expected to change a word to piglatin 

    Algorithms:
       1. check the word if it contains a vowel 
            1.1 In that case, I will then check if that the vowel is at the begining or somewhere else
            1.2 If at the beginning, then add 'way' to the end of that same word
            1.3 Otherwise, then cut until the vowel and take that to the end of the word and add 'ay'
        2. Otherwise, do nothing 
    """
    first_vowel = find_first_vowel(word)
    if first_vowel > 0:
        first_part = word[:first_vowel]
        second_part = word[first_vowel:]
        word = second_part + first_part + "ay"
    
    elif first_vowel == 0:
        word = word + "way"
    return word

# if __name__ == "__main__":
#     for word in ENGLISH_WORDS:
#         if is_english_word(pig_latin(word)) and word != pig_latin(word):
#             print(word, pig_latin(word))


def members_birthday():
    """
    Here is the birthday program
    Enter your name: Joe
    Enter your birth month: April
    Enter your birth year: 1985
    """
    col1Label = "Name"
    col2Label = "Birth Month"
    col3Label = "Age"
    table = f"{col1Label:<10s} {col2Label:<15s} {col3Label:<5s}"
    birthdays = ""
    for i in range(2):
        name = input("Enter your name: ")
        month = input("Enter your birth month: ")
        year = int(input("Enter your birth year "))
        birthdays += f"{name:<10s} {month:<15s} {2026 - year:<5d}" + "\n"
    print("-"*30)
    print(table)
    print("-"*30)
    print(birthdays)

members_birthday()