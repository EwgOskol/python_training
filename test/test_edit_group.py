__author__ = 'tester'

from model.group import Group

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="test_nm1", header="test_hdr1", footer="test_ftr1"))
    app.session.logout()
