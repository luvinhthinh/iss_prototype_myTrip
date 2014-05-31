#import httplib, urllib, urllib2

#params = urllib.urlencode({'origin': 'Singapore Zoo', 'destination': 'Underwater World', 'sensor': 'false', 'key':'AIzaSyBn3GNyb8I5bUVSP7DdcEN1L_pnLQ6Hk5s'})
#print params
#params2 = ""
#print params2

#headers = {"Content-type": "application/json", "Accept":"*/*"}
#conn = httplib.HTTPSConnection('maps.googleapis.com')
#conn.connect()
#conn.request('POST', '/maps/api/directions/json', 'origin=Singapore+Zoo,Singapore&destination=Underwater+World,Singapore&sensor=false&key=AIzaSyBn3GNyb8I5bUVSP7DdcEN1L_pnLQ6Hk5s', {"Content-type": "application/json"})
#conn.request('POST', '/maps/api/directions/json', params2, headers)

#response = conn.getresponse()
#print response.status, response.reason, response.read()

import urllib2, json
req = urllib2.Request('https://maps.googleapis.com/maps/api/directions/json?origin=Singapore+Zoo,Singapore&destination=Underwater+World,Singapore&sensor=false&key=AIzaSyBn3GNyb8I5bUVSP7DdcEN1L_pnLQ6Hk5s', "")
response = urllib2.urlopen(req)
result_json = response.read()
print result_json

j = json.loads(result_json)
distance = j['routes'][0]['legs'][0]['distance']['value']
print distance
