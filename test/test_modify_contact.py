__author__ = 'tester'

from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="tester", lname="tester", company="Test Inc"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Ivan1", "Ivanov1", "My company1", "Voronezh Kirova street 91 151", "31-33-31",
        "8-900-800-7001", "17-18-11", "my_homepage1.ru")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




