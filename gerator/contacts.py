from model.contact import Contact
import string
import random
import re
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

def random_personal_data(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digit_data(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_date_data():
   return str(random.randint(1,31))

def random_month_data():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November"])

def randon_year_data():
    return str(random.randrange(1700, 2250))

test_data_wo_group = [
    Contact(fname = re.sub('  ', ' ', random_personal_data("firstName", maxlen = 10)).strip(),
            mname = random_personal_data("middleName", maxlen = 10),
            lname = re.sub('  ', ' ', random_personal_data("lastnameName", maxlen = 10)).strip(),
            nickname = random_personal_data("nickName", maxlen = 10),
            title = random_personal_data("title", maxlen = 10),
            #photo= 'D:\python_traning\image.jpg',
            company = random_personal_data("nickName", maxlen = 10),
            address = random_personal_data("address", maxlen = 10),
            homephone = "+7" + random_digit_data(maxlen = 10),
            mobilephone = "+7" + random_digit_data(maxlen = 10),
            workphone = "+7" +  random_digit_data(maxlen = 10),
            fax = "+7" + random_digit_data(maxlen = 10),
            email1 = random_personal_data("email1", maxlen = 10),
            email2 = random_personal_data("email2", maxlen = 10),
            email3 = random_personal_data("email3", maxlen = 10),
            homepage = random_personal_data("homepage", maxlen = 10),
            bday = random_date_data(),
            bmonth = random_month_data(),
            byear = randon_year_data(),
            anniverday = random_date_data(),
            annivermonth = random_month_data(),
            anniveryear = randon_year_data()
            )
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(test_data_wo_group))