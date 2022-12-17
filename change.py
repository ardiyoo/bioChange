import json
import requests
import subprocess

clear = lambda: subprocess.call('cls||clear', shell=True)
r = requests.session()

def login(username, password, bio):
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'mid=Y2Zv0gALAAEu2xjDmODiS0opiELA; ig_did=AB9E03B4-E094-4D2B-B295-D7CFB20D65A1; ig_nrcb=1; datr=S3BmY_2v51I_b8fww9zR1aB6; dpr=0.8999999761581421; shbid="16372\\05454147915088\\0541701901105:01f77b2a5480337e83146ee2a5843996075dab66332d5b72b461c4a20b9419ec1c1fcd32"; shbts="1670365105\\05454147915088\\0541701901105:01f7e5493083668fde5d4a18a40cf57ac216653222b7fde18586f9ee9a12c794c79f20e0"; rur="ODN\\05454147915088\\0541701901219:01f7fb64b084cc8ab0376fe4e4986a5fe012dfaed87bde25285fe4bed8a4633d84fb31cd"; csrftoken=RVKL9DIHFzNcOVaUDTIVFhM3utZZWKlj',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'RVKL9DIHFzNcOVaUDTIVFhM3utZZWKlj',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2tHwWsnNKjUMXhhUua50EwO_6RI4V6jMUl1VdRKsWF3MNV',
        'x-instagram-ajax': '1006692538',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:10:1670361832:{password}',
        'username': f'{username}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}',
    }

    res = r.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)

    if 'authenticated":true' in res.text:
        sessioni = res.cookies['sessionid']
        getinfo(sessioni, bio)
    elif 'authenticated":false' in res.text:
        print('Username Or Password Incorrect')
        input()
    else:
        print(f'Unknown Error: {res.text}')
        input()


def getinfo(sessionID, bio):
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': f'sessionid={sessionID};',
        'referer': 'https://www.instagram.com/accounts/edit/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'qmWu8mnd4fXiysqxkDFdv60xqgppiDuu',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2tHwWsnNKjUMXhhUua50EwO_6RI4V6jMUl1VdRKsWF3MNV',
        'x-requested-with': 'XMLHttpRequest',
    }

    res = r.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', headers=headers)

    data = json.loads(res.text)

    firstname = data['form_data']['first_name']
    email = data['form_data']['email']
    username = data['form_data']['username']
    phone_number = data['form_data']['phone_number']

    change(sessionID, firstname, email, username, phone_number, bio)
        
def change(sess, first_name, email, username, phone_number, bio):
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'sessionid={sess};',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/edit/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'RoNpzqG5S8POHg6iVyYatwCd4ySjTnF5',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2tHwWsnNKjUMXhhUua50EwO_6RI4V6jMUl1VdRKsWF3MNV',
        'x-instagram-ajax': '1006692538',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'first_name': f'{first_name}',
        'email': f'{email}',
        'username': f'{username}',
        'phone_number': f'{phone_number}',
        'biography': f'{bio}',
    }

    res = r.post('https://www.instagram.com/api/v1/web/accounts/edit/', headers=headers, data=data)

    if '{status: "ok"}' in res.text:
        print(f'Bio Changed to: {bio}')
        input()
    else:
        print(f'Error: {res.text}')
    
clear()
username = input('Enter Username: ')
password = input('Enter Password: ')
bio = input('Enter Biography: ')

login(username, password, bio)
