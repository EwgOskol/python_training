__author__ = 'tester'

from model.contact import Contact


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

    def modify_some_contact(self, index, contact):
        wd = self.app.wd
        # init contact modify
        self.app.open_home_page()
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
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
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
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
                print(element)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                ln = element.find_elements_by_css_selector('td')[1].text
                fn = element.find_elements_by_css_selector('td')[2].text
                self.contact_cache.append(Contact(fname=fn, lname=ln, id=id))
        return list(self.contact_cache)
