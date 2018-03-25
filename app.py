from flask import Flask, render_template, request
from stores import stores, get_nearest

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        closest_stores = get_nearest(request.form['postcode'])
        return render_template("index.html", stores=closest_stores)
    return render_template("index.html", stores=stores)

