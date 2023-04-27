from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.


def home(request, year=datetime.now().year, month=datetime.now().month):
    now = datetime.now()
    cal = HTMLCalendar().formatmonth(year, month)
    current_month = now.month
    current_year = now.year
    apple = 'apple'

    return render(request, 'home.html', {'current_year': current_year, 'current_month': current_month, 'apple': apple, 'cal': cal})
