from model.group import Group
import string
import random

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [Group("", "", "")] + [
#     Group(name = random_string("name", 10), header = random_string("header", 30),
#           footer = random_string("footer", 30))
#     for i in range(5)
# ]

testdata = [
    Group('name1', 'header1', 'footer1'),
    Group('name2', 'header2', 'footer2'),
    Group('name3', 'header3', 'footer3')
]