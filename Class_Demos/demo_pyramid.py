# Here is a version of the pyramid without using formating function

def draw_console_pyramid(size):
    star = '*'
    addstar = '**'
    for i in range(size,0,-1):
        indent = " "*i
        print(f'{indent} {star}')
        star = star + addstar


# Here is a version of the pyramid using formating function

def second_drw_console_pyramid(size):
    star = '*'
    addstar = '**'
    for i in range(size,0,-1):
        #indent = " "*i
        #output = star.rjust(i)
        print(f'{star.center(i)}')
        star = star + addstar
if __name__ == "__main__":
    #draw_console_pyramid(8)
    second_drw_console_pyramid(8)
