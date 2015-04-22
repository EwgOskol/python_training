__author__ = 'tester'

from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        # fill form
        self.change_contact_field_value("firstname", contact.fname)
        self.change_contact_field_value("lastname", contact.lname)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.homephone)
        self.change_contact_field_value("mobile", contact.mobilephone)
        self.change_contact_field_value("work", contact.workphone)
        self.change_contact_field_value("homepage", contact.hm_page)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def modify_first(self, contact):
        self.modify_some_contact(0, contact)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).find_element_by_xpath("../..").find_elements_by_tag_name("td")[7].find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        lst = wd.find_elements_by_css_selector('img[alt="Details"]')
        cnt = len(lst)
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()

    def modify_some_contact(self, index, contact):
        wd = self.app.wd
        # init contact modify
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        # fill form new data
        self.change_contact_field_value("firstname", contact.fname)
        self.change_contact_field_value("lastname", contact.lname)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.homephone)
        self.change_contact_field_value("mobile", contact.mobilephone)
        self.change_contact_field_value("work", contact.workphone)
        self.change_contact_field_value("homepage", contact.hm_page)
        # submit contact modify
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        # init contact modify
        self.app.open_home_page()
        self.open_contact_to_edit_by_id(id)
        # fill form new data
        self.change_contact_field_value("firstname", contact.fname)
        self.change_contact_field_value("lastname", contact.lname)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.homephone)
        self.change_contact_field_value("mobile", contact.mobilephone)
        self.change_contact_field_value("work", contact.workphone)
        self.change_contact_field_value("homepage", contact.hm_page)
        # submit contact modify
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def delete_first(self):
        self.delete_some_contact(0)

    def delete_some_contact(self, index):
        wd = self.app.wd
        # edit first contact
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        # init contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # edit first contact
        self.app.open_home_page()
        self.open_contact_to_edit_by_id(id)
        # init contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_css_selector('td')
                id = element.find_element_by_name("selected[]").get_attribute("value")
                ln = cells[1].text
                fn = cells[2].text
                address = cells[3].text
                emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(fname=fn, lname=ln, id=id, address=address, emails=emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(fname=firstname, lname=lastname, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, id=id, address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = search_data("H: (.*)", text)
        workphone = search_data("W: (.*)", text)
        mobilephone = search_data("M: (.*)", text)
        secondaryphone = search_data("P: (.*)", text)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

def search_data(msk, text):
    nnn = ""
    mmm = re.search(msk, text)
    if mmm is not None:
        nnn = mmm.group(1)
    return nnn

