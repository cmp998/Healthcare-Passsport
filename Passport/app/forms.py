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
    doc_name = StringField('Doc_Name')
    doc_address = StringField('Doc_Address')
    med_id = StringField('MedID')
    purpose = StringField('POV')
    patient_info = StringField('PatientInfo')
    submit = SubmitField('Create')
