from flask import Blueprint, jsonify, render_template
from app.models import Meter, MeterData
from app import db

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    endpoints = [
        {'endpoint': '/meters/', 'description': 'Retrieve all meters and render them in HTML.'},
        {'endpoint': '/meters/<meter_id>/', 'description': 'Retrieve meter data for a specific meter ID and return it as JSON.'}
    ]
    return render_template('index.html', endpoints=endpoints)

@bp.route('/meters/')
def get_meters():
    """Retrieve all meters and render them in HTML."""
    meters = Meter.query.all()
    return render_template('meters.html', meters=meters)

@bp.route('/meters/<int:meter_id>/')
def get_meter_data(meter_id):
    """Retrieve meter data for a specific meter ID and return it as JSON."""
    meter = Meter.query.get_or_404(meter_id)
    meter_data = MeterData.query.filter_by(meter_id=meter_id).order_by(MeterData.timestamp.desc()).all()
    data_list = [{'id': data.id, 'timestamp': data.timestamp.isoformat(), 'value': data.value} for data in meter_data]
    response_data = {
        'meter_label': meter.label,
        'data': data_list
    }
    return jsonify(response_data)