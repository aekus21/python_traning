class EditGroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()

    def change_group_data(self, group):
        wd = self.app.wd
        # fill group info
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.test_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.test_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.test_footer)

    def save_new_group_data(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.open_groups_page()