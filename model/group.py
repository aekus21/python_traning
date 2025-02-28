from sys import maxsize

class Group:
    def __init__(self, name = None, header = None, footer = None, ids = None):
        self.test_name = name
        self.test_header = header
        self.test_footer = footer
        self.id = ids

    def __repr__(self):
        return '%s:%s' % (self.id, self.test_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.test_name == other.test_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize