__author__ = 'tester'

from sys import maxsize
import re

class Contact:

    def __init__(self, fname=None, lname=None, company=None, address=None, hm_page=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 all_phones_from_home_page=None, email=None, email2=None, email3=None, emails=None):
        self.fname = fname
        self.lname = lname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.hm_page = hm_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.emails = emails


    def __repr__(self):
        return "%s:%s" % (self.fname, self.lname)

    def __eq__(self, other):
        return re.sub(r'\s+', ' ', self.fname.rstrip()) == re.sub(r'\s+', ' ', other.fname.rstrip()) \
               and re.sub(r'\s+', ' ', self.lname.rstrip()) == re.sub(r'\s+', ' ', other.lname.rstrip()) \
               and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if (self.id):
            return str(self.id)
        else:
            return str(maxsize)
