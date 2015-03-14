# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_new_contact(app):
    app.contact.create(Contact("Ivan", "Ivanov", "My company", "Voronezh Kirova street 91 154", "31-33-37",
        "8-900-800-7000", "17-18-19", "my_homepage.ru"))

def test_add_empty_contact(app):
    app.contact.create(Contact("", "", "", "", "", "", "", ""))


