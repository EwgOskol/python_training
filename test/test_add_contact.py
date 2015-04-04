# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

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
    for name in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print(new_contacts)


