# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("Ivan", "Ivanov", "My company", "Voronezh Kirova street 91 154", "31-33-37",
        "8-900-800-7000", "17-18-19", "my_homepage.ru"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("", "", "", "", "", "", "", ""))
    app.session.logout()


