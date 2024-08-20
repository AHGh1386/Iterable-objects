from datetime import timedelta

class IterableDateRange:
    
    def __init__(self, start_date , end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.present_day = start_date
        
    def __iter__ (self):
        return self
    
    def __next__ (self):
        if self.present_day >= timedelta(days=1):
            raise StopIteration
        today = self.present_day
        self.present_day += timedelta(days=1)
        return today
    
"""
for day in IterableDateRange(date(2024,1,1), date(2024,1,6)):
    print day 
"""
