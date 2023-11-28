from flask import Flask, render_template

app = Flask(__name__, template_folder='practice')

#connect html page
@app.route("/home")
def home():
    return render_template("practice.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)