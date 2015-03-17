__author__ = 'tester'

from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="tester", lname="tester", company="Test Inc"))
    app.contact.delete_first()
