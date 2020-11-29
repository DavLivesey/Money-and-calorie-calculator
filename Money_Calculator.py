import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = sum(
            record.amount for record in self.records
            if record.date == dt.date.today()
        )
        return today_stats

    def get_week_stats(self):
        week_stats = sum(record.amount for record in self.records if
                         dt.date.today() - dt.timedelta(days=7) <=
                         record.date <= dt.date.today())
        return week_stats


class CashCalculator(Calculator):
    EURO_RATE = 77.96
    USD_RATE = 69.47

    def get_today_cash_remained(self, currency):
        cash = self.limit - self.get_today_stats()
        rates = {
            "usd": {"rate": self.USD_RATE, "val": "USD"},
            "eur": {"rate": self.EURO_RATE, "val": "Euro"},
            "rub": {"rate": 1, "val": "руб"}
        }
        index_remained = cash / rates[currency]["rate"]
        cash_remained = abs(round(index_remained, 2))
        index_value = rates[currency]['val']
        if index_remained > 0:
            return f"На сегодня осталось {cash_remained} {index_value}"
        if index_remained == 0:
            return "Денег нет, держись"
        if index_remained < 0:
            return f"Денег нет, держись: твой долг " \
                   f"- {cash_remained} {index_value}"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_border_today = self.limit - self.get_today_stats()
        if calories_border_today > 0:
            message = (f"Сегодня можно съесть что-нибудь ещё, "
                       f"но с общей калорийностью не более"
                       f"{calories_border_today} кКал")
        else:
            message = "Хватит есть!"
        return message


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


if __name__ == "__main__":
    cash_calculator = CashCalculator(2000)
    calories_calcultor = CaloriesCalculator(2000)

    cash_calculator.add_record(Record(amount=2500, comment="кофе"))
    cash_calculator.add_record(Record(amount=1000,
                                      comment="бар в Танин др",
                                      date="08.11.2019"))
    cash_calculator.add_record(Record(amount=700,
                                      comment="бар в Танин др",
                                      date="27.06.2020"))
    cash_calculator.add_record(Record(amount=800,
                                      comment="бар в Танин др",
                                      date="22.06.2020"))
    cash_calculator.add_record(Record(amount=500,
                                      comment="бар в Танин др",
                                      date="21.06.2020"))
    calories_calcultor.add_record(Record(amount=500,
                                         comment="бар в Танин др"))
    calories_calcultor.add_record(Record(amount=1000,
                                         comment="бар в Танин др",
                                         date="21.06.2020"))
    calories_calcultor.add_record(Record(amount=1000,
                                         comment="бар в Танин др",
                                         date="22.06.2020"))
    calories_calcultor.add_record(Record(amount=1000,
                                         comment="бар в Танин др",
                                         date="27.06.2020"))
    calories_calcultor.add_record(Record(amount=1000,
                                         comment="бар в Танин др",
                                         date="30.06.2020"))

    print(cash_calculator.get_today_cash_remained("rub"))
    print(cash_calculator.get_today_cash_remained("eur"))
    print(cash_calculator.get_today_cash_remained("usd"))
    print(calories_calcultor.get_calories_remained())
    print(calories_calcultor.get_week_stats())
