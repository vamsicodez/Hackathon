import urllib3
from bs4 import BeautifulSoup, SoupStrainer

def extract_url():
	http = urllib3.PoolManager()
	url = raw_input("Enter Url") 
	try:             # Input Url
		response = http.request('GET',url)        # Get response of the url
	except except urllib3.exceptions.HTTPError,e:
		print "Enter Valid Url"
	except:
		print "Error in url"	
	host = urllib3.util.parse_url(url).host   # Get the domain name of the url
	host = host+"/"
	print response.status,host
	soup = BeautifulSoup(response.data)
	f=open("baseurl.txt","w")
	f.write(response.data)
	f.close()
	counter = 1
	for link in soup.find_all('a'):
		new_url = link.get('href')
		if new_url!=None:

			if new_url.startswith('http://'):
				try:
					response = http.request('GET',new_url)
					
				except urllib3.exceptions.HTTPError,e:
					continue
				except:
					continue		
			else:
				if new_url.startswith("/"):
					new_url = host+new_url[1:]
				else:
					new_url = url+new_url	
				try:
					response = http.request('GET',host+new_url)
					
				except urllib3.exceptions.HTTPError,e:
					continue
				except:
					continue	
			f=open("deriverd_url "+str(counter)+".txt","w")
			f.write(response.data)
			f.close()
			counter = counter+1

if __name__ == '__main__':
	extract_url()


				













			




except urllib3.exceptions.HTTPError,e:
	print "Enter valid url",url


