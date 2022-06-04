amount = []
hours = {} #dictionary for every hour and reading levels in that hour
days = {}   
weeks = {}
def createdict(filename):
    with open(filename, "r+") as csvfile:
        content = csvfile.readlines()
        for line in content:
            piece = line.split(',')
            appy = piece[5].split('.')
            hour = appy[0].split(':') #breaks the date value to the hour
            try:
                if int(piece[2]) < 0: #if water level is less than 0 move on
                    next
                elif hour[0] in hours.keys(): #if the hour is already a key then create a list in that key which holds every water reading
                    if not isinstance(hours[hour[0]], list):
                        hours[hour[0]] = [hours[hour[0]]]
                    hours[hour[0]].append(piece[2])
                else:
                    hours[hour[0]] = piece[2] #if the hour is not a key, create a new key for that hour
                piece.clear()
            except ValueError: #if the value is a string like the first line couple lines for example
                next
        for line in content:
            piece = line.split(',')
            appy = piece[5].split()
            try:
                day = appy[0]
                amount.append(day)
                try:
                    if int(piece[2]) < 0: #if water level is less than 0 move on
                        next
                    elif day in days.keys(): 
                        if not isinstance(days[day], list):
                            days[day] = [days[day]]
                        days[day].append(piece[2])
                    else:
                        days[day] = piece[2] #if the hour is not a key, create a new key for that hour
                except ValueError: #if the value is a string like the first line couple lines for example
                    next

            except IndexError:
                next
    average(days)
    average(hours)    
    writefile(filename.join('hours'), hours)
    writefile(filename.join('days.csv'), days)

def average(wiener):
    dict = wiener.items()
    for key, value in dict:
        numlist = []
        try:
            if type(value) == list:
                for num in value:
                    numlist.append(int(num)) #for every water reading turn it into an integer and put it into a list
                average = sum(numlist) / len(numlist) #find the average
                wiener[key] = average #add the average to dictionary
            else:
                wiener[key] = value
        except ValueError:
            next

def writefile(file, dict):
    with open(file, 'w') as thefile:
        thefile.truncate(0)
        thefile.write('date, waterlevel\n')
        for key, value in dict.items():
            thefile.write(f"{key}, {value}\n")
    
    