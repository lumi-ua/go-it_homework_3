from datetime import datetime, timedelta
from collections import defaultdict
employees = [{"name":"Ilona", "birthdate": datetime(1987, 6, 30)},
            {"name": "Anatolii", "birthdate": "28.06.1990"},
            {"name": "Mikolay", "birthdate": datetime(1986, 7, 3)},
            {"name": "Elena", "birthdate": "24.06.1983"},
            {"name": "Pitier", "birthdate": datetime(1990, 7, 1)},
            {"name": "Angel", "birthdate": "24.06.2000"},
            {"name": "Anna", "birthdate": datetime(1985, 6, 28)},
            {"name": "Marina", "birthdate": "26.06.1989"},
            {"name": "Vladislav", "birthdate": "27.06.1991"},
            {"name": "Svitlana", "birthdate": "25.06.1987"}]

def get_period() -> tuple([datetime.date, datetime.date]): # передавать в эту функцию ничего не будем, но будем возвращать tuple с двумя значениями
        current_date = datetime.now()   # определим субботы
        start_period = current_date + timedelta(days=5-current_date.weekday())      # здесь мы возвращаем субботу и вычисляем следующую пятницу
        monday = current_date + timedelta(days=5-current_date.weekday() + 2)
        #print("monday:", str(monday.date()))
        #print("sp:", start_period.date())
        return start_period.date(), (start_period + timedelta(6)).date(), monday  # здесь мы возвращаем субботу и вычисляем следующую пятницу
        

# дальше мы создадим функцию которая будет перебирать наших работников:

def check_employees(list_employees: list) -> None: # пока ничего не будет возвращать
    result = defaultdict(list)   # оформление поздравления
    current_year = datetime.now().year # вызываем текущий год
    
    for employee in list_employees: # в каждой переменной у нас будут работники
        br_date = employee["birthdate"]
        if isinstance(br_date, datetime):  # превратим получившийся список на нормальные 100% даты
            br_date = br_date.date()
        else:
            br_date = datetime.strptime(br_date, "%d.%m.%Y").date()  #разпарсим, то есть строку превратим в полноценные даты с помощью мини-языка
        br_date = br_date.replace(year=current_year) # заменили год рождения на текущий год
        start, end, monday = get_period()   # проверим входят ли наши выходные сюда

        #print("start-end:", start, end)
        if start <= br_date <= end: # если наше br_date входит то мы можем :
            if br_date.weekday() in (5,6):
                #result["Mondey"].append(br_date)   # то мы добавляем в result 
                result[monday.date()].append(employee["name"])
            else:
                 #result[br_date.strftime("%A")].append(br_date) #сюда добавляем другие дни
                 result[br_date].append(employee["name"])
    return result
            
        #print(br_date.date()) # теперь наши даты имеют одинаковый вид
    
# Теперь нам нужно заменить год, то есть нам нужно узнать в этом ли году выпадает дата др
# год мы можем взять с текущей даты, сделать это лучше нужно вначале нашей функции, чтобы она крутилась
# в функции, то есть формировалась наша текущая дата, точнее год при запуске функции а не всего модуля
# после создания текущего года наш получившийся список др нужно заменить на текущий год
if __name__ == "__main__":
    for key , value in check_employees(employees).items():
        #print(key, [v.strftime("%A") for v in value])
        print(key.strftime("%A"), value, " : " + str(key))
    #print(get_period())
# далее нужно определить диапозон который нам нужен в этом месяце, чтобы определить попадает ли дата
# дня рождения в текущем месяце создадим новую функцию 
