# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Ivan", "Ivanov", "My company", "Voronezh Kirova street 91 154", "31-33-37",
        "8-900-800-7000", "17-18-19", "my_homepage.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print(new_contacts)

# def test_add_empty_contact(app):
#    app.contact.create(Contact("", "", "", "", "", "", "", ""))

