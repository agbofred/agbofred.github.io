class ERModel(object):
    """Model of a scheduler."""

    def __init__(self):
        self.patients = LinkedPriorityQueue()

    def isEmpty(self):
        """Returns True if there are patients in the model
        or False otherwise."""
        return self.patients.isEmpty()

    def schedule(self, p):
        """Adds a patient to the schedule."""
        self.patients.add(p)

    def treatNext(self):
        """Returns the patient treated or None if there are none."""
        if self.patients.isEmpty():
            return None
        else:
            return self.patients.pop()