import json
import urllib.request
import urllib.parse

apiEndPoint = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter location:")
params = {
    "key": 42,
    "address": address
}
url = apiEndPoint + urllib.parse.urlencode(params)
print("Retrieving", url)
responseData = urllib.request.urlopen(url).read()
print("Retrieved", len(responseData))
placeId = json.loads(responseData)["results"][0]["place_id"]
print("Place id", placeId)
