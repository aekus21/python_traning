from selenium.webdriver.support.ui import Select

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
        wd.find_element_by_name("photo").send_keys(contact.photo)
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
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
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
        wd.find_element_by_link_text("home").click()

    #выбирает и удаляет первый контакт
    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_home()

    # открывает контакт на редактирование
    def open_contact_editor(self):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    # def add_group_to_contact(self, contact):
    #     wd = self.app.wd
    #     wd.find_element_by_name("new_group").click()
    #     Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.select_group)
    #     wd.find_element_by_xpath("//input[20]").click()
    ...
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

    #сохранение контакта без группы
    def save_contact_wo_group(self, new_contact):
        wd = self.app.wd
        self.new_contact_form()
        self.fill_form_wo_group(new_contact)
        self.save_contact()

    # редактирование контакта
    def edit_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_editor()
        self.fill_form_wo_group(new_contact_data)
        self.save_new_contact_data()