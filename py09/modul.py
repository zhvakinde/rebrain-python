import os
import psutil as ps
nm = {'user_name': os.uname(),'memory_total': ps.virtual_memory().total, 'memory_used': ps.virtual_memory().used, 'memory_percent': ps.virtual_memory().percent}
