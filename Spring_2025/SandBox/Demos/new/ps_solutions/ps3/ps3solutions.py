# Problem 1 solution

style = ["solid", "hollow", "alternate"]
def draw_complex_pyramid(height, symbol, style):
    for row in range(height):
        star = 2*row -1
        space = height - row - 1
        line = " " * space + symbol * star
        if style =='solid':
            print(line)
        elif style =='hollow':
            #vacume = space-2
            #line = " " * space + symbol * star
            #print(line)
            print("Not matching")

if __name__ == '__main__':
    draw_complex_pyramid(8,"*", style[0])



    