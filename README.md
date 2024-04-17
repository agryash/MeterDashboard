# Meter Data API

This is a Flask application that provides a RESTful API for displaying meter data stored in a SQLite database.

## Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/agryash/MeterDashboard.git
    ```
2. Navigate to the project directory:
    ```
    cd MeterDashboard
    ```      
3. Create a virtual environment:
    ```
    virtualenv env
    ```
4. Activate the virtual environment:

- For macOS and Linux:
  ```
  source venv/bin/activate
  ```
- For Windows:
  ```
  venv\Scripts\activate
  ```
5. Install the required dependencies: 
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```
    python3 run.py
    ```

2. Access the application in your web browser at `http://127.0.0.1:5000`.

## Endpoints

- `/meters/`: Displays a list of unique meters in the database. Each meter is a clickable link that points to its associated data endpoint.

- `/meters/<meter_id>/`: Displays a list of all the datapoint entries for the specified meter ID, sorted by timestamp, in JSON format.