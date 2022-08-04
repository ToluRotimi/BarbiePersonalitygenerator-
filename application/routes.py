from flask import request, redirect,url_for, render_template
from application import app, db
from application.models import *
from datetime import date
from application.forms import *

@app.route('/') #go to the home page
def index():
    return render_template('layout.html')

#CRUD for users and also get the dob_year to calculate the era/////////////////////////////////////////////////////////////////////////////////////////

@app.route('/view_user')
def all_users():
    view_all_users = user.query.all()
    return render_template('view_user.html',entity='Users',Users=view_all_users)

# adds new users using form and get the dob_year to calculate the era
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


@app.route('/update_user/<int:id>', methods = ['GET', 'POST'])
def update_users(id):
    user_update = user.query.get(id)
    form = usersForm()
    if form.validate_on_submit():
        forename = form.forename.data
        surname = form.surname.data
        user_update.forename =forename
        user_update.surname = surname 
        db.session.commit()
        return redirect (url_for('all_users', print="User Updated"))
    return render_template('user_form.html', form=form)

@app.route('/delete_user/<int:id>')
def delete_users(id):
    user_delete = user.query.get(id)
    db.session.delete(user_delete)
    db.session.commit()
    return redirect (url_for('all_users', print="User Deleted"))

#CRUD user_era schema ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/view_user_era')
def view_user_era():
    user_era_ = user_era.query.all()
    return render_template('get_user_era.html', entity ='Era',Era=user_era_)

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
@app.route('/create_user_era', methods=['GET','POST'])
def add_user_era():
    form = user_eraForm()
    Users = user.query.all()
    form.user_era.choices = [(user.user_id, f"{user.forename} {user.surname}") for user in Users]
    if form.validate_on_submit():
        user_era_decade = form.user_era_decade.data
        user_id = form.user_era
        new_user_era = user_era(user_era_decade=user_era_decade, user_era=user_id) 
        db.session.add(new_user_era)
        db.session.commit()
        return redirect (url_for('get_user_era', print = 'Added ',year=int(user_era_decade.strip("'s"))))
    else:
        return render_template('user_era_form.html', form=form )
     
#update user_era //////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/update_user_era/<int:id>', methods = ['GET', 'POST'])
def update_user_era(id):
    user_era_update = user_era.query.get(id)
    form = user_eraForm()
    Users = user.query.all()
    form.user_era.choices = [(user.user_id, f"{user.forename}{user.surname}" for user in Users)]
    if form.validate_on_submit():
        user_era_decade = form.user_era_decade.data
        user_era= form.user_era.data
        db.session.commit()
        return redirect (url_for('view_user_era', print='User Era Updated'))
    form.user_era_decade.data = user_era_decade
    form.user_era.data = user_era
    return render_template('user_era_form.html', form=form)

@app.route('/delete_user_era/<int:id>')
def delete_user_era(id):
    user_era_delete = user.query.get(id)
    db.session.delete(user_era_delete)
    db.session.commit()
    return redirect (url_for('view_user_era', print="User Era Deleted"))