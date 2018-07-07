from model.group import Group


def test_add_group2(app):
    app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.session.logout()


def test_add_empty_group2(app):
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
