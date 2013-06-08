import simplejson as json

edu =  json.loads(file("pueblos.json").read())

def f(x,y):
	return int(x["properties"]["COUNTY"])-int(y["properties"]["COUNTY"])

x = sorted(edu["pueblos"]["features"], f) 
y =  json.dumps({"pueblos": {"type": "FeatureCollection", "features":x }})

file("pueblos2.json", 'w').write(y)


