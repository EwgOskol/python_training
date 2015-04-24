__author__ = 'tester'

from model.contact import Contact
from model.group import Group
from model.cont_in_group import Cont_in_Groups
import random

def test_remove_contact_to_group(app, db):

    # preconditions
    # if groups list is empty
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    # if contacts list is empty
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="tester_f", lname="tester_l", company="Test Inc"))
    # if none contacts are not included in group
    if len(db.get_address_in_groups_list()) == 0:
        app.contact.move_contact_into_group(db.get_contact_list()[0].id, 0)

    # list of contacts which included in groups
    cont_in_group_old = db.get_address_in_groups_list()

    # choice random pair (contact : group)
    selected_pair = random.choice(cont_in_group_old)
    id_contact = selected_pair.id
    id_group = selected_pair.group_id
    # find position of the selected group in groups list
    index = list(i.id for i in db.get_group_list("group_name")).index(id_group)

    # remove contact from group
    app.contact.remove_contact_from_group(id_contact, index)

    # asserts
    assert len(cont_in_group_old) - 1 == len(db.get_address_in_groups_list())
    cont_in_group_new = db.get_address_in_groups_list()
    cont_in_group_old.remove(Cont_in_Groups(id=id_contact, group_id=id_group))
    assert sorted(sorted(cont_in_group_new, key=Cont_in_Groups.get_id), key=Cont_in_Groups.get_group_id) \
           == sorted(sorted(cont_in_group_old, key=Cont_in_Groups.get_id), key=Cont_in_Groups.get_group_id)
