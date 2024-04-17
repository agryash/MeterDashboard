from app import create_app, db
from app.models import Meter, MeterData
from datetime import datetime

app = create_app()

def add_sample_data():
    """Create sample meters"""
    meter1 = Meter(label='Meter A')
    meter2 = Meter(label='Meter B')
    db.session.add_all([meter1, meter2])
    db.session.commit()

    # Create sample meter data
    meter_data1 = [
        MeterData(meter_id=meter1.id, timestamp=datetime(2024, 5, 1, 10, 0), value=100),
        MeterData(meter_id=meter1.id, timestamp=datetime(2024, 5, 1, 11, 0), value=200),
        MeterData(meter_id=meter1.id, timestamp=datetime(2024, 5, 1, 12, 0), value=150)
    ]
    meter_data2 = [
        MeterData(meter_id=meter2.id, timestamp=datetime(2024, 5, 1, 10, 30), value=50),
        MeterData(meter_id=meter2.id, timestamp=datetime(2024, 5, 1, 11, 30), value=75),
        MeterData(meter_id=meter2.id, timestamp=datetime(2024, 5, 1, 12, 30), value=80)
    ]
    db.session.add_all(meter_data1 + meter_data2)
    db.session.commit()

@app.shell_context_processor
def make_shell_context():
    """Configure the shell context for Flask CLI."""
    return {'db': db, 'Meter': Meter, 'MeterData': MeterData}

if __name__ == '__main__':
    """Entry point for the program."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_sample_data()
    app.run(debug=True)