from mailing import Mailing
from address import Address

from_address = Address(123456, "Москва", "Советская", 305, 1)
to_address = Address(123457, "Саров", "Советская", 5, 1)
cost = 500
track = "TRACK123456789"

mailing = Mailing(to_address=to_address, from_address=from_address, cost=500, track="TRACK123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")