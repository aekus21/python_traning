from sys import maxsize

class Contact:
    def __init__(self,  fname = None, mname = None, lname =None, nickname = None, photo = '',
                 title = None, company = None, address = None, homephone = None, mobilephone = None,
                 workphone = None, fax = None, email1 = None, email2 = None, email3 = None, homepage = None,
                 bday = None, bmonth = None, byear = None, anniverday = None, annivermonth = None,
                 anniveryear = None, all_phones_from_homepage = None, all_email = None, id = None,):
        self.id = id
        self.first_name = fname
        self.middle_name = mname
        self.last_name = lname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = bday
        self.birth_month = bmonth
        self.birth_year = byear
        self.anniversary_day = anniverday
        self.anniversary_month = annivermonth
        self.anniversary_year = anniveryear
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_email = all_email

    def __repr__(self):
        return '%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s' % (self.id, self.first_name, self.last_name, self.address,
                                   self.workphone, self.homephone, self.mobilephone, self.email3, self.email2, self.email1,
                                                  self.all_email, self.all_phones_from_homepage)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id)
                and (self.first_name is None or other.first_name is None or self.first_name == other.first_name)
                and (self.last_name is None or other.last_name is None or self.last_name == other.last_name)
                and (self.address is None or other.address is None or self.address == other.address)
                and (self.all_email is None or other.all_email is None or self.all_email == other.all_email)
                and (self.all_phones_from_homepage is None or other.all_phones_from_homepage is None
                     or self.all_phones_from_homepage == other.all_phones_from_homepage)
                )

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize