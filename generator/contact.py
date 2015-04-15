
from model.contact import Contact
import random
import string
import jsonpickle
#import json
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen, addition=""):
    symbols = addition + string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    symbols = string.digits + "+"
    prefix = random.choice(symbols)
    return prefix + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen-1))])

def random_email(maxlen1, maxlen2):
    symbols = string.ascii_letters + string.digits + ".-_"
    prefix = "".join([random.choice(symbols) for i in range(random.randrange(maxlen1))])
    suffix = "".join([random.choice(symbols) for i in range(random.randrange(maxlen2))])
    return prefix + "@" + suffix

testdata = [Contact(fname="", lname="", address="", company="", email="",
                    mobilephone="", workphone="", homephone="", hm_page="")] + [
    Contact(fname="Ivan", lname="Ivanov", company="My company", address="Voronezh Kirova street 91 154",
            homephone="31-33-37", mobilephone="8-900-800-7000", workphone="17-18-19", hm_page="my_homepage.ru")] + [
    Contact(fname=random_string("F", 15), lname=random_string("L", 20), company=random_string("OAO ", 20, "-. "),
            email=random_email(10, 7), address=random_string("OAO ", 30, "\n,   "),
            hm_page=random_string("www.", 40, "/.-_ "),
            mobilephone=random_phone(11), workphone=random_phone(7), homephone=random_phone(7))
    for name in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
