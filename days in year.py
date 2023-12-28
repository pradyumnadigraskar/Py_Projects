
year=int(input("enter the year : "))
month=input("enter the month : ")

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a leap year")

def days_in_month(month,year):   
      months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"] 
      month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

      is_leap(year)

      if month in months:
           ind=months.index(month)
           days=month_days[ind]

           print(f"the given month {month} has {days} days")
      else:
           print("invld inp")

days=days_in_month(month,year)
print(days)
             
             
             
    



                  

        
