import requests

custom_message = sys.argv[1]

blindvalues = {'a':'10', 'b':'120', 'c':'140', 'd':'1450', 'e':'150', 'f':'1240', 'g':'12450', 'h':'1250', 'i':'240', 'j':'2450', 'k':'130', 'l':'1230', 'm':'1340', 'n':'13450', 'o':'1350', 'p':'12340', 'q':'123450', 'r':'12350', 's':'2340', 't':'23450', 'u':'1360', 'v':'12360','w':'24560', 'x':'13460', 'y':'134560', 'z':'13560'}

blindmap = []

for i in custom_message:
	blindmap += blindvalues[i]

data = ''.join(blindmap)

PARAMS = {'message': data}
#PARAMS = PARAMS.json

URL = 'https://bnv.web.ctfcompetition.com/api/search'

r = requests.post(url = URL, json = PARAMS, proxies = {"https":'127.0.0.1:8080'}, verify = False)

print r.content



