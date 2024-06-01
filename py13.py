#lesson13
import os
import psutil as ps
class PercentError(Exception):
    pass
class PCMemory:
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent=None):
        self.id = pc_id
        self.name = user_name
        try:
            self.mtotal = int(memory_total)
            self.mused = int(memory_used)
            try:
                if self.mtotal < 0 or self.mused < 0 or self.mtotal < self.mused:
                   raise ValueError 
            except ValueError:
                print('wrong memory value, default value used')
                self.mtotal = 107374182400
                self.mused = 0   
        except ValueError:
            print('wrong memory value, default value used')
            self.mtotal = 107374182400
            self.mused = 0
        try:          
            if memory_percent is None:
               raise ValueError
            else:
                self.mpercent = float(memory_percent)
        except ValueError:
            print('wrong percent value, value calculated automatically')
            self.mpercent = (self.mused/(self.mtotal/100))     
        try:
            if self.mpercent < 0 or self.mpercent > 100:
               raise PercentError('Percent value must be between 0 and 100')
        except PercentError as p1:
            print(p1)

    def show_user_percent(self):
        return print(f'PC with id {self.id} used {self.mpercent} percent of memory')

    def is_enough_memory(self):
        if (100-self.mpercent) < 10 or (self.mtotal-self.mused) < 1073741824:
            return False
        else:
            return True

m1 = PCMemory(1, 'root', 100, 20, 120)
print(m1.mtotal, m1.mused, m1.mpercent)