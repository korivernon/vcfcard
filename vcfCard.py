import os
import shutil

class vcfCard:
    def __init__(self, fn, ln="", mn= "", number=None, email=None, dob=None, website=None, company=None, school=None, major=None, grad_year = None):
        '''
        :param fn: First name (str)
        :param ln: Last name (str)
        :param mn: Middle name (str)
        :param number: Number in the format XXXXXXXXXX (str)
        :param email: this is the email in the format of (str)
        :param dob: this is the email in the format of (str)
        :param company: this is the company name (str)
        :param school: this is the school name (str)
        :param major: this is the major name (str)
        :param grad_year: this is the format DD-YY-MM (str)
        '''
        self.fn = fn
        self.ln = ln
        self.mn = mn
        self.num = number
        self.dob = dob
        self.grad = grad_year
        self.url = website
        self.email = email
        self.comp = company
        self.school = school
        self.major = major

    def add_ln(self, lname):
        self.ln = lname
        return self.ln

    def add_mn(self, mname):
        self.mn = mname
        return self.mn

    def add_num(self, number):
        self.num = number
        return self.num

    def add_dob(self, new_date):
        self.dob = new_date
        return self.dob

    def add_grad(self, grad):
        self.grad = grad
        return self.grad

    def add_url(self,url):
        self.url = url
        return self.url

    def add_comp(self, comp):
        self.comp = comp
        return self.comp

    def add_school(self, school):
        self.school = school
        return self.school

    def add_major(self, major):
        self.major = major
        return self.major

    def make_comp_line(self):
        line = ""
        if self.comp is not None:
            line += self.comp + " | "
        if self.school is not None:
            line += self.school + " | "
        if self.major is not None:
            line += self.major + " | "
        if self.grad is not None:
            line += "c/o " +  self.grad + " | "
        return line

    def __str__(self):
        if self.ln != "" and self.mn != "":
            card = f"{self.ln},{self.mn} {self.fn}"
        elif self.ln != "":
            card = f"{self.ln},{self.fn}"
        else:
            card = f"{self.fn}"
        comp = self.make_comp_line()
        if comp != "":
            card += f"\n{comp}"
        if self.num is not None:
            card += f"\n{self.num}"
        if self.email is not None:
            card += f"\n{self.email}"
        if self.url is not None:
            card += f"\n{self.url}"
        return card

    def make_card(self):
        st = "BEGIN:VCARD\nVERSION:3.0\n"
        st += f"N:{self.ln};{self.fn};{self.mn};;\n"
        comp = self.make_comp_line()
        if comp != "":
            st += f"ORG:{self.make_comp_line()}\n"
        if self.email:
            st += f"EMAIL;type=INTERNET;type=HOME;type=pref:{self.email}\n"
        if self.num:
            st += f"TEL;type=CELL;type=VOICE;type=pref:{self.num}\n"
        if self.url:
            st += f"item2.URL;type=pref:{self.url}\n"
            st += f"item2.X-ABLabel:_$!<HomePage>!$_\n"
        if self.dob:
            st += f"BDAY:{self.dob}\n"
        st += "END:VCARD"
        return st

    def export_card(self):
        contents = self.make_card()
        if self.ln != "":
            card_name = f"{self.fn}_{self.ln}.vcf"
        else:
            card_name = f'{self.fn}'
        file_obj = open(card_name, "w")
        for line in contents:
            try:
                file_obj.write(line)
            except:
                os.remove(card_name)
                print("error: failure to add card")
                return False
        file_obj.close()
        return True
