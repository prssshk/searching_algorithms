# -*- coding: utf-8 -*-


class wedding:
    def __init__(self,male, male_bday, female, female_bday,wedding_date, zags_number):
        self.male = male
        self.male_bday = male_bday
        self.female = female
        self.female_bday = female_bday
        self.wedding_date = wedding_date
        self.zags_number = zags_number

    def __lt__(self, other):
        if self.wedding_date < other.wedding_date:
            return True
        elif int(self.zags_number) < int(other.zags_number) and self.wedding_date == other.wedding_date :
            return True
        elif self.male < other.male and int(self.zags_number) == int(other.zags_number) and self.wedding_date == other.wedding_date:
            return True
        return False

    def __gt__(self, other):
        if self.wedding_date > other.wedding_date:
            return True
        elif int(self.zags_number) > int(other.zags_number) and self.wedding_date == other.wedding_date:
            return True
        elif self.male > other.male and int(self.zags_number) == int(other.zags_number) and self.wedding_date == other.wedding_date:
            return True
        return False

    def __eq__(self, other):
        if int(self.zags_number) == int(other.zags_number) and self.wedding_date == other.wedding_date and self.male == other.male:
            return True
        return False

    def __str__(self):
        return self.zags_number + " " + self.wedding_date + " " + self.male

