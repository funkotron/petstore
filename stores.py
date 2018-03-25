import json
import requests

class MissingPostCodeException(Exception):
	pass

def get_lat_long(postcode):
	print("Searching for ", postcode)
	r = requests.get("http://api.postcodes.io/postcodes/" + postcode.replace(" ", ""))
	j = r.json()
	if j['status'] == 404:
		raise MissingPostCodeException
	assert j["status"] == 200, j["error"]
	return j["result"]["latitude"], j["result"]["longitude"]


def get_nearest(postcode):
	# Get outcode from postcode (in case they enter a full postcode)
	r = requests.get("http://api.postcodes.io/postcodes?q=%s"%(postcode))
	if not 'result' in r.json():
		raise Exception("Incorrect Postcode Entered")
	outcode = r.json()["result"][0]["outcode"]
	print("Searching for outcode", outcode)
	r = requests.get("http://api.postcodes.io/outcodes/%s/nearest"%(outcode))
	if 'result' not in r.json():
		return []
	outcodes_nearby = [outcode] + [x['outcode'] for x in r.json()['result']]
	# Filter matching postcodes
	matching_stores = [store for store in stores if store['outcode'] in outcodes_nearby]
	# Sort by nearest
	sorted_stores = sorted(matching_stores, key=lambda a: outcodes_nearby.index(a['outcode']))
	return sorted_stores


with open("stores.json") as stores_file:
	json_stores = json.load(stores_file)
	sorted_stores = sorted(json_stores, key=lambda x: x['name'])
	stores = []
	for store in sorted_stores:
		try:
			store["lat"], store["long"] = get_lat_long(store['postcode'])
			store["name"] = store["name"].replace("_", " ")
			store["outcode"] = store["postcode"].split(' ')[0]
			stores.append(store)
		except MissingPostCodeException:
			# Skip stores that have no matching postcode
			continue
