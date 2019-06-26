from bs4 import BeautifulSoup
import requests
import time

r = requests.get('https://drivetothetarget.web.ctfcompetition.com/')

soup = BeautifulSoup(r.content, 'html.parser')

token =  soup.find_all('input')[2].get('value')

lat = 51.6498
lon = 0.0982
Inc_Flag = False

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

def getLat():
	#print 'Called getLat function'
	global lat
	global lon
	global token
	global Inc_Flag
	if False == Inc_Flag:
		lat -= 0.00002
	else:
		lon -= 0.00002
	URL = 'https://drivetothetarget.web.ctfcompetition.com/?lat=' + str(lat) + '&lon='+ str(lon)+'&token=' + token

	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'html.parser')
	token =  soup.find_all('input')[2].get('value')

	print "Lat = ", soup.find_all('input')[0].get('value')
	print "Lon = ", soup.find_all('input')[1].get('value')
	print "Token = ", soup.find_all('input')[2].get('value')

	print str(soup.find_all('p')[-1])

	if 'away' in str(soup.find_all('p')[-1]):
		if False == Inc_Flag:
			Inc_Flag = True
		else:
			return True		
	return False

while True:
	ret_val = getLat()
	if True == ret_val:
		print lat, lon, token
		break
	time.sleep(0.05)	
