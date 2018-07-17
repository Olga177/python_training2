from sys import maxsize

class Contact:
    def __init__(self, first_name=None, last_name=None, home_phone=None, mobile_phone=None,
                 work_phone=None, secondary_phone = None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.id = id

    def __repr__(self):
        return " %s:%s" % (str(self.id), self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

