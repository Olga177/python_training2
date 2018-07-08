from model.group import Group


def test_edit_group2(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.group.edit_group(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
