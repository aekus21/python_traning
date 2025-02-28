class Group:
    def __init__(self, name = None, header = None, footer = None, id = None):
        self.test_name = name
        self.test_header = header
        self.test_footer = footer
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.id, self.test_name)

    def __eq__(self, other):
        return self.id == other.id and self.test_name == other.test_name