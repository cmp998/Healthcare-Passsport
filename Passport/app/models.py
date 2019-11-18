from app import db

class Patient(db.Model):
    __tablename__ = 'patient'
    ssn = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String (10),nullable=False)
    dob = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(10),nullable=False)
    full_name = db.Column(db.String(50),nullable=False)
    #reports = db.relationship('Reports', backref = 'patient')

    def __repr__(self):
        return '<Patient {}>'.format(self.full_name)

class Doctor(db.Model):
    __tablename__ = 'doctor'
    doc_id = db.Column(db.String, primary_key=True)
    doc_name = db.Column(db.String(50),nullable=False)
    address = db.Column(db.String(50), db.ForeignKey('hospital.address'),nullable=False)

    def __repr__(self):
        return '<Doctor {}>'.format(self.doc_id)

class Hospital(db.Model):
    __tablename__ = 'hospital'
    address = db.Column(db.String, primary_key=True)
    hospital_name = db.Column(db.String(20))

    def __repr__(self):
        return '<Hospital {}>'.format(self.address)

class Report(db.Model):
    __tablename__ = 'report'
    report_id = db.Column(db.String, primary_key=True)
    ssn = db.Column(db.String, db.ForeignKey('patient.ssn'))
    doc_id = db.Column(db.String, db.ForeignKey('doctor.doc_id'))
    med_id = db.Column(db.String, db.ForeignKey('medication.med_id'))
    purpose = db.Column(db.String(200))
    patient_info = db.Column(db.String(200))

    def __repr__(self):
        return '<Report {}>'.format(self.report_id)
        
class Medication(db.Model):
    __tablename__ = 'medication'
    report_id = db.Column(db.String, db.ForeignKey('report.report_id'))
    med_id = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return '<Medication {}>'.format(self.med_id) 

class Department(db.Model):
    __tablename__ = 'department'
    address = db.Column(db.String(50), db.ForeignKey('hospital.address'), primary_key=True)
    department_name = db.Column(db.String(20))

    def __repr__(self):
        return '<Department {}>'.format(self.address + self.department_name)
