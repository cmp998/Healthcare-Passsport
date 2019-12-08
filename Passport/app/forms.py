from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    patient_id = StringField('Patient ID', validators=[DataRequired()])
    doctor_id = StringField('Doctor ID')
    medication_id = StringField('Medication ID')
    report_id = StringField('Report ID')
    submit = SubmitField('Search')

class NewPatientForm(FlaskForm):
    ssn = StringField('SSN*', validators=[DataRequired()])
    full_name = StringField('FullName*', validators=[DataRequired()])
    dob = StringField('DOB*', validators=[DataRequired()])
    phone = StringField('Phone*', validators=[DataRequired()])
    gender = StringField('Gender*', validators=[DataRequired()])
    submit = SubmitField('Create')


class NewReportForm(FlaskForm):
    report_id = StringField('ReportID*', validators=[DataRequired()])
    ssn = StringField('SSN*', validators=[DataRequired()])
    doc_id = StringField('DocID*', validators=[DataRequired()])
    med_id = StringField('MedID')
    purpose = StringField('Purpose of Visit')
    patient_info = StringField('PatientInfo')
    doc_name = StringField('Doc_Name')
    doc_address = StringField('Doc_Address')
    doc_department = StringField('Doc_Department')
    hospital_name = StringField("Hospital_Name")
    submit = SubmitField('Create')

class EditReport(FlaskForm):
    report_id = StringField('ReportID*', validators=[DataRequired()])
    ssn = StringField('SSN*', validators=[DataRequired()])
    doc_id = StringField('DocID*', validators=[DataRequired()])
    med_id = StringField('MedID')
    purpose = StringField('Purpose of Visit')
    patient_info = StringField('PatientInfo')
    submit = SubmitField('Edit')

class EditDoctor(FlaskForm):
    doc_id = StringField('DocID*', validators=[DataRequired()])
    doc_name = StringField('Doc_Name')
    address = StringField('Doc_Address')
    department = StringField('Doc_Department')
    hospital_name = StringField("Hospital_Name")
    submit = SubmitField('Edit')

class EditMed(FlaskForm):
    report_id = StringField('ReportID*')
    med_id = StringField('MedID', validators=[DataRequired()])
    submit = SubmitField('Edit')
