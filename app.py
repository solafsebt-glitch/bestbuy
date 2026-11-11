from flask import Flask

app = Flask(__name__)

# Route 1: The Basics
@app.route("/")
def home():
    return "Hello, world!"

# Route 2: Getting Fancy with HTML
@app.route("/greet")
def greet():
    return "<h1>This is HTML!</h1>"

# Route 3: Personalized Greetings (with extra styling & emojis)
@app.route("/greet/<name>")
def greet_name(name):
    return f"""
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1 style="color: #4A90E2; font-size: 2.5rem;">
            Hello, {name}! 👋✨
        </h1>
        <p style="color: #777; font-size: 1.2rem;">
            Welcome to your personalized Flask page! 🚀
        </p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)