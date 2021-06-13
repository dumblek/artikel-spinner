from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from oauth2client import client
import webbrowser
import time
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from os import listdir
from os.path import isfile, join

xmlDict = {}
sitemap_url = input("Input your sitemap url with https://: ")
path_to_cred = input("Input your path to credential: ")
r = requests.get(sitemap_url, time.sleep(10))
xml = r.text

soup = BeautifulSoup(xml)
sitemapTags = [re.findall(r"(?<=loc>).*(?=</loc>)", str(url))[0] for url in soup.find_all("loc")]



SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# using service account
JSON_KEY_FILE = [f for f in listdir(path_to_cred) if isfile(join(path_to_cred, f))]
jsons = ['/Users/ayyoub/Downloads/oaut2/client_secret_1084374245520-doote8e38hpnko5p85p2jf3gq6h3mnhd.apps.googleusercontent.com.json']
#using oauth2.0
"""Flows through OAuth 2.0 authorization process for credentials."""
out = pd.DataFrame(columns=['url', 'status'])
j = 0
method = input("Using service account or oauth2: ")
for i in range(0, len(JSON_KEY_FILE)):
    if method == 'oauth2':
        # auth the indexing api
        flow = client.flow_from_clientsecrets(
            jsons[i],
            scope=SCOPES,
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        # (2)
        auth_uri = flow.step1_get_authorize_url()
        print(auth_uri)
        # webbrowser.open(auth_uri)

        # (3')
        auth_code = input('Enter the authentication code: ')

        # (4),(5)
        credentials = flow.step2_exchange(auth_code)


        http = credentials.authorize(httplib2.Http())

        #auth the console search
        flow = client.flow_from_clientsecrets(
            jsons[i],
            scope="https://www.googleapis.com/auth/webmasters",
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        auth_uri = flow.step1_get_authorize_url()
        print(auth_uri)
        # webbrowser.open(auth_uri)

        # (3')
        auth_code = input('Enter the authentication code: ')

        # (4),(5)
        credentials = flow.step2_exchange(auth_code) 
        credentials.authorize(httplib2.Http())
    elif method == 'service account':
        credentials = ServiceAccountCredentials.from_json_keyfile_name(path_to_cred+JSON_KEY_FILE[i], scopes=SCOPES)
        http = credentials.authorize(httplib2.Http())
        
    while j < len(sitemapTags):
        content = '''{
          \"url\": \"'''+sitemapTags[j]+'''\",
          \"type\": \"URL_UPDATED\"
        }'''
        # sitemapTags[j]
        print(j, sitemapTags[j])
        response, content = http.request(ENDPOINT, method="POST", body=content)
        print(response['status'], content)
        out = out.append({'url':j, 'status':response['status']}, ignore_index=True)
        time.sleep(3)
        if response['status'] == '200':
            j += 1
            print("sini")
        elif response['status'] == '429':
            j = j
            print("sini2")
            break
        elif response['status'] == '403':
            j = j
            print("You have not verify this domain in search console yet")
            break
out.to_csv('/home/agc/out_indexing.csv', index = False)