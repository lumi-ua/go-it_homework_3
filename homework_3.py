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

def get_period() -> tuple([datetime.date, datetime.date]): 
        current_date = datetime.now()   # определим субботы
        start_period = current_date + timedelta(days=5-current_date.weekday())      
        monday = current_date + timedelta(days=5-current_date.weekday() + 2)
        return start_period.date(), (start_period + timedelta(6)).date(), monday  
        

def check_employees(list_employees: list) -> None: 
    result = defaultdict(list)   
    current_year = datetime.now().year 
    
    for employee in list_employees: 
        br_date = employee["birthdate"]
        if isinstance(br_date, datetime):  
            br_date = br_date.date()
        else:
            br_date = datetime.strptime(br_date, "%d.%m.%Y").date()  
        br_date = br_date.replace(year=current_year) 
        start, end, monday = get_period()   

        if start <= br_date <= end: 
            if br_date.weekday() in (5,6):
                result[monday.date()].append(employee["name"])
            else:
                 result[br_date].append(employee["name"])
    return result
            
        
if __name__ == "__main__":
    for key , value in check_employees(employees).items():
        print(key.strftime("%A"), value, " : " + str(key))
    

