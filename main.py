from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

#connect html page
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": 23}

if __name__ == "__main_-":
    app.run(debug=True)