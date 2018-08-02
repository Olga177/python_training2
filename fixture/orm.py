from pony.orm import *

class ORMFixture:

    db = Database()
    class ORMGroup(db.Entity):
        _table_ ='group_list'
        id = PrimaryKey(int, column ='group_id')
        name = Optional(str, column ='group_name')
        header = Optional(str, column ='group_header')
        footer = Optional(str, column ='group-Footer')


