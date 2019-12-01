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
            if Report.query.get(form.report_id.data):
                #Only a specfic report
                return render_template('results.html', patient = Patient.query.get(form.patient_id.data), form=form, 
                                        type='report', reports = Report.query.filter_by(ssn = form.patient_id.data))
            else:
                return render_template('search.html',title='Search',form=form, error="Invalid Report")

        elif form.doctor_id.data:
            if Doctor.query.get(form.doctor_id.data):
                #Only a specific doctor
                return render_template('results.html', patient=Patient.query.get(form.patient_id.data), form=form, 
                                        type='doctor', doctors=Doctor.query.get(form.doctor_id.data))
            else:
                return render_template('search.html',title='Search',form=form, error="Invalid Doctor")

        elif form.medication_id.data:
            if Medication.query.get(form.medication_id.data):
                #Only a specific medication
                return render_template('results.html', patient=Patient.query.get(form.patient_id.data), form=form, 
                                        type='medication', medications=Medication.query.get(form.medication_id.data))
            else:
                return render_template('search.html',title='Search',form=form, error="Invalid Medication")
        else:
            #All info about patient
            if Patient.query.get(form.patient_id.data):
                #Patient Specific Doctors and Meds
                patient = Patient.query.get(form.patient_id.data)
                reports = Report.query.filter_by(ssn = patient.ssn)
                meds_filtered = []
                docs_filters = []
                for r in reports:
                    for m in Medication.query.all():
                        if m.report_id == r.report_id:
                            meds_filtered.append(m)
                    for d in Doctor.query.all():
                        if d.doc_id == r.doc_id:
                            if d not in docs_filters:
                                docs_filters.append(d)

                return render_template('results.html', patient=patient, form=form,
                                        type='generic', 
                                        medications=meds_filtered, doctors=docs_filters, reports = reports)
            else: 
                return render_template('search.html',title='Search',form=form, error="Invalid Patient")

    return render_template('search.html',title='Search',form=form)

@app.route('/newreport', methods=['GET','POST'])
def newreport():
    form = NewReportForm()
    if form.validate_on_submit():
        #See if the medication is in db yet
        med_options = form.med_id.data.split(",")
        for med_id in med_options:
            if not Medication.query.get(med_id) and med_id:
                print("didn't see this med, adding")
                m = Medication(report_id = form.report_id.data, med_id = med_id)
                db.session.add(m)
                db.session.commit()
                print("added meds: ", Medication.query.get(med_id))

        #See if the doctor is in db yet
        if not Doctor.query.get(form.doc_id.data) and form.doc_name.data and form.doc_address.data:
            print("didn't see this doc, adding")
            d = Doctor(doc_id = form.doc_id.data, doc_name = form.doc_name.data, address = form.doc_address.data)
            db.session.add(d)
            db.session.commit()
            print("added doc: ", Doctor.query.get(form.doc_id.data))
        elif not Doctor.query.get(form.doc_id.data):
            return render_template('newreport.html',title='New Report',form=form, error="New Doctor Detected: Please Include All Info")

        #See if the hopsital exists
        if not Hospital.query.get(form.doc_address.data) and form.hospital_name.data and form.doc_address.data:
            print("didn't see this hospital, adding")
            h = Hospital(hospital_name = form.hospital_name.data, address = form.doc_address.data)
            db.session.add(h)
            db.session.commit()
            print("added hospital: ", Hospital.query.get(form.doc_address.data))
        elif not Hospital.query.get(form.hospital_name.data):
            return render_template('newreport.html',title='New Report', form=form, error="New Hospital Detected: Please Include All Info")

        #See if the department exists
        if not Department.query.get(form.doc_address.data) and form.doc_address.data and form.doc_department.data:
            print("didn't see this department, adding")
            d = Department(address = form.doc_address.data, department_name = form.doc_department.data)
            db.session.add(d)
            db.session.commit()
            print("added department: ", Department.query.get(form.doc_address.data))
        elif not Department.query.get(form.doc_address.data):
            return render_template('newreport.html',title='New Report', form=form, error="New Department Detected: Please Include All Info")


        #Add report to the db
        if Report.query.get(form.report_id.data):
            return render_template('newreport.html',title='New Report',form=form, error="Duplicated Report ID")
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
    if form.validate_on_submit() and  not Patient.query.get(form.ssn.data):
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
    elif Patient.query.get(form.ssn.data):
        print("NON UNIQUE PATIENT ERROR")
        return render_template('newpatient.html',title='NewPatient', form = form, error = "NON UNIQUE PATIENT ERROR")
    return render_template('newpatient.html',title='NewPatient', form = form)

@app.route('/clean_house')
def clean_house():
    print("List of patients before: ", Patient.query.all())
    for p in Patient.query.all():
        db.session.delete(p)
    for d in Doctor.query.all():
        db.session.delete(d)
    for m in Medication.query.all():
        db.session.delete(m)
    for r in Report.query.all():
        db.session.delete(r)
    for h in Hospital.query.all():
        db.session.delete(h)
    for d in Department.query.all():
        db.session.delete(d)
    db.session.commit()
    print("List of patients after: ", Patient.query.all())
    return redirect('/index')

@app.route('/delete_med/<string:med_id>')
def delete_med(med_id):
    for m in Medication.query.all():
        if m.med_id == med_id:
            print("Deleting ",med_id)
            db.session.delete(m)
    db.session.commit()
    return redirect('/search')

@app.route('/delete_doc/<string:doc_id>')
def delete_doc(doc_id):
    #Delete the actual doctor
    for d in Doctor.query.all():
        if d.doc_id == doc_id:
            print("Deleting doc",doc_id)
            db.session.delete(d)
    #Delete in reports from this doctor
    deleted_reports = []
    for r in Report.query.all():
        if r.doc_id == doc_id:
            deleted_reports.append(r.report_id)
            print("Deleting report",r.report_id)
            db.session.delete(r)
    #Remove meds if their report was removed.
    for m in Medication.query.all():
        if m.report_id in deleted_reports:
            print("Deleting med",m.med_id)
            db.session.delete(m)

    db.session.commit()
    return redirect('/search')

@app.route('/delete_report/<string:report_id>')
def delete_report(report_id):
    #Delete the actual report
    for r in Report.query.all():
        if r.report_id == report_id:
            print("Deleting report",report_id)
            db.session.delete(r)

    #Delete meds from this report
    for m in Medication.query.filter_by(report_id = report_id):
        db.session.delete(m)
        print("Deleting med",m)
            
    #Remove meds if their report was removed.
    for m in Medication.query.all():
        if m.report_id in deleted_reports:
            print("Deleting med",m.med_id)
            db.session.delete(m)

    db.session.commit()
    return redirect('/search')