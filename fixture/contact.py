from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:
    def __init__(self,app):
        self.app = app

    #открывает создание нового контакта
    def new_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    #заполняет данные в форме
    def fill_form_wo_group(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # wd.find_element_by_name("photo").send_keys(contact.photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)

    #заполняет группу в контакте
    def fill_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(group)

    #сохраняет новый контакт
    def save_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[20]").click()

    #нажимает на элемент home в горизонтальном меню
    def open_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    #выбирает и удаляет первый контакт
    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_home()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_home()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    # открывает контакт на редактирование по индексу
    def open_contact_editor(self, index):
        wd = self.app.wd
        self.open_home()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    # открывает контакт на просмотр по индексу
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    # сохраняет контакт после редактирования
    def save_new_contact_data(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.open_home()

    #сохранение контакта с группой
    def save_contact_w_group(self, new_contact, new_one_group):
        wd = self.app.wd
        self.new_contact_form()
        self.fill_form_wo_group(new_contact)
        self.fill_group(new_one_group)
        self.save_contact()
        self.contact_cache = None

    #сохранение контакта без группы
    def save_contact_wo_group(self, new_contact):
        wd = self.app.wd
        self.new_contact_form()
        self.fill_form_wo_group(new_contact)
        self.save_contact()
        self.contact_cache = None

    def edit_contact(self):
        self.edit_contact_by_index(0)

    # редактирование контакта
    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_editor(index)
        self.change_contact_data(new_contact_data)
        self.save_new_contact_data()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_name("selected[]"))

    def change_contact_data(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("bday", contact.birth_day)
        self.change_field_value("bmonth", contact.birth_month)
        self.change_field_value("byear", contact.birth_year)
        self.change_field_value("aday", contact.anniversary_day)
        self.change_field_value("amonth", contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                cells = element.find_elements_by_css_selector('td')
                texts = []
                for cell in cells:
                    texts.append(cell.text)
                id = element.find_element_by_name('selected[]').get_attribute('value')
                all_phones = cells[5].text
                all_address = cells[3].text
                all_email = cells [4].text
                self.contact_cache.append(Contact(fname=texts[2], lname=texts[1], ids=id,
                                                  all_phones_from_homepage = all_phones, address=all_address,
                                                  all_email = all_email))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_editor(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').text
        return Contact(fname=firstname, lname=lastname, ids=id, homephone=homephone,
                       workphone=workphone, mobilephone=mobilephone, email1=email1,
                       email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        return Contact(homephone=homephone,
                       workphone=workphone, mobilephone=mobilephone)

    def add_contact_to_group(self, contact_id, group_name):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name('to_group').click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_name)
        wd.find_element_by_name('add').click()

