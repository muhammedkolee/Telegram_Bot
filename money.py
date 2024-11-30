import http.client
import json

def para(num = 0): 
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 5oGAiwnuaBuT0Ghvkoty59:7hXU2RIQRKz3T01zv33R1X"
        }


    if num == 0:
        conn.request("GET", f"/economy/currencyToAll?int={num}&base=USD", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        veri = json.loads(data)

        result = ""
        result += f"1$ = {(veri['result']['data'][-4]['rate'])}₺\n"

        conn.request("GET", f"/economy/currencyToAll?int={num}&base=EUR", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        veri = json.loads(data)

        result += f"1€ = {(veri['result']['data'][-5]['rate'])}₺\n"

        conn.request("GET", f"/economy/currencyToAll?int={num}&base=RUB", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        veri = json.loads(data)

        result += f"1₽ = {str(veri['result']['data'][-5]['rate'])}₺"
        return result

    else:
        conn.request("GET", f"/economy/currencyToAll?int={num}&base=USD", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        veri = json.loads(data)

        result = ""
        result += f"{num}$ = {(veri['result']['data'][-4]['calculatedstr'])}₺\n"

        conn.request("GET", f"/economy/currencyToAll?int={num}&base=EUR", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        veri = json.loads(data)

        result += f"{num}€ = {(veri['result']['data'][-5]['calculatedstr'])}₺\n"

        conn.request("GET", f"/economy/currencyToAll?int={num}&base=RUB", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        veri = json.loads(data)

        result += f"{num}₽ = {str(veri['result']['data'][-5]['calculatedstr'])}₺"
        return result

para(10)