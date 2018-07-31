from model.group import Group
from random import randrange
import random

def test_delete_some_group(app,db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name ='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert sorted(old_groups, key= Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_group2(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="group_name", header="group_header", footer="group_footer")
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key= Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)