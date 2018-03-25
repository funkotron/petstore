# Petstore Solution

### Set up a virtual env
* `virtualenv -p python3 venv`
* `. ./virtualenv/bin/activate`

### Run tests
* `nosetests`

### Run the app
* `export FLASK_APP=app.py`
* `python3 -m flask run`

### For #4 (BONUS POINTS) Implement #3 as a progressively-enhanced in-page search feature

I would use an AJAX call triggered by an onkeyup method on the search form to POST to a new endpoint which returns a JSON list of the results of the `get_nearest` function (the nearest POSTCODES) and then filter only the matching shops to be shown on the client side.
