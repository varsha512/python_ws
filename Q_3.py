"""Write a program to determine the work hours of the day entered based on the timetable provided below."""
week_data = {'Mon':[3,2,2],'Tue':[3,2,2],'Wed':[3,2,2],'Thu':[3,2,1],'Fri':[3,2,1],'Sat':[3,1,0],'Sun':[0,0,0]}
user = input("Enter the weekday: ")
for i in week_data:
    if user in week_data:
        print(week_data[user])
        break
    else:
        print("Sorry..Invalid day")