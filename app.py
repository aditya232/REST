from flask import Flask,request,render_template,redirect,request,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import MyForm
from utils import process_form
from models import db,Update
from datetime import timedelta, date,datetime
import json

app = Flask(__name__)
app.config.from_object(Config)
with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/',methods=['GET', 'POST'])
def hello_world():
	return "hello"

@app.route('/success',methods=['GET'])
def success():
	return "Update successfull"

@app.route('/detail',methods=['GET'])
def get_record():
	price=availability=None
	query_date = request.args.get('start')
	query_room_type =(request.args.get('type')=='single')
	try:
		query_date = datetime.strptime(request.args.get('start'),'%Y-%m-%d').date()
		update = Update.query.filter_by(date=query_date).filter_by(room_type = query_room_type).first()
		if update:
			price = update.price
			availability =update.availability
		return jsonify(price =price,availability = availability)
	except:
		abort(404)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
	form = MyForm()
	if form.validate_on_submit(): 
		filtered_dates = process_form(form)
		for filtered_date in filtered_dates:
			update = Update.query.filter_by(date=filtered_date).filter_by(room_type=(form.room_type.data == 'Single Room')).first()
			if update:
				update.price = form.price.data
			else:	
				update = Update(form.price.data,form.availability.data,filtered_date,form.room_type.data == 'Single Room')
				db.session.add(update)
		db.session.commit()
		return redirect('/success') 
	return render_template('login.html', title='Sign In',form=form)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')