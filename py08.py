#lesson8
#task1
list_1 = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]
#task2
list_2 = []
def parse_2(inp):
    for disk in inp:
        size = int((int(disk['total'])-int(disk['used']))/1073741824)
        percent = int(int(disk['total'])-int(disk['used']))/(int(disk['total'])/100)
        if int(size) < 10 or int(percent) < 5:
           out= {'id': disk['id'], 'memory_status': 'memory_critical'}
           yield out
        elif int(size) < 30 or int(percent) < 10:
           out = {'id': disk['id'], 'memory_status': 'memory_not_enough'}
           yield out
        else:
           out = {'id': disk['id'], 'memory_status': 'memory_ok'}
           yield out
#task3
for i in parse_2(list_1):
       list_2.append(i)
list_3 = list({**a, **b} for a, b in zip(list_1, list_2))
#task4
print(list_3)
#task5
log = [
'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
'May 20 11:01:12 PC-00102 PackageKit: daemon start',
'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'
]
#task6  
sort_1 = sorted(log, key=lambda a: a.split()[2])
print(sort_1[2])
#task7
filt_1 = list(filter(lambda b:  b.split()[3] == 'PC-00102', log))
print(filt_1)
#task8
filt_2 = list(c[c.find("kernel:")+8:] for c in (filter(lambda b:  b.split()[4] == 'kernel:', log))) 
print(filt_2)
      

  