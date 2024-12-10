import http.client
import json

def soccer():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey"
        }

    conn.request("GET", "/football/results?data.league=super-lig", headers=headers)

    res = conn.getresponse()
    data = res.read()
    veri = json.loads(data.decode("utf-8"))

    result = ""

    for i in range(len(veri['result'])):
        if str(veri['success']) != 'True':
            result += "Bugünlük API hakkı dolmuştur. Lütfen farklı bir zamanda tekrar deneyiniz!"
            return result           
        else:
            result += f"{str(veri['result'][i]['date'])[8:10]}-{str(veri['result'][i]['date'])[5:7]}-{str(veri['result'][i]['date'])[:4]} {str(int(veri['result'][i]['date'][11:13])+3)}:{str(veri['result'][i]['date'])[14:16]}\n"
            if str(veri['result'][i]['skor']) == 'undefined-undefined':
                result += f"{str(veri['result'][i]['home'])} - {str(veri['result'][i]['away'])}\n\n"
            else:
                result += f"{str(veri['result'][i]['home'])} {str(veri['result'][i]['skor'])} {str(veri['result'][i]['away'])}\n\n"
    return result

def league():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey"
        }

    conn.request("GET", "/football/league?data.league=super-lig", headers=headers)

    res = conn.getresponse()
    data = res.read()
    veri = json.loads(data.decode("utf-8"))
    result = ""
    max_length = 0

    for i in range(len(veri['result'])):
        if len(veri['result'][i]['team']) > max_length:
            max_length = len(veri['result'][i]['team'])

    gap = len(str(veri['result'][0]['point']))

    for i in range(len(veri['result'])):
        if gap == len(str(veri['result'][i]['point'])):
            result += f"{veri['result'][i]['point']}p - {veri['result'][i]['team']}\n"
        else:
            result += f"{veri['result'][i]['point']}p   - {veri['result'][i]['team']}\n"   
    return result