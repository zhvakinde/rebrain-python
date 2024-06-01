#lesson11
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

#m1 = PCMemory(1, os.getlogin(), ps.virtual_memory().total, ps.virtual_memory().used)
m1 = PCMemory(1, os.getlogin(), ps.virtual_memory().total, ps.virtual_memory().used, ps.virtual_memory().percent)

m1.show_user_percent()
print(m1.is_enough_memory())

