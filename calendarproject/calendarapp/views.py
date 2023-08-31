from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.
def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    name = "nagendra"
    month =month.capitalize()
    #convert month from name to number
    month_number =list(calendar.month_name).index(month)
    month_number =int(month_number)
    #create a calendar
    cal = HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    current_year =now.year
    
    #get current time
    time =now.strftime('%I: %M: %S %p')
    return render(request,
        'calendarapp/home.html',{
        "name":name,
        "year":year,
        "month":month,
        "month_number": month_number,
        "cal":cal,
        "current_year": current_year,
        "time":time,
        })