from sys import maxsize


class Contact:
    def __init__(self, first_name=None, last_name=None, id=None,
                 home_phone=None, mobile_phone=None,
                 work_phone=None, secondary_phone=None,
                 all_phones_from_home_page=None,
                 email1=None, email2=None, email3=None,
                 all_emails_from_home_page = None):
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
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

