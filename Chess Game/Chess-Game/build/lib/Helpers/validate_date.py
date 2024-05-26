import datetime

class DateValidator:
    @staticmethod
    def validate_date(date):
        # Assuming date format is "YYYY-MM-DD"
        try:
            year, month, day = map(int, date.split("-"))
            date_obj = datetime.date(year, month, day)
            return True
        except ValueError:
            return False