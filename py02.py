# lesson 2
log1 = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
print(log1[:15]) 
print(log1[log1.find("ad ")+3:log1.rfind("]:" )+1])
print(log1.replace('ideapad', 'PC-12092'))
print(log1.find('failed'))
print(log1.count('s')+log1.count('S'))
print(int(log1[7:9])+int(log1[10:12])+int(log1[13:15]))
log2 = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
data = log2[:15]
message = log2[37:-22]
error = log2[-20:]
print(f'The PC "{log2[16:23]}" receive message from service "{log2[24:35]}" what says "{message}" because "{error}" at {data}')
