# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.create_contact(Contact("Ivan", "Ivanov", "My company", "Voronezh Kirova street 91 154", "31-33-37",
        "8-900-800-7000", "17-18-19", "my_homepage.ru"))
    app.logout()

def test_add_empty_contact(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.create_contact(Contact("", "", "", "", "", "", "", ""))
    app.logout()


