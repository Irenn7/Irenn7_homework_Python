from smartphone import Smartphone

catalog = [
    Smartphone("Sasmsung", "Galaxy", +79000000001),
    Smartphone("VIVO", "Y", +79000000002),
    Smartphone("Infinix", "NOTE", +79000000003),
    Smartphone("Sasmsung", "Galaxy", +79000000004),
    Smartphone("Xiaomi", "Redmi", +79000000005),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")

