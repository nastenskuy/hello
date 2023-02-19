# вправа 1
print (60*60)
# вправа 2 
seconds_per_hour=60*60
print(seconds_per_hour)
# вправа 3
seconds_per_hour=60*60*24
print(seconds_per_hour)
# вправа 4
seconds_per_day=60*60*24
print(seconds_per_day)
# вправа 5
print(f'{seconds_per_day}/{seconds_per_hour}={seconds_per_day}/{seconds_per_hour}')
# вправа 6
print(f'{seconds_per_day}//{seconds_per_hour}={seconds_per_day}//{seconds_per_hour}')
# вправа 7
a = 5
b = 2
c = 6
d = 7
e = 24
s = 14
print (f'{a}+{d}={a+d}')
print (f'{s}-{b}={s-b}')
print (f'{c}*{b}={c*b}')
print (f'{e}/{b}={e/b}')
# вправа 8
print('Твоє ульблене число?') # треба натиснути 31, для того щоб програма продовжила працювати
fnumber = input()
print('моє також 31', fnumber)
# вправа 9
my_variable = "Hello"
print(my_variable.upper())
print(my_variable.lower())
# вправа 10
poem = '''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''
print(poem[0])
print(len(poem))
a = poem.startswith("Yes")
print(a)
b = poem.endswith("I shall live!")
print(b)
a = poem.find(",")
print(a)
b = poem.rfind(",")
print(b)
c = poem.count(",")
print(c)
a = poem.isalnum()
print(a)
# задача 1
a = "Hello, world"
print(a)
a = "My name is Nastya!"
print(a)
# задача 2
a = "Maria"
print("Hello,", a , ",do you like school?")
# задача 3
famous_person = "Сергій Жадан"
message = "Любов варта всього - варта болю твого, варта твоїх розлук, варта відрази і мук, псячого злого виття, шаленства та милосердь. Варта навіть життя. Не кажучи вже про смерть."
print(famous_person, "якось сказав:",message)
# задача 4
txt = "  \t Anastasia \n  "
print(txt.strip())
print(txt.rstrip())
print(txt.lstrip())
# задача 5
print("Кричун Анастасія")
print("Україна")
print("58012")
print("м.Чернівці")
print("вул.Братів Кантемирів")
print("6 А")
# задача 6
a =  "is only {distance:.1f} inches"
print(a.format(distance = 39.37))
a =  "is only {distance:.1f} foot"
print(a.format(distance = 3.28))
a =  "is only {distance:.1f} miles"
print(a.format(distance = 0.06))
a =  "is only {distance:.1f} yards"
print(a.format(distance = 1.09))
# задача 7
weekends = 30
weekends_in_seconds = 60*weekends
weekends_in_minutes = 60*weekends
weekends_in_hours = 24*weekends
print('{:<10} {:<10}'.format(weekends_in_seconds, weekends_in_minutes, weekends_in_hours))
# задача 9
a = input("numeric")
asum = [int(x) for x in a if x.isnumeric()]
print(asum)
b = sum(asum)
print(b)

