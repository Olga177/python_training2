from model.group import Group
from random import randrange

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name ='test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # Deleting first group in group list 'old_groups'
    old_groups[index:index+1]=[]
    assert sorted(old_groups, key= Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_group2(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="group_name", header="group_header", footer="group_footer")
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key= Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)