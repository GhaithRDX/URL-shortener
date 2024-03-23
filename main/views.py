from django.shortcuts import render
import pyshorteners 
import bitly_api
import requests
import json

bitly_token ='ca742bde600bfa01e77c801477a29ece72589403'
group_guid = 'Bo3l9SkBK0g'
bitly_api_url = 'https://api-ssl.bitly.com/v4/shorten'


def url(request):
    
    if request.method == 'POST':
        url_received = request.POST["url"]
        short_url = pyshorteners.Shortener().tinyurl.short(url_received)
        context ={
            'new_url':short_url,
            'old_url':url_received,
        }
        return render(request ,"form.html",context)
    
    else : 
        return render(request,"form.html")

def bitly(request):
    if request.method == 'POST':
        try:
            
            url_received = request.POST["url"]
            headers = {
            'Authorization': f'Bearer {bitly_token}',
            'Content-Type': 'application/json'
            }

            payload = {
                'group_guid': group_guid,
                'domain': 'bit.ly',
                'long_url': url_received
            }

            response = requests.post(bitly_api_url, headers=headers, data=json.dumps(payload))

            if response.ok:
                link = response.json().get('link')
                context ={
                    'new_url':link,
                    'old_url':url_received,
                }
                return render(request,"form_bitly.html",context)
            else:
                print(f'Error: {response.text}')
                return render(request ,"form_bitly.html")
                        
        except Exception as e:
            print("Error" , e)    
            return render(request ,"form_bitly.html")
        
    