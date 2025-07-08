def month_to_season(month_number):

    
    seasons = {1:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6:"Лето",
              7:"Лето", 8:"Лето", 9:"Осень", 10:"Осень", 11:"Осень", 12:"Зима"}


    if month_number not in seasons:
        raise ValueError('Номер месяца должен быть между 1 и 12')
    

    return seasons.get(month_number)
print(month_to_season(3))
print(month_to_season(12))
print(month_to_season(6))
print(month_to_season(13))

