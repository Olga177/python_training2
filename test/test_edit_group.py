from model.group import Group


def test_edit_group2(app):
    app.group.edit_group(Group(name="group_name2", header="group_header2", footer="group_footer2"))
