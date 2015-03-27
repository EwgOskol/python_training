__author__ = 'tester'

from sys import maxsize

class Contact:

    def __init__(self, fname=None, lname=None, company=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, hm_page=None, id=None):
        self.fname = fname
        self.lname = lname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.hm_page = hm_page
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.fname, self.lname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fname == other.fname and self.lname == other.lname

    def id_or_max(self):
        if (self.id):
            return int(self.id)
        else:
            return maxsize
