import unittest
from bag import Bag

class TestBag(unittest.TestCase):
    def test_add_and_count(self):
        b = Bag()
        b.add(1)
        b.add(1)
        b.add(2)
        self.assertEqual(b.count(1), 2)
        self.assertEqual(b.count(2), 1)
        self.assertEqual(b.count(3), 0)

    def test_remove(self):
        b = Bag([1, 2, 2])
        b.remove(2)
        self.assertEqual(b.count(2), 1)
        b.remove(2)
        self.assertEqual(b.count(2), 0)
        with self.assertRaises(ValueError):
            b.remove(2)

    def test_len(self):
        b = Bag([1, 2, 2, 3])
        self.assertEqual(len(b), 4)
        b.remove(2)
        self.assertEqual(len(b), 3)

    def test_iter(self):
        b = Bag([1, 2, 2])
        items = list(b)
        self.assertEqual(sorted(items), [1, 2, 2])

    def test_contains(self):
        b = Bag([1, 2])
        self.assertTrue(1 in b)
        self.assertFalse(3 in b)

    def test_repr(self):
        b = Bag([1, 2, 2])
        self.assertTrue("Bag" in repr(b))

    def test_empty_init(self):
        b = Bag()
        self.assertEqual(len(b), 0)

    def test_mixed_types(self):
        b = Bag(["a", 1, "a"])
        self.assertEqual(b.count("a"), 2)
        self.assertEqual(b.count(1), 1)

if __name__ == "__main__":
    unittest.main()
