from model.group import Group
import pytest
import random
import string
from data.groups import constant as test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])

def test_add_group(app, group):
    # group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def clear(s):
#     return re.sub("[() -]","",s)
