__author__ = 'tester'

class Cont_in_Groups:

    def __init__(self, id=None, group_id=None):
        self.id = id
        self.group_id = group_id

    def __repr__(self):
        return "%s:%s" % (self.id, self.group_id)

    def __eq__(self, other):
        return self.id == other.id and self.group_id == other.group_id

    def get_id(self):
        if (self.id):
            return int(self.id)

    def get_group_id(self):
        if (self.group_id):
            return int(self.group_id)
