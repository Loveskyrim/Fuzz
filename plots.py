import os

path = '/home/andrey/Рабочий стол/FUZZING_LENINGRAD'

summ = 0
file_num = 0

def norm_hours(time1, time2):
    try:
        return abs(int(time1) - int(time2)) / 3600
    except:
        return 0.0

def parse_line(line1, line2):
    time1 = line1.split()[0]
    time2 = line2.split()[0]
    return norm_hours(time1.strip(',. '), time2.strip(',. '))


def plotting(file, folder):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        if len(lines) > 1:
            first_line = lines[1]
            last_line = lines[-1]
            hours = parse_line(first_line, last_line)
            global summ, file_num
            summ += hours
            file_num += 1
            print(os.path.abspath(file), ': ', hours)
        else:
            print(os.path.abspath(file), ': False')


def passage(file_name, folder):
    for file in os.scandir(folder):
        if file.is_file():
            if file_name in file.name:
                plotting(file, folder)
        else:
            passage(file_name, file.path)


passage('plot', path)
print("Total hours:", summ)
print("Total files:", file_num)
