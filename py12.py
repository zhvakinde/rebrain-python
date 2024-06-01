#lesson12
import os
import psutil as ps
class PCMemory:
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent=None):
        self.id = pc_id
        self.name = user_name
        self.mtotal = memory_total
        self.mused = memory_used
        if memory_percent is None:
            self.mpercent = self.mused/(self.mtotal/100)
        else:
            self.mpercent = memory_percent

    def show_user_percent(self):
        return print(f'PC with id {self.id} used {self.mpercent} percent of memory')

    def is_enough_memory(self):
        if (100-self.mpercent) < 10 or (self.mtotal-self.mused) < 1073741824:
            return False
        else:
            return True

class PCAdvanced(PCMemory):
    def __init__(self, pc_id, user_name, memory_total, memory_used, ld_avg_1m, ld_avg_15m, memory_percent=None):
        PCMemory.__init__(self, pc_id, user_name, memory_total, memory_used, memory_percent)
        self.la1 = ld_avg_1m
        self.la15 = ld_avg_15m

    def is_overloaded(self):
        if self.la1 > self.la15*3:
            return True
        else:
            return False
        
    def __call__(self, i=str('memory')):
       if i == 'memory':
           return super().is_enough_memory()
       elif i == 'load':
           return self.is_overloaded() 
       else:
           return None
        
#m1 = PCAdvanced(1, 'root', ps.virtual_memory().total, ps.virtual_memory().used, ps.virtual_memory().percent, ps.getloadavg()[0], ps.getloadavg()[2])
m1 = PCAdvanced(1, 'root', ps.virtual_memory().total, ps.virtual_memory().used, ps.getloadavg()[0], ps.getloadavg()[2])

print(m1.is_overloaded())
print(m1())
