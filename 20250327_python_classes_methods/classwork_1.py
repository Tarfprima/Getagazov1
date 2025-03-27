from datetime import datetime  # для текущей даты и времени

class Weather:
    def __init__(self, temp, sunny=, precip="", year=0, month=0, day=0, hour=0, minute=0, second=0):

        self.temp = temp  
        self.sunny = sunny  
        self.precip = precip  
       
        num1 = datetime.now() 
        
        if year == 0:
            self.year = num1.year
        else:
            self.year = year
        
        if month == 0:
            self.month = num1.month
        else:
            self.month = month
            
        if day == 0:
            self.day = num1.day
        else:
            self.day = day
            
        # если час не пеедали, берем текущий
        if hour == 0:
            self.hour = num1.hour
        else:
            self.hour = hour
            
# проверяем как работает

