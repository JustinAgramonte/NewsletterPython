#!usr/bin/env python3

'''Download articles from site daily. Possibly run in background. Check performance alteration'''
#iterate over urls --> send article links as part of one email ---> do every three days
	#use beautiful soup to read the href & send as article?

###Import Statements###
from bs4 import BeautifulSoup
import requests
import smtplib


###Variables###
sender = 'JustinAgramonte@gmail.com'
receiver = 'JustinAgramonte@gmail.com'
message = """From: From Person <%s> 
To: To Person <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format.

""" #%sender %receiver

CenterLeaningURLs = ["https://www.cityandstateny.com/news-politics", "https://www.cityandstateny.com/policy", 
"https://www.factcheck.org/", "https://americanmilitarynews.com/category/north-korea/", "https://americanmilitarynews.com/category/middle-east-regions/",
"https://americanmilitarynews.com/category/national-security/", "https://apnews.com/apf-technology", "https://apnews.com/apf-politics", 
"https://apnews.com/apf-business"] 
#Check the HTML code for href
#Look at following link for other sites right-leaning --> https://mediabiasfactcheck.com/right-center/

def LinkCompiler():
	for link in CenterLeaningURLs:
		request = requests.get(link)
		if request.status_code != requests.codes.ok:
			print('This failed')
			return None
		print(request.text)
		LinkParser()	
	# 	#get href for every link using beautiful soup
	# 	CenterLeaningURLsList = 
	# 	#add to list variable
	# return CenterLeaningURLsList

def LinkParser():
	NewsSoup = BeautifulSoup(request.text, 'html.parser')
	for link in NewsSoup.find_all('a'):
		link.get('href')
LinkCompiler()

# def LinkMailer():
