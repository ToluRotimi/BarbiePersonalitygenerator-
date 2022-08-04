from flask import request, redirect,url_for, render_template
from application import app, db
from application.models import user,barbie_era,user_era
from datetime import date
from application.forms import *

@app.route('/') #go to the home page
@app.route('/Home')
def index():
    return render_template('layout.html')

#CRUD for users and also get the dob_year to calculate the era/////////////////////////////////////////////////////////////////////////////////////////

@app.route('/view_user')
def all_users():
    view_all_users = user.query.all()
    return render_template('view_user.html',Users=view_all_users)

# adds new users using form and get the dob_year to calculate the era
@app.route('/add_user', methods=['GET','POST'])
def add_new_user():
    form = usersForm()
    if form.validate_on_submit():
        forename = form.forename.data
        surname = form.surname.data
        dob = form.dob.data
        new_user = user(forename=forename, surname=surname, dob=dob)
        db.session.add(new_user)
        db.session.commit()
        return redirect (url_for('all_users', print="User Added")) #if completed redirect to view all users page
    else:
        return render_template('user_form.html', form=form) #if not completed redirect to the user-form


@app.route('/update_user/<int:id>', methods = ['GET', 'POST'])
def update_users(id):
    user_update = user.query.get(id)
    form = usersForm()
    if form.validate_on_submit():
        forename = form.forename.data
        surname = form.surname.data
        dob = form.dob.data
        user_update.forename =forename
        user_update.surname = surname 
        user_update.dob = dob
        db.session.commit()
        return redirect (url_for('all_users', print="User Updated"))
    return render_template('user_form.html', form=form)

@app.route('/delete_user/<int:id>')
def delete_users(id):
    user_delete = user.query.get(id)
    db.session.delete(user_delete)
    db.session.commit()
    return redirect (url_for('all_users', print="User Deleted"))

## CRUD for barbie_era ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/view_barbie_era')
def view_all_era():
    era = barbie_era.query.all()
    return render_template('view_era.html',barbie_era=era)
    

@app.route('/new_barbie_era', methods=['GET', 'POST'])
def new_barbie_era():
    form = barbie_eraForm()
    if form.validate_on_submit():
        era_decade = form.era_decade.data
        new_era = barbie_era(era_decade=era_decade)
        db.session.add(new_era)
        db.session.commit()
        return redirect (url_for('view_all_era', print = 'Barbie Era Added'))
    else:
        return render_template('era_form.html', form=form) 


@app.route('/update_era/<int:id>', methods = ['GET', 'POST'])
def update_era(id):
    barbie_era_update = barbie_era.query.get(id)
    form = barbie_eraForm()
    if form.validate_on_submit():
        era_decade = form.era_decade.data
        barbie_era_update.era_decade = era_decade
        db.session.commit()
        return redirect (url_for('view_all_era', print='Barbie Era Updated'))
    return render_template('era_form.html', form=form)

@app.route('/delete_era/<int:id>')
def delete_era(id):
    era_delete = barbie_era.query.get(id)
    db.session.delete(era_delete)
    db.session.commit()
    return redirect (url_for('view_all_era', print="Barbie Era Deleted"))
    
#CRUD user_era schema ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/view_user_era')
def view_user_era():
    user_era_ = user_era.query.all()
    return render_template('get_user_era.html', user_era_=user_era_)

# creating the function to calculate the era the user was born 

@app.route("/get-user-era/<int:year>")
def get_user_era(year):
    if year >= 2000: 
         message = "You were born between the 00's barbie era"
    elif year >= 1990:
        message = "You were born between the 90's barbie era"
    elif year >= 1980:
        message = "You were born between the 80's barbie era"
    elif year >= 1970:
        message = "You were born between the 70's barbie era"
    elif year >= 1960:
        message =  "You were born between the 60's barbie era"
    elif year >= 1950:
        message =  "You were born between the 50's barbie era"
    else:
       message =  "You were not born in a barbie era"

    return render_template('get_user_era.html', message=message, user_era=[])
#add entry to user_era databse
@app.route('/new_user_era', methods=['GET','POST'])
def add_user_era():
    form = user_eraForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        era_id = form.era_id.data
        user_era_decade = form.user_era_decade.data
        new_user_era = user_era(user_id=user_id, era_id=era_id, user_era_decade=user_era_decade) 
        db.session.add(new_user_era)
        db.session.commit()
        return redirect (url_for('get_user_era', print = 'Added ',year=int(user_era_decade.strip("'s"))))
    else:
        return render_template('user_era_form.html', form=form )
     
#update user_era //////////////////////////////////////////////////////////////

@app.route('/update_user_era/<int:id>', methods = ['GET', 'POST'])
def update_user_era(id):
    user_era_update = user_era.query.get(id)
    form = user_eraForm()
    if form.validate_on_submit():
        user_era_decade = form.user_era_decade.data
        user_era_update.user_era_decade = user_era_decade
        db.session.commit()
        return redirect (url_for('get_user_era', print='User Era Updated'))
    return render_template('user_era_form.html', form=form)