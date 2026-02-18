class Bag:
    def __init__(self, iterable=None):
        """Initialize the Bag. Optionally add items from iterable."""
        self._counts = {}
        if iterable is not None:
            for item in iterable:
                self.add(item)

    def add(self, item):
        """Add one occurrence of item to the Bag."""
        if item in self._counts:
            self._counts[item] += 1
        else:
            self._counts[item] = 1

    def remove(self, item):
        """Remove one occurrence of item from the Bag. Raise ValueError if not found."""
        if item in self._counts:
            if self._counts[item] > 1:
                self._counts[item] -= 1
            else:
                del self._counts[item]
        else:
            raise ValueError(f"{item} not found in Bag")

    def count(self, item):
        """Return the number of times item appears in the Bag."""
        return self._counts.get(item, 0)

    def length(self):
        """Return the total number of items in the Bag (including duplicates)."""
        return sum(self._counts.values())

    def __iter__(self):
        """Yield each item in the Bag, including duplicates."""
        for item, cnt in self._counts.items():
            for _ in range(cnt):
                yield item  

    def contains(self, item):
        """Return True if item is in the Bag, False otherwise."""
        return item in self._counts        

    def __repr__(self):
        """Return a string representation of the Bag."""
        items = []
        for item in self:
            items.append(str(item))
        return f"Bag([{', '.join(items)}])"
    