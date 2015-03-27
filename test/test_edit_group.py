__author__ = 'tester'

from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="test_nm1", header="test_hdr1", footer="test_ftr1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

