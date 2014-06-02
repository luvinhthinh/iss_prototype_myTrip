country = 'Singapore'
places = ['Singapore Zoo', 'Underwater World', 'Night Safari', 'Jurong Bird Park', 'Gardens by the Bay']
#start = 'Singapore Zoo'
start = 'Underwater World'

# Contruct distance graph
# install networkx : https://pypi.python.org/pypi/networkx/
# install openopt : https://pypi.python.org/pypi/openopt
# install milp : http://openopt.org/MILP
# install lpsolve : https://racingtadpole.com/blog/install-lpsolve-for-python/ 

import networkx as nx
import urllib2, json
from openopt import *

G = nx.Graph()
baseurl = 'https://maps.googleapis.com/maps/api/directions/json?'
src = 'origin='
des = '&destination='
otherParams = '&sensor=false&key=AIzaSyBn3GNyb8I5bUVSP7DdcEN1L_pnLQ6Hk5s'
for i in range(len(places)):
    for j in range(len(places)):
        if j<i :
        	p1 = places[i].replace(' ', '+')
        	p2 = places[j].replace(' ', '+')
        	url = baseurl+src+p1+','+country+ des+p2+','+country+otherParams
        	req = urllib2.Request(url, "")
        	response = urllib2.urlopen(req)
        	result_json = response.read()
        	jsonObj = json.loads(result_json)
        	distance = jsonObj['routes'][0]['legs'][0]['distance']['value']
        	G.add_edges_from([(i, j, {'distance':distance})])
        	
p = TSP(G, objective = 'distance', start = places.index(start))
r = p.solve('lpSolve')
print(r.nodes)
print(r.edges)
print(r.Edges)