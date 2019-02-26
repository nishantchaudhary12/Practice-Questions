#pay and hours worked

#lists to store the data from the file
start_time = []
break_start = []
break_end = []
end_time =[]
hours_worked = []
hourly_pay = []
daily_pay = []
last_name = []
first_name = []

#splits the data and stores it in the lists
def clean(value):
    data = line.split()
    start_time.append(int(data[0]))
    break_start.append(int(data[1]))
    break_end.append(int(data[2]))
    end_time.append(int(data[3]))
    hours_worked.append(float(data[4]))
    hourly_pay.append(float(data[5]))
    daily_pay.append(float(data[6]))
    name = " ".join(data[7:])
    names = name.split(",")
    last_name.append(names[0])
    first_name.append(names[1])


for line in open('data.txt',"r"):
    clean(line)


def printTable():
    print('\tStart time\t Break Start time\t Break End time\t  End time\t Hours Worked\t Hourly Pay\t\t Daily Pay\t '
          ' Last name\t\t\t First name')
    for num in range(len(first_name)):
        print(num+1,'\t  ',format(start_time[num],'4d'),'\t\t  ',format(break_start[num],'4d'),'\t\t\t   ',format(break_end[num],'4d'),
        '\t\t',format(end_time[num],'4d'),'\t\t',format(hours_worked[num],'.2f'),'\t\t',format(hourly_pay[num],'.2f'),
        '\t\t\t',format(daily_pay[num],'.2f'),'\t\t',format(last_name[num],'10s'),'\t\t',first_name[num])


def printDetails():
    print('\nTotal number of employees:',len(first_name))

    average_pay = sum(daily_pay)/len(daily_pay)

    print('\nPay:')
    print('Total pay: $',format(sum(daily_pay),'.3f'))
    print('The average pay for the day: $',format(average_pay,'.3f'))

    average_hours = sum(hours_worked)/len(hours_worked)

    print('\nHours worked:')
    print('Average:',average_hours)
    print('Minimum:',min(hours_worked))
    print('Maximum:',max(hours_worked))

if __name__ == "__main__":
    printTable()
    printDetails()
