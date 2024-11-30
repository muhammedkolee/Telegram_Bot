import http.client
import json



def hava(city):
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 5oGAiwnuaBuT0Ghvkoty59:7hXU2RIQRKz3T01zv33R1X"
        }

    lang = "tr"

    conn.request("GET", f"/weather/getWeather?data.lang={lang}&data.city={city}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data = data.decode("utf-8")

    veri = json.loads(data)

    result = ""

    print(f"{city.capitalize()} şehri için 7 günlük hava durumu:")
    for i in range(0,7):
        result += f"{veri['result'][i]['date']} {veri['result'][i]['day']} {int(float(veri['result'][i]['degree']))}° hava {veri['result'][i]['description']}\n\n"

    return f"{city.capitalize()} şehri için 7 günlük hava durumu:\n{result}"
