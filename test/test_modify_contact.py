__author__ = 'tester'

from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="tester", lname="tester", company="Test Inc"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact("Ivan_new", "Ivanov1_new", "My company1", "Voronezh Kirova street 91 151", "31-33-31",
        "8-900-800-7001", "17-18-11", "my_homepage1.ru")
    contact.id = old_contacts[index].id
    app.contact.modify_some_contact(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




