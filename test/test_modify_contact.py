__author__ = 'tester'

from model.contact import Contact

def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first(Contact("Ivan1", "Ivanov1", "My company1", "Voronezh Kirova street 91 151", "31-33-31",
        "8-900-800-7001", "17-18-11", "my_homepage1.ru"))
    app.session.logout()



