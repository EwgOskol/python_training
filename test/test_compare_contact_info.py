__author__ = 'tester'

import re
# from random import randrange
from model.contact import Contact


def test_contact_info_on_home_page(app, db):
    contact_from_db = list(sorted(db.get_contact_list(), key=Contact.id_or_max))
    contact_from_home_page = list(sorted(app.contact.get_contact_list(), key=Contact.id_or_max))
    assert len(contact_from_db) == len(contact_from_home_page)
    for index in range(len(contact_from_db)):
        contact_from_db[index].all_phones_from_home_page = merge_phones_like_on_home_page(contact_from_db[index])
        contact_from_db[index].emails = merge_emails_like_on_home_page(contact_from_db[index])
        assert contact_from_home_page[index].all_phones_from_home_page == contact_from_db[index].all_phones_from_home_page \
                and re.sub(r'\s+', ' ', contact_from_home_page[index].address.rstrip("\n ")) == re.sub(r'\s+', ' ', contact_from_db[index].address.rstrip("\n ")) \
                and contact_from_home_page[index].emails == contact_from_db[index].emails \
                and re.sub(r'\s+', ' ', contact_from_home_page[index].fname.rstrip("\n ")) == re.sub(r'\s+', ' ', contact_from_db[index].fname.rstrip("\n ")) \
                and re.sub(r'\s+', ' ', contact_from_home_page[index].lname.rstrip("\n ")) == re.sub(r'\s+', ' ', contact_from_db[index].lname.rstrip("\n "))


#def test_contact_info_on_home_page(app):
#    count_contacts = app.contact.get_contact_list()
#    index = randrange(len(count_contacts))
#    contact_from_home_page = app.contact.get_contact_list()[index]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    contact_from_edit_page.all_phones_from_home_page = merge_phones_like_on_home_page(contact_from_edit_page)
#    contact_from_edit_page.emails = merge_emails_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_phones_from_home_page == contact_from_edit_page.all_phones_from_home_page \
#           and re.sub(r'\s+', ' ', contact_from_home_page.address.rstrip("\n ")) == re.sub(r'\s+', ' ', contact_from_edit_page.address.rstrip("\n ")) \
#           and contact_from_home_page.emails == contact_from_edit_page.emails \
#           and contact_from_home_page.fname == contact_from_edit_page.fname \
#           and contact_from_home_page.lname == contact_from_edit_page.lname


def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None,
                            filter(lambda x: x != "", [contact.email, contact.email2, contact.email3])))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
