import jsonpickle
from model.group import Group
import string
import random
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of grops", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group("", "", "")] + [
    Group(name = random_string("name", 10), header = random_string("header", 30),
          footer = random_string("footer", 30))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))