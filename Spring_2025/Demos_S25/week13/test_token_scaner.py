from tokenscanner import TokenScanner
from PigLatin import word_to_pig_latin

def to_pig_latin(text):
    translation = ""
    scanner = TokenScanner()
    scanner.set_input(text)
    while scanner.has_more_tokens():
        token = scanner.next_token()
        if token.isalpha():
            #token = word_to_pig_latin(token)
            pass
        translation += token
    return translation

print(to_pig_latin("word of wisdom is enough"))
