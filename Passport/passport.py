from app import app, db
from app.models import Patient,Doctor,Report,Hospital,Medication,Department

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Patient': Patient, 'Doctor': Doctor, 'Report': Report, 'Hospital': Hospital, 'Medication': Medication, 'Department': Department}