from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, SubmitField,DateField,IntegerField,SelectField
from wtforms.validators import DataRequired,NumberRange
from datetime import date
class MyForm(FlaskForm):
	room_type = SelectField('Select room type: ',choices=[('single', 'Single Room'), ('double','Double room')])
	availability = IntegerField('Change availability to',validators=[DataRequired(),NumberRange(min=0, max=5, message="Must be an integer in range [0,5]")])
	price = IntegerField('Change price to',validators=[DataRequired(),NumberRange(min=0)])
	all_days = BooleanField('All Days')
	all_weekdays = BooleanField('All Weekdays')
	all_weekends = BooleanField('All Weekends')
	mondays = BooleanField('Mondays')
	tuesdays = BooleanField('Tuesdays')
	wednesdays = BooleanField('Wednesdays')
	thursdays = BooleanField('Thursdays')
	fridays = BooleanField('Fridays')
	saturdays = BooleanField('Saturdays')
	sundays = BooleanField('Sundays')
	start_date = DateField('Select start date')
	end_date = DateField('Select end date')
	submit = SubmitField('Update')
	def validate(self):
		return True
		rv = FlaskForm.validate(self)
		if not rv:
			return False
		start_date = self.start_date.data
		end_date = self.end_date.data
		today_date = date.today()
		if start_date > end_date :
			self.start_date.errors.append('Invalid start date ')
			return False
		if start_date <today_date:
			self.start_date.errors.append('Invalid start date')
			return False 
		if start_date <today_date:
			self.end_date.errors.append('Invalid end date')
			return False 
		return True


