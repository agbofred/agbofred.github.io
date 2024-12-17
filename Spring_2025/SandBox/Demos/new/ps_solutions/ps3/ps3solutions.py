style = ["solid", "hollow", "alternate"]
def draw_complex_pyramid(height, symbol, style):
    for row in range(height):
        star = 2*row + 1
        space = height - row - 1
        line = " " * space + symbol * star
        hollow = 2*row - 1
        if style =='solid':
            print(line)
        elif style =='hollow':
            if((hollow<0 ) or (hollow > height)):
                print(line)
            else:
                linehole = " " * space + "*" + " " * hollow + "*"
            #vacume = space-2
            #line = " " * space + symbol * star
            #print(line)
                print(linehole)

if __name__ == '__main__':
    draw_complex_pyramid(8,"*", style[0])