import datetime

class birthday_calculator:     
    def __init__(self, birth_date, birth_time):
        self.birth_date = birth_date
        self.birth_time = birth_time
        
        
    def next_bithday():    
    # create the birthday_delta
      
    #subtract today from the birthday_delta    
    # sum bugs up there
        pass
      
    def num_day_lived(self):
        # next let's see calculate the number of day spent
        today_date = datetime.date.today()
        birth_day = datetime.datetime.strptime(self.birth_date, '%Y-%m-%d')
        return (datetime.date.today() - birth_day.date()).days
        
         
    def num_hours_lived(self):
        # calculate the number of days lived
        return f'{self.num_day_lived() * 24 :,}'
        
    def num_seconds_lived(self):
        # calculate the number of day lived
        return  f'{self.num_day_lived() * 24 * 60 :,}'
        
    def num_sleep_hour(self):
        # calculate the number of hour spent sleeping
        return f'{self.num_day_lived() * 24 // 0.33:,}'
        
    def num_sleep_day(self):
        # calculate the number of dady spent sleeping
        return f'{self.num_day_lived() // 0.33:,}'
        
        
        
    
    


    
