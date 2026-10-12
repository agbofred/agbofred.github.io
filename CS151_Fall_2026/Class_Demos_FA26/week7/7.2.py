from pgl import GWindow, GOval, GLine, GRect
def mystery():
    def enigma():
        rect.move(1, 1)

    def puzzle():
        rect.set_filled(True)

    gw = GWindow(200, 200)
    rect = GRect(0, 0, 25, 25)
    gw.add(rect)
    gw.set_interval(enigma, 20)
    gw.set_timeout(puzzle, 1000)

if __name__ == '__main__':
    mystery()