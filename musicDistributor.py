import random, smtplib

playlist = "http://www.youtube.com/watch_videos?video_ids="

raw = open('musicFound.txt',"r")

hold = []

for i in raw:
	hold.append(i)
	

description =''

random = random.sample(range(0,len(hold)-1),5)

for i in random:
	chosen = hold[i]
	print(chosen)
	chosen = chosen.split('|||')
	chosen[2] = chosen[2][:-1]
	if "youtu.be" in chosen[2]:
		vid = chosen[2].split('.be/')
	else:
		if 'v=' in chosen[2]: 
			vid = chosen[2].split('v=')
		else:
			vid = chosen[2].split('v%3D')
	playlist += vid[1][0:11] +","
	description +=  chosen[0] + " | " + chosen[1] +"\n"+"\n"
print(random)
for x in random[::-1]:
	hold.pop(0)

print(playlist)

updatedlist = open('musicFound.txt','w')
for i in hold:
	updatedlist.write(i)

updatedlist.close()
raw.close()

#Email section 
username = "" #add here
password = "" #add here
sender = '' #add here
receivers = [''#add here]

try:
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.ehlo()
   server.login(username,password)
   server.sendmail(sender, receivers,"Subject: <heres New Music>" +"\n"+ description +"\n"+ playlist)         
   print("Successfully sent email")
except:
   print("Error: unable to send email")



'''
#Fuck using the youtube api till further notice
#https://developers.google.com/youtube/v3/quickstart/python

key = 'AIzaSyBBIhashagqFCdQ-3ETLPtRxdbWsKFMyAE'

## -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from datetime import date

today = date.today().strftime("%d/%m/%Y")

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
#    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_327326406685-1m4lioj7coq5jlt49q4ado1bm4ifu5kt.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials, developerKey = key)

    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": "with ears unclouded",
            "description": today,
            "tags": [
              "sample playlist",
              "API call"
            ],
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "public"
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
'''
