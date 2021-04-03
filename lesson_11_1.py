class Date:
    def __init__(self, string):
        self.string = Date.parse_date(string)

    @classmethod
    def parse_date(cls, arg):
        try:
            return Date.validate_date(*list(map(int, arg.split("-"))))
        except ValueError:
            return "Invalid format"

    @staticmethod
    def validate_date(d, m, y):
        if 0 < d < 32 and 0 < m < 13 and 0 < y < 10000:
            return f"{d}-{m}-{y}"
        else:
            return "Wrong date"


date_1 = Date("21-12-2012")
print(date_1.string)
date_2 = Date("07.07.2007")
print(date_2.string)
date_3 = Date("13-13-2013")
print(date_3.string)
