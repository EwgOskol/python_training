
from model.contact import Contact
import random
import string

testdata = [Contact(fname="First_name1", lname="Last_name1", address="Addres1",
                    company="Company1", email="email1@m.ru",
                    mobilephone="11111111", workphone="22222222", homephone="33333333",
                    hm_page="www.homepage1.ru"),
            Contact(fname="First_name2", lname="Last_name2", address="Addres2",
                    company="Company2", email="email2@m.ru",
                    mobilephone="44444444", workphone="55555555", homephone="66666666",
                    hm_page="www.homepage2.ru")
]


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


testdata2 = [Contact(fname="", lname="", address="", company="", email="",
                    mobilephone="", workphone="", homephone="", hm_page="")] + [
    Contact(fname="Ivan", lname="Ivanov", company="My company", address="Voronezh Kirova street 91 154",
            homephone="31-33-37", mobilephone="8-900-800-7000", workphone="17-18-19", hm_page="my_homepage.ru")] + [
    Contact(fname=random_string("F", 15), lname=random_string("L", 20), company=random_string("OAO ", 20, "-. "),
            email=random_email(10, 7), address=random_string("OAO ", 30, "\n,   "),
            hm_page=random_string("www.", 40, "/.-_ "),
            mobilephone=random_phone(11), workphone=random_phone(7), homephone=random_phone(7))
    for name in range(5)
]
