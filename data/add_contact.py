from model.contact import Contact
import random
import string


constant = [
    Contact(first_name ='first_name1', last_name = 'last_name1', home_phone = 'home_phone1',
            mobile_phone='mobile_phone1', work_phone='work_phone1',
            email1 = 'email11',email2 = 'mail21', email3 = 'email31'),
    Contact(first_name='first_name2', last_name='last_name2', home_phone='home_phone2',
            mobile_phone='mobile_phone2', work_phone='work_phone2',
            email1='email12', email2='mail22', email3='email32')
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(first_name="", last_name="", address="",
                     home_phone="", mobile_phone="",
                     work_phone="", secondary_phone="",
                     email1="", email2="", email3="", )] + [
                Contact(first_name=random_string("first_name1", 5), last_name=random_string("last_name1", 5),
                        address=random_string("address1", 5),
                        home_phone=random_string("home_phone1", 5), mobile_phone=random_string("mobile_phone1", 5),
                        work_phone=random_string("work_phone1", 5),
                        secondary_phone=random_string("secondary_phone1", 5),
                        email1=random_string("email1", 5), email2=random_string("email2", 5),
                        email3=random_string("email3", 5))
                for i in range(5)
            ]
