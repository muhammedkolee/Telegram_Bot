import http.client
import json

def soccer():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 5oGAiwnuaBuT0Ghvkoty59:7hXU2RIQRKz3T01zv33R1X"
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
            result += f"{str(veri['result'][i]['date'])[8:10]}-{str(veri['result'][i]['date'])[5:7]}-{str(veri['result'][i]['date'])[:4]} {str(veri['result'][i]['date'])[11:16]}\n"
            if str(veri['result'][i]['skor']) == 'undefined-undefined':
                result += f"{str(veri['result'][i]['home'])} - {str(veri['result'][i]['away'])}\n\n"
            else:
                result += f"{str(veri['result'][i]['home'])} {str(veri['result'][i]['skor'])} {str(veri['result'][i]['away'])}\n\n"

    return result

print(soccer())