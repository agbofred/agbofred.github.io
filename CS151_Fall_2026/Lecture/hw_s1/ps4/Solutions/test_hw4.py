# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest
from pgl import GCompound

from Prob1 import create_cube
from Prob2 import to_obenglobish
from Prob3 import encrypt

class Test_Prob1:
    def test_create_cube_output(self):
        student = create_cube()
        assert isinstance(student, GCompound), f"Your create_cube function should be returning a GCompound, but is instead returning a {type(student)}."

class Test_Prob2:
    def test_returns_string(self):
        student = to_obenglobish("english")
        assert type(student) == str, f"You should be returning a string, but are currently returning a {type(student)}."

    def test_easy_vowels(self):
        words = ["english", "fish", "panda"]
        sols = ["obenglobish", "fobish", "pobandoba"]
        for w,s in zip(words, sols):
            student = to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_repeat_vowels(self):
        words = ["gooiest", "fruit", "books"]
        sols = ["gobooiest", "frobuit", "bobooks"]
        for w,s in zip(words, sols):
            student = to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_ending_ees(self):
        words = ["amaze", "apple", "eerie"]
        sols = ["obamobaze", "obapple", "obeerobie"]
        for w,s in zip(words, sols):
            student = to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

class Test_Prob3:
    KEY = "pyfgcrlaoeuidhtnsqjkxbmwvz"
    def test_returns_string(self):
        student = encrypt("english", self.KEY)
        assert type(student) == str, f"You should be returning a string, but are currently returning a {type(student)}."

    def test_basic_substitutions(self):
        msgs = ["hello", "fishsticks", "papaya"]
        sols = ["aciit", "rojajkofuj", "npnpvp"]
        for w,s in zip(msgs, sols):
            student = encrypt(w, self.KEY)
            assert student == s, f"{w} encrypted to {student} with key={self.KEY} but should have been {s}."

    def test_non_alphabetic_characters(self):
        msgs = ["hello!", "fishsticks and food", "i'm here now!"]
        sols = ["aciit!", "rojajkofuj phg rttg", "o'd acqc htm!"]
        for w,s in zip(msgs, sols):
            student = encrypt(w, self.KEY)
            assert student == s, f"{w} encrypted to {student} with key={self.KEY} but should have been {s}."

    def test_capitalization(self):
        msgs = ["Hello", "Fishsticks", "BoomBoom"]
        sols = ["Aciit", "Rojajkofuj", "YttdYttd"]
        for w,s in zip(msgs, sols):
            student = encrypt(w, self.KEY)
            assert student == s, f"{w} encrypted to {student} with key={self.KEY} but should have been {s}."

    def test_all_combined(self):
        msgs = ["Hello??", "Fishsticks and FooD", "Give me that NOW!"]
        sols = ["Aciit??", "Rojajkofuj phg RttG", "Lobc dc kapk HTM!"]
        for w,s in zip(msgs, sols):
            student = encrypt(w, self.KEY)
            assert student == s, f"{w} encrypted to {student} with key={self.KEY} but should have been {s}."
