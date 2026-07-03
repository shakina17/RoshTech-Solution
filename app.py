from flask import Flask, request, render_template, redirect, session
import sqlite3

app = Flask(__name__)

app.secret_key = "roshtech123"  

# Create Database Table
def create_table():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    # Contact Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        message TEXT
    )
    """)

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()

@app.route("/")
def home():

    if "username" not in session:
        return redirect("/login")

    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/admin-login")
def admin_login_page():

    if "admin" in session:
        return redirect("/admin")

    return render_template("admin-login.html")



@app.route("/logout")
def logout():

    session.pop("username", None)
    session.pop("admin", None)

    return redirect("/login")

@app.route("/web-development")
def web_development():
    return render_template("web-development.html")


@app.route("/mobile-app")
def mobile_app():
    return render_template("mobile-app.html")


@app.route("/cloud-solutions")
def cloud_solutions():
    return render_template("cloud-solutions.html")


@app.route("/it-consulting")
def it_consulting():
    return render_template("it-consulting.html")


@app.route("/uiux-design")
def uiux_design():
    return render_template("uiux-design.html")


@app.route("/cyber-security")
def cyber_security():
    return render_template("cyber-security.html")


@app.route("/software-maintenance")
def software_maintenance():
    return render_template("software-maintenance.html")

@app.route("/job-application")
def job_application():
    return render_template("job-application.html")

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts(name,email,phone,message) VALUES (?,?,?,?)",
        (name, email, phone, message)
    )

    conn.commit()
    conn.close()

    print("Data Saved Successfully!")

    return """
    
    
    
    <!DOCTYPE html>
    <html>
    <head>
        <title>Success</title>

        <style>

            body{
                font-family: Arial, sans-serif;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                background:#f4f7fc;
            }

            .box{
                background:white;
                padding:40px;
                border-radius:15px;
                text-align:center;
                box-shadow:0 5px 15px rgba(0,0,0,0.1);
            }

            h1{
                color:green;
            }

            a{
                display:inline-block;
                margin-top:20px;
                padding:10px 20px;
                background:#0A192F;
                color:white;
                text-decoration:none;
                border-radius:8px;
            }

        </style>

    </head>

    <body>

        <div class="box">

            <h1>✅ Thank You!</h1>

            <p>
                Your message has been submitted successfully.
            </p>

            <p>
                Our team will contact you soon.
            </p>

            <a href="javascript:history.back()">
                Back to Website
            </a>

        </div>

    </body>
    </html>
    """

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    if user:

        conn.close()

        return """
        <h1 style='color:red;text-align:center;margin-top:100px;'>
        Username Already Exists
        </h1>

        <div style='text-align:center;'>
            <a href="/register">
                Back To Register
            </a>
        </div>
        """

    cursor.execute(
        "INSERT INTO users(name,email,username,password) VALUES (?,?,?,?)",
        (name, email, username, password)
    )

    conn.commit()
    conn.close()

    return redirect("/login")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        session["username"] = username

        return redirect("/")

    else:

        return """
        <h1 style='color:red;text-align:center;margin-top:100px;'>

        Invalid Username or Password

        </h1>

        <div style='text-align:center;'>

        <a href="/login">

        Try Again

        </a>

        </div>
       """
@app.route("/admin-login", methods=["POST"])
def admin_login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":

        session["admin"] = username

        return redirect("/admin")

    else:

        return """
        <h1 style="text-align:center;color:red;margin-top:100px;">
        Invalid Admin Username or Password
        </h1>

        <div style="text-align:center;">
            <a href="/admin-login">Try Again</a>
        </div>
        """

@app.route("/admin")
def admin():

    if "admin" not in session:
        return redirect("/admin-login")

    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM contacts")
    total_messages = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "admin.html",
        contacts=contacts,
        total_users=total_users,
        total_messages=total_messages
    )

if __name__ == "__main__":
    app.run(debug=True)

