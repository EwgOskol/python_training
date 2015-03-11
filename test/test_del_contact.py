__author__ = 'tester'

def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete_first()
    app.session.logout()
