from flask import request, redirect,url_for, render_template
from application import app, db
from application.models import *
from application.forms import *

@app.route('/') #go to the home page
def index():
    return render_template('layout.html')

#CRUD for users /////////////////////////////////////////////////////////////////////////////////////////

# Creates new users 

@app.route('/add_user', methods=['GET','POST'])
def add_new_user():
    form = usersForm()
    if form.validate_on_submit():
        forename = form.forename.data
        surname = form.surname.data
        new_user = user(forename=forename, surname=surname)
        db.session.add(new_user)
        db.session.commit()
        return redirect (url_for('all_users', print="User Added")) #if completed redirect to view all users page
    else:
        return render_template('user_form.html', form=form) #if not completed redirect to the user-form

@app.route('/view_user')
def all_users():
    view_all_users = user.query.all()
    return render_template('view_user.html', entity='Users',Users=view_all_users)

@app.route('/update_user/<int:id>', methods = ['GET', 'POST'])
def update_users(id):
    user_update = user.query.get(id)
    form = usersForm()
    if form.validate_on_submit():
        user_update.forename = form.forename.data
        user_update.surname = form.surname.data
        db.session.commit()
        return redirect (url_for('all_users', print="User Updated"))
    form.forename.data = user_update.forename
    form.surname.data = user_update.surname
    return render_template('user_form.html', form=form)

@app.route('/delete_user/<int:id>')
def delete_users(id):
    user_delete = user.query.get(id)
    db.session.delete(user_delete)
    db.session.commit()
    return redirect (url_for('all_users', print="User Deleted"))

#CRUD user_era schema ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Creating the function to calculate the era the user was born 

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

    return render_template('view_barbie_era.html', message=message)

# Add entry to barbie_era database

@app.route('/create_barbie_era', methods=['GET','POST'])
def add_barbie_era():
    form = barbie_eraForm()
    Users = user.query.all()
    form.user.choices = [(user.user_id, f"{user.forename} {user.surname}") for user in Users]
    if form.validate_on_submit():
        barbie_year = form.barbie_year.data
        birth_year= form.birth_year.data
        user_id = form.user.data
        new_barbie_era = barbie_era( barbie_year=barbie_year, birth_year=birth_year)
        db.session.add(new_barbie_era)
        db.session.commit()
        return redirect (url_for('get_user_era',year=int(birth_year.strip("'s"))))
    else:
        return render_template('barbie_era_form.html', form=form )

@app.route('/view_barbie_era')
def view_barbie_era():
    barbie_era_= barbie_era.query.all()
    return render_template('view_barbie_era.html', entity ='barbie',barbie=barbie_era_)
     
#update user_era //////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/update_barbie_era/<int:id>',  methods=['GET','POST'])
def update_barbie_era(id):
    barbie_era_to_update=barbie_era.query.get(id)
    form = barbie_eraForm()
    Users = user.query.all()
    form.user.choices = [(user.user_id, f"{user.forename} {user.surname}") for user in Users]
    if form.validate_on_submit():
        barbie_era_to_update.barbie_year=form.barbie_year.data
        barbie_era_to_update.birth_year= form.birth_year.data
        db.session.commit()
        return redirect (url_for('get_user_era',year=int(barbie_era_to_update.barbie_year.strip("'s"))))
    return render_template('barbie_era_form.html', form=form )

@app.route('/delete_barbie_era/<int:id>')
def delete_barbie_era(id):
    barbie_era_delete = barbie_era.query.get(id)
    db.session.delete(barbie_era_delete)
    db.session.commit()
    return redirect (url_for('view_barbie_era', print="User Era Deleted"))