__author__ = 'tester'

from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="tester", lname="tester", company="Test Inc"))
    old_contacts = db.get_contact_list()
    contactn = Contact("Ivan_new", "Ivanov1_new", "My company1", "Voronezh Kirova street 91 151", "31-33-31",
        "8-900-800-7001", "17-18-11", "my_homepage1.ru")
    contactm = random.choice(old_contacts)
    contactn.id = contactm.id
    app.contact.modify_contact_by_id(contactn.id, contactn)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contactm)
    old_contacts.append(contactn)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

