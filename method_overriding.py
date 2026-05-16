from abc import ABC, abstractmethod

class PaymentUpdater(ABC):

    def validate_booking(self, booking_obj):
        if not booking_obj:
            raise ValueError(
                "Booking Not Found!!"
            )


    @abstractmethod
    def update(self, value, booking_obj):
        pass



class TotalAmountUpdater(PaymentUpdater):

    def update(self, new_total_amount_to_update, booking_obj):

        self.validate_booking(booking_obj)

        if new_total_amount_to_update<0:
            raise TypeError(
                "AMount should be greater than 0!!"
            )

        booking_obj.total_amount = new_total_amount_to_update


class FactoryPaymentUpdate:
    _UPDATES = {
        "total_amt" : TotalAmountUpdater()
    }


    @classmethod
    def get_updater(cls, field_name):
        return cls._UPDATES.get(field_name)


class Booking:
    def __init__(self, start_date, end_date, total_amount):
        self.st_dt = start_date
        self.end_dt = end_date
        self.total_amount = total_amount

    def __str__(self):
        return f"{self.st_dt} :: {self.end_dt} :: {self.total_amount}"


b1 = Booking("2026-05-16", "2026-05-19", 1000)

print(b1)

updator = FactoryPaymentUpdate.get_updater("total_amt")

if updator:
    updator.update(2400, b1)

print(b1)