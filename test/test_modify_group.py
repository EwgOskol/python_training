__author__ = 'tester'

from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    groupm = random.choice(old_groups)
    groupn = Group(name="New group")
    groupn.id = groupm.id
    app.group.modify_group_by_id(groupm.id, groupn)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(groupm)
    old_groups.append(groupn)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
