# myrequest.py
# url > resp.text
import requests

def get(url):
    
    html = ''
    resp = requests.get(url)
    resp.encoding = None # 한글 깨짐 방지
    
    if resp.status_code == 200:
        html = resp.text
    
    return html








