from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "supersecretkey" # Required for flash messages
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth_app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

# MANDATORY: Create database tables outside the main block for Render
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Backend Validation Requirements [cite: 19, 21-28]
        if not name or not email or not password:
            flash("All fields (Name, Email, Password) are mandatory.", "danger")
            return redirect(url_for('register'))

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "danger") [cite: 28]
            return redirect(url_for('register'))

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("Email already registered. Show proper error message.", "warning") [cite: 27, 30]
            return redirect(url_for('register'))

        # Save valid user
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!", "success")
        return redirect(url_for('home'))

    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)