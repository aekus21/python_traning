class GroupHelper:
    def __init__(self, group):
        self.group = group

    def open_groups_page(self):
        wd = self.group.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.group.wd
        self.open_groups_page()
        # create new group
        wd.find_element_by_name("new").click()
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
        # submit new group
        wd.find_element_by_name("submit").click()
        self.return_group_page()

    def return_group_page(self):
        wd = self.group.wd
        wd.find_element_by_link_text("groups").click()
