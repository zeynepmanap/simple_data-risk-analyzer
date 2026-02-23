from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///risk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -----------------
# DATABASE MODEL
# -----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# -----------------
# CREATE DB
# -----------------
with app.app_context():
    db.create_all()

# -----------------
# HOME
# -----------------
@app.route("/")
def home():
    return redirect(url_for("login"))

# -----------------
# REGISTER
# -----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

# -----------------
# LOGIN
# -----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))
        else:
            return "Invalid email or password"

    return render_template("login.html")

# -----------------
# LOGOUT
# -----------------
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

# -----------------
# DASHBOARD
# -----------------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if not session.get("user_id"):
        return redirect(url_for("login"))

    risk_score = None
    risk_level = None
    recommendation = None

    if request.method == "POST":
        # SAFE FORM GET (NO MORE KEY ERROR)
        password_strength = int(request.form.get("password_strength", 3))
        two_factor = int(request.form.get("two_factor", 0))
        open_ports = int(request.form.get("open_ports", 0))
        software_updated = int(request.form.get("software_updated", 0))
        encryption = int(request.form.get("encryption", 0))

        score = 0

        score += (5 - password_strength)
        score += (0 if two_factor == 1 else 5)
        score += open_ports
        score += (0 if software_updated == 1 else 5)
        score += (0 if encryption == 1 else 5)

        if score <= 5:
            risk_level = "LOW"
            recommendation = "System is relatively secure."
        elif score <= 12:
            risk_level = "MEDIUM"
            recommendation = "Security improvements recommended."
        else:
            risk_level = "HIGH"
            recommendation = "Immediate action required."

        risk_score = score

    return render_template(
        "dashboard.html",
        risk_score=risk_score,
        risk_level=risk_level,
        recommendation=recommendation
    )

# -----------------
# RUN
# -----------------
if __name__ == "__main__":
    app.run(debug=True)
