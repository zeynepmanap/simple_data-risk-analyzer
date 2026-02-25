# Simple Data Risk Analyzer

A lightweight version of the main **Data Risk Analyzer** project, built with Flask.  
Designed for quick setup and testing of risk assessment features with minimal configuration.

---

## Features

- Flask-based web application  
- Basic risk calculation based on password strength, 2FA, open ports, software updates, and data encryption  
- Lightweight and easy to deploy  
- Simple dashboard showing risk trends and previous records  

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/zeynepmanap/simple_data-risk-analyzer.git
cd simple_data-risk-analyzer

Create a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies
pip install -r requirements.txt

Run the application
python app.py

Open your browser and go to http://127.0.0.1:5000

Usage
Register a new user or log in with existing credentials
Fill out the Risk Assessment form to calculate risk scores
View previous records and trends on the dashboard
Delete individual records or all records using the delete buttons

Project Structure
simple_data-risk-analyzer/
│
├─ app.py              # Main Flask app
├─ models.py           # Database models (if separated)
├─ templates/          # HTML templates (dashboard, login, register)
├─ static/             # CSS/JS files
├─ screenshots/        # Screenshots used in README
├─ requirements.txt    # Python dependencies
└─ README.md

Notes
This is a simplified version of the main Data Risk Analyzer project.
For the full-featured version, see Data Risk Analyzer
Designed for educational purposes and quick testing

License
MIT License
