__author__ = 'tester'

def test_modify_contact(app):
    app.contact.delete_first()
