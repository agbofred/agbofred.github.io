'''
For the histogram problem.
'''

def create_histogram_array(nbins, data):
    """ Returns counts of how much data is present in each bin where data counts do
    not exceed the number of bins. """
    bins = [0] * nbins
    for value in data:
        bins[value] += 1
    return bins

def print_histogram(array):
    for i in range(len(array)):
        print(f"{i}: {array[i]*'*'}")

def create_histogram_graph(array, width, height):
    from pgl import GRect, GCompound

    c = GCompound()
    barhscale = height / max(array)
    barwidth = width / len(array)
    for i in range(len(array)):
        bar = GRect(i*barwidth, height - array[i]*barhscale, barwidth, array[i]*barhscale)
        bar.set_filled(True)
        bar.set_fill_color('red')
        c.add(bar)
    return c




if __name__ == '__main__':
    pi_hist = create_histogram_array(10, [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9])
    print_histogram(pi_hist)

    from pgl import GWindow
    gw = GWindow(800, 600)
    graph = create_histogram_graph(pi_hist, 800/2, 600/2)
    gw.add(create_histogram_graph(pi_hist, 800/2, 600/2))
    gw.add(create_histogram_graph(pi_hist, 800/2, 600/2), 800/2, 0)
    gw.add(create_histogram_graph(pi_hist, 800/2, 600/2), 0, 600/2)
    gw.add(create_histogram_graph(pi_hist, 800/2, 600/2), 800/2, 600/2)

