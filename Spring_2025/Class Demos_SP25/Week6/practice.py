from english import is_english_word, ENGLISH_WORDS
def tracer(n):
    total = 0
    while n > 0:# start tracing here
        digit = n % 10
        total += digit
        n //= 10
    return total


if __name__ == "__main__":
    print(tracer(1984))