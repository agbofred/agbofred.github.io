
import pytest
import mock
import pgl

from Prob1a import calc_months_to_savings
from Prob1b import count_chain, find_longest_chain
from Prob1c import estimate_pi
from Prob2 import consecutive_heads


class PGL_Test:
    def __init__(self):
        self._gw = None
        self._base = None
        self._contents = None

_pgltest = PGL_Test()

class Test_Prob1a:
    def test_given_expressions(self):
        inputs = [(1000,0.01), (1000, 0.10)]
        outputs = [325, 48]
        for i,o in zip(inputs, outputs):
            student = calc_months_to_savings(*i)
            assert student == o

    def test_other_inputs(self):
        inputs = [(1,1), (1000, 0.1, 10000)]
        outputs = [1043, 90]
        for i,o in zip(inputs, outputs):
            student = calc_months_to_savings(*i)
            assert student == o

class Test_Prob1b:
    def test_given_expressions(self):
        inputs = [100, 1000]
        outputs = [118, 178]
        for i,o in zip(inputs, outputs):
            student = find_longest_chain(i)
            assert student == o

    def test_other_inputs(self):
        inputs = [2, 10000, 500]
        outputs = [1, 261 ,143]
        for i,o in zip(inputs, outputs):
            student = find_longest_chain(i)
            assert student == o

class MyRandom:
    # seq = [True, False, True, True, False, True, True, True, False, True, True, True, True, False, True]
    seq = []

    def __init__(self):
        for i in range(1,5):
            MyRandom.seq.extend([True]*i)
            MyRandom.seq.extend([False]*i)
        self.gen = self.coin_flip()

    def coin_flip(self):
        i = 0
        while True:
            yield self.seq[i % len(self.seq)]
            i += 1

    def randint(self, a,b):
        return int(next(self.gen))

    def random(self):
        return int(next(self.gen))



class Test_Prob2:

    def test_returns_an_int(self):
        student = consecutive_heads(4)
        assert isinstance(student, int)

    def test_num_flips(self):
        inputs = [1,2,3,4]
        outputs_head_true = [1,4,9,16]
        outputs_head_false = [2,6,12,20]
        for i,o1,o2 in zip(inputs, outputs_head_true, outputs_head_false):
            R = MyRandom()
            with mock.patch('random.randint', R.randint), mock.patch('random.random', R.random):
                student = consecutive_heads(i)
                assert student == o1 or student == o2

    def test_print_final_line(self, capsys):
        inputs = [1,2,3,4]
        outputs_head_true = [1,4,9,16]
        outputs_head_false = [2,6,12,20]
        for i,o1,o2 in zip(inputs, outputs_head_true, outputs_head_false):
            R = MyRandom()
            with mock.patch('random.randint', R.randint), mock.patch('random.random', R.random):
                consecutive_heads(i)
                captured = capsys.readouterr().out.splitlines()
                assert str(o1) in captured[-1] or str(o2) in captured[-1]


class MyWindow(pgl.GWindow):
    def __init__(self,*args):
        super().__init__(*args)
        _pgltest._gw = self
        _pgltest._base = self._base
        _pgltest._contents = self._base._contents


class Test_Prob1c:
    def test_glabel_position(self):
        with mock.patch('Prob1c.GWindow', MyWindow):
            estimate_pi(100)
            labels = [i for i in _pgltest._contents if isinstance(i, pgl.GLabel)]
            assert len(labels) == 1, "There are more than one label in the scene."
            label = labels[0]
            assert label.get_x() == _pgltest._gw.get_width() / 2 - label.get_width() / 2, "The label is not centered correctly horizontally."
            assert label.get_y() == _pgltest._gw.get_height() / 2 + label.get_ascent() / 2, "The label is not centered correctly vertically."

    def test_glabel_contents(self):
        with mock.patch('Prob1c.GWindow', MyWindow):
            tries = 100
            estimate_pi(tries)
            label = [i for i in _pgltest._contents if isinstance(i, pgl.GLabel)][0]
            hits = [i for i in _pgltest._contents if i.get_color() == "#FF0000"]
            pi = len(hits) / tries * 4
            assert label.get_label() == str(round(pi,2)), "The label is not showing the correct value of pi."

    def test_red_targets_inside(self):
        with mock.patch('Prob1c.GWindow', MyWindow):
            tries = 1000
            estimate_pi(tries)
            hits = [i for i in _pgltest._contents if i.get_color() == "#FF0000"]
            for hit in hits:
                xcent = hit.get_x() + hit.get_width()/2
                ycent = hit.get_y() + hit.get_height()/2
                size = _pgltest._gw.get_width() / 2
                assert (xcent-size)**2 + (ycent-size)**2 <= size ** 2, "Some red shots are not within the target."
