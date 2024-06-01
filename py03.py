#lesson3
#task1
list_1 = [
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
#task2
n_str = int(input())
str_1 = list_1[n_str]
list_2 = str_1.split(' ')
v_time = (' '.join(list_2[:3]))
v_pc = list_2[3]
v_service = (list_2[4]).replace(':', '')
v_message = (' '.join(list_2[5:]))
dict_1 = {}
dict_1['time'] = v_time
dict_1['pc_name'] =v_pc
dict_1['service_name'] = v_service
dict_1['message'] = v_message
print(': '.join([dict_1.get('pc_name'), dict_1.get('message')]))
#task3
list_3 = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']
list_4 = ['time', 'pc_name', 'service_name', 'message']
dict_2 = dict(zip(list_4, list_3))
#task4
list_dict = [dict_1, dict_2]
print(list_dict)
#task5
set_1 = set(dict_1.values())
set_2 = set(dict_2.values())
print(set_1 & set_2)