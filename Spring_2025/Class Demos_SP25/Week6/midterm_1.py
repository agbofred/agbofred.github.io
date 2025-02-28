from english import ENGLISH_WORDS, is_english_word
import random

def one_off(real_word):

 #first i make an empty list to put words that are the correct length into

    word_list = []

    final_words = []

    for words in ENGLISH_WORDS:

        if len(words) == len(real_word):

            word_list.append(words)

 #now i take my real word and make it missing one letter and checking if this

 #matches another word missing a letter in the same index

            for x in range(len(real_word)):

                fake_word = real_word[:x] + real_word[x+1:]

                for word in word_list:

                    for z in range(len(word)):

                        other_word = word[:z] + word[z+1:]

                        if fake_word == other_word:

                            word_list += word

                            print(word_list)
print(one_off("grace"))