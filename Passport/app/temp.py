from app import db

class Patient(db.Model):
    SSN = db.Column(db.Integer, primary_key=True)
    Gender = db.Column(db.String(10),nullable=False)
    DOB = db.Column(db.String(120),nullable=False)
    Phone = db.Column(db.String(10),nullable=False)
    FullName = db.Column(db.String(50),nullable=False)
    Reports = db.relationship('Reports', lazy='dynamic')

    def __repr__(self):
        return '<Patient {}>'.format(self.SSN)

class Doctor(db.Model):
    DocID = db.Column(db.Integer, primary_key=True)
    DocName = db.Column(db.String(50),nullable=False)
    Address = db.Column(db.String(50), db.ForeignKey('hospital.Address'),nullable=False)

    def __repr__(self):
        return '<Doctor {}>'.format(self.DocID)

class Hospital(db.Model):
    Address = db.Column(db.String, primary_key=True)
    Hospital_Name = db.Column(db.String(20))

    def __repr__(self):
        return '<Hospital {}>'.format(self.Address)

class Report(db.Model):
    ReportID = db.Column(db.Integer, primary_key=True)
    SSN = db.Column(db.Integer, db.ForeignKey('patient.SSN'))
    DocID = db.Column(db.Integer, db.ForeignKey('doctor.DocID'))
    MedID = db.Column(db.Integer, db.ForeignKey('medication.MedID'))
    POV = db.Column(db.String(200))
    PatientInfo = db.Column(db.String(200))

    def __repr__(self):
        return '<Report {}>'.format(self.ReportID)
        
class Medication(db.Model):
    ReportID = db.Column(db.Integer, db.ForeignKey('report.ReportID'))
    MedID = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Medication {}>'.format(self.MedID) 

class Department(db.Model):
    Address = db.Column(db.String(50), db.ForeignKey('hospital.Address'), primary_key=True)
    DepartmentName = db.Column(db.String(20))

    def __repr__(self):
        return '<Department {}>'.format(self.Address + self.DepartmentName)
           