from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template("login.html")

@views.route('/home')
@login_required
def hhome():
    return render_template("home.html")


@views.route('/patient_home')

def patient_home():
    return render_template("patient_home.html")

@views.route('/doc_home')

def doc_home():
    return render_template("doc_home.html")

@views.route('/ent_dpmt')
def ent_dpmt():
    return render_template("ent_dpmt.html")

@views.route('/physician_dpmt')
def physician_dpmt():
    return render_template("physician_dpmt.html")

@views.route('/pediatrician_dpmt')
def pediatrician_dpmt():
    return render_template("pediatrician_dpmt.html")

@views.route('/dentist_dpmt')
def dentist_dpmt():
    return render_template("dentist_dpmt.html")

@views.route('/ent_appointment')
def ent_appointment():
    return render_template("ent_appointment.html")

@views.route('/physician_appointment')
def physician_appointment():
    return render_template("physician_appointment.html")

@views.route('/pediatrician_appointment')
def pediatrician_appointment():
    return render_template("pediatrician_appointment.html")

@views.route('/dentist_appointment')
def dentist_appointment():
    return render_template("dentist_appointment.html")

@views.route('/appointment_status')
def appointment_status():
    return render_template("appointment_status.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

