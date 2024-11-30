import http.client
import json

def para(num = 0): 
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 5oGAiwnuaBuT0Ghvkoty59:7hXU2RIQRKz3T01zv33R1X"
        }


    def mny():
        if num == 0:
            conn.request("GET", f"/economy/currencyToAll?int={num}&base=USD", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            dolar = json.loads(data)

            if str(dolar['success']) == 'True':
                result = ""
                result += f"1$ = {(dolar['result']['data'][-4]['rate'])}₺\n"

            else:
                return "Döviz kuru için bugünlük API hakkı dolmuştur.\n"


            conn.request("GET", f"/economy/currencyToAll?int={num}&base=EUR", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            euro = json.loads(data)

            if str(euro['success']) == 'True':
                result += f"1€ = {(euro['result']['data'][-5]['rate'])}₺\n"

            else:
                return "Döviz kuru için bugünlük API hakkı dolmuştur.\n"

            conn.request("GET", f"/economy/currencyToAll?int={num}&base=RUB", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            ruble = json.loads(data)

            if str(ruble['success']) == 'True':
                result += f"1₽ = {str(ruble['result']['data'][-5]['rate'])}₺"

            else:
                return "Döviz kuru için bugünlük API hakkı dolmuştur.\n"

            return result

        else:
            conn.request("GET", f"/economy/currencyToAll?int={num}&base=USD", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            usd = json.loads(data)

            if str(usd['success']) == 'True':
                result = ""
                result += f"{num}$ = {(usd['result']['data'][-4]['calculatedstr'])}₺\n"

            else:
                return "Döviz kuru için bugünlük API hakkı dolmuştur.\n"

            conn.request("GET", f"/economy/currencyToAll?int={num}&base=EUR", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            eur = json.loads(data)

            if str(eur['success']) == 'True':
                result += f"{num}€ = {(eur['result']['data'][-5]['calculatedstr'])}₺\n"

            else:
                return "Döviz kuru için bugünlük API hakkı dolmuştur.\n"

            conn.request("GET", f"/economy/currencyToAll?int={num}&base=RUB", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            rub = json.loads(data)

            if str(rub['success']) == 'True':
                result += f"{num}₽ = {str(rub['result']['data'][-5]['calculatedstr'])}₺\n\n"

            else:
                return "Döviz kuru için bugünlük API hakkı dolmuştur.\n"

            return result

    def gold():

        conn.request("GET", "/economy/goldPrice", headers=headers)  
        res = conn.getresponse()
        data = res.read()
        veri = json.loads(data)
        result = ""

        if veri['success'] == 'True':
            for i in range(6):
                result += f"{veri['result'][i]['name']}\nAlış: {veri['result'][i]['buying']}\nSatış: {veri['result'][i]['selling']}\n"
            return result
        
        else:
            return "Altın fiyatları için bugünlük API hakkı dolmuştur."


    return f"{mny()}{gold()}"
print(para())