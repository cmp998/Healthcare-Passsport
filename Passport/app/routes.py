from flask import render_template
from app import app, db
from app.forms import SearchForm, NewPatientForm, NewReportForm
from flask import render_template, flash, redirect
from app.models import Report, Doctor, Patient, Medication, Hospital, Department


@app.route('/')
 
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        if form.report_id.data:
            #Only a specfic report
            return render_template('results.html', 
                    reports = Report.query.get(form.report_id.data), 
                    form=form, 
                    type='report',
                    patient=Patient.query.get(form.patient_id.data))
        elif form.doctor_id.data:
            #Only a specific doctor
            return render_template('results.html', 
                    doctors=Doctor.query.get(form.doctor_id.data), 
                    form=form, 
                    type='doctor',
                    patient=Patient.query.get(form.patient_id.data))
        elif form.medication_id.data:
            #Only a specific medication
            return render_template('results.html', 
                    medications=Medication.query.get(form.medication_id.data), 
                    form=form, 
                    type='medication',
                    patient=Patient.query.get(form.patient_id.data))
        else:
            #All info about patient
            return render_template('results.html',
                    form=form,
                    type='generic',
                    patient=Patient.query.get(form.patient_id.data),
                    medications=Medication.query.all(),
                    doctors=Doctor.query.all(),
                    reports = Report.query.all())

    return render_template('search.html',title='Search',form=form)

@app.route('/newreport', methods=['GET','POST'])
def newreport():
    form = NewReportForm()
    if form.validate_on_submit():
        #Add the report to our database
        r = Report(report_id = form.report_id.data,
            ssn = form.ssn.data,
            doc_id = form.doc_id.data,
            med_id = form.med_id.data,
            purpose = form.purpose.data,
            patient_info = form.patient_info.data,)
        db.session.add(r)
        db.session.commit()

        print("Added: ",form.report_id.data,form.ssn.data,form.doc_id.data,form.med_id.data,form.purpose.data,form.patient_info.data,)
        #Redirect instead of render_template
        return render_template('index.html', create = "Report", form = form)
    return render_template('newreport.html',title='NewReport', form = form)

@app.route('/newpatient', methods=['GET','POST'])
def newPatient():
    form = NewPatientForm()
    if form.validate_on_submit():
        p = Patient(ssn=form.ssn.data, 
            full_name = form.full_name.data,
            dob = form.dob.data,
            phone = form.phone.data,
            gender = form.gender.data)
        db.session.add(p)
        db.session.commit()
        print("Added: ",form.ssn.data, form.full_name.data,form.dob.data,form.phone.data,form.gender.data)
        #Redirect instead of render_template?
        return render_template('index.html', create = "Patient", form = form)
    return render_template('newpatient.html',title='NewPatient', form = form)

@app.route('/results')
def results():
    results = [
        {'SSN': "123 45 6789",'DocID': 'Doc1'},
        {'SSN': "999 99 9999",'DocID': 'Doc2'}
    ] 
    return render_template('results.html',title="Results",results=results)