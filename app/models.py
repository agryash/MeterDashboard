from datetime import datetime
from app import db

class Meter(db.Model):
    """Meter model representing a unique meter."""
    __tablename__ = 'meters'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)
    meter_data = db.relationship('MeterData', backref='meter', lazy=True)

class MeterData(db.Model):
    """MeterData model representing data points for a meter."""
    __tablename__ = 'meter_data'
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meters.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    value = db.Column(db.Integer, nullable=False)