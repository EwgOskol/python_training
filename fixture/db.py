__author__ = 'tester'

import mysql.connector
from model.group import Group
from model.contact import Contact
from model.cont_in_group import Cont_in_Groups

class dbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True


    def get_group_list(self, orderby=None):
        list = []
        additional_str = ""
        if orderby is not None:
            additional_str = "order by %s " % orderby
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list %s " % additional_str)
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_address_in_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list.append(Cont_in_Groups(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list

    def get_address_not_in_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select addressbook.id, group_list.group_id from addressbook, group_list "
                           "where addressbook.deprecated='0000-00-00 00:00:00' "
                           "and (addressbook.id, group_list.group_id) not in "
                           "(select address_in_groups.id, address_in_groups.group_id from address_in_groups where deprecated='0000-00-00 00:00:00')")
            for row in cursor:
                (id, group_id) = row
                list.append(Cont_in_Groups(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, company, address, homepage, home, mobile, work, phone2, "
                           "email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, fname, lname, company, address, hm_page, homephone, mobilephone, workphone, secondaryphone, email, email2, email3) = row
                list.append(Contact(id=str(id), fname=fname, lname=lname, company=company, address=address,
                                    hm_page=hm_page, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                                    secondaryphone=secondaryphone, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()