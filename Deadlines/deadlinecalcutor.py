import datetime

#declare variables

totalNoDays = 0
strDeadline = ""
NoWeeks = 0
NoDays = 0

#get the current date

currentdate = datetime.date.today()

#get the deadline date

strDeadline = input("When is the task due (mm/dd/yyyy): ")

deadline = datetime.datetime.strptime(strDeadline,"%m/%d/%Y").date()

#get the number of days between the two

totalNoDays = deadline - currentdate

#get the weeks and days in between

NoWeeks = totalNoDays.days / 7

#number of days

NoDays = totalNoDays.days % 7

#show your results

print(" you have {} weeks and {} days until the deadline".format(NoWeeks,NoDays))