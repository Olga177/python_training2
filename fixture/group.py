from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not ((wd.current_url.endswith('groups.php') and len(wd.wd.find_elements_by_name("new"))) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # Open group page
        self.open_group_page()
        # Initiating group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submitting group form
        wd.find_element_by_name("submit").click()
        # Return to group page
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Open modification form
        wd.find_element_by_name("edit").click()
        # Populate group form updates
        self.fill_group_form(new_group_data)
        # Submit updated form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Select first group
        self.select_first_group()
        # Edit first group
        wd.find_element_by_name("edit").click()
        # Populate group form
        self.fill_group_form(group)
        # Submitting group form
        wd.find_element_by_name("update").click()
        # Return to group page
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        if not ((wd.current_url.endswith('groups.php') and len(wd.wd.find_elements_by_name("new"))) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name('selected[]').get_attribute('value')
            groups.append(Group(name=text, id=id))
        return groups
