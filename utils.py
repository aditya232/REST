from datetime import timedelta, date
from models import Update

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_dates(days,start_date,end_date):
	dates = []
	for date in daterange(start_date, end_date):
	     if date.weekday() in days:
	     	dates.append(date)
	return dates

def process_form(form):
	days = set()
	if form.all_days.data :
		days = set([i for i in range(0,7)])
	if form.all_weekends.data:
		days = set([i for i in range(5,7)])
	if form.all_weekdays.data:
		for i in range(0,5):
			days.add(i)
	if form.mondays.data:
		days.add(0)
	if form.tuesdays.data:
		days.add(1)
	if form.wednesdays.data:
		days.add(2)
	if form.thursdays.data:
		days.add(3)
	if form.fridays.data:
		days.add(4)
	if form.saturdays.data:
		days.add(5)
	if form.sundays.data:
		days.add(6)
	return get_dates(days,form.start_date.data,form.end_date.data)	