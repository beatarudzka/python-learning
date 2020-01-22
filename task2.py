#import datetime
import datetime

# asking name
name = input('Type your name:')

# asking age
age = input('Type your age:')

# get the current year
now = datetime.datetime.now()

# get difference between age x 100 years
diff = 100 - int(age)

# show exactly year that user will turn 100 years old
print('Hi '+name+" you will complete 100 years in ", (now.year+diff))
