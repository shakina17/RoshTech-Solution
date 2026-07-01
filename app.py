from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Create Database Table
def create_table():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()

@app.route("/")
def home():
    return "RoshTech Backend Running Successfully!"

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

if __name__ == "__main__":
    app.run(debug=True)