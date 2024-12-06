import http.client
import json

def vakit(city = "cankiri"):
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 5oGAiwnuaBuT0Ghvkoty59:7hXU2RIQRKz3T01zv33R1X"
        }

    conn.request("GET", f"/pray/all?data.city={city}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    veri = json.loads(data)
    result = f"{city.capitalize()} şehri için bugünlük namaz vakitleri:\n"

    if str(veri['success']) == 'True':
        for i in range(6):
            result += f"{veri['result'][i]['vakit']}: {veri['result'][i]['saat']}\n"
        return result
    
    else:
        return "Namaz vakti için bugünlük API hakkı dolmuştur."