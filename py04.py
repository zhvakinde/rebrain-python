#lesson4
list_dict = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]
n_disk = (input('Введите номер накопителя: '))
if not n_disk or not n_disk.isdigit():
    exit('Некорректные данные! Введите натуральное число') 
elif int(n_disk) < len(list_dict):
    disk = list_dict[int(n_disk)]
    size = round((int(disk['total'])-int(disk['used']))/1073741824, 1)
    percent = round(int(int(disk['total'])-int(disk['used']))/(int(disk['total'])/100), 1)
    if int(size) < 10 or int(percent) < 5:
        print(f'на накопителе {n_disk} критически мало свободного места')
    elif int(size) < 30 or int(percent) < 10:
        print(f'на накопителе {n_disk} мало свободного места')
    else:
        print(f'на накопителе {n_disk} достаточно свободного места')       
else:
    exit('Накопитель с таким номером отсутствует')
    