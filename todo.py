import time
import schedule as s

def job():
    print("Montunuzu giymeyi unutmayın Narin hanım!!!!")

def job_weekend():
    print("Dışarı çıkacak olursanız montunuzu giymeyi sakın unutmayın Narin hanım!!!!")

s.every().monday.at("07:00").do(job)
s.every().tuesday.at("07:00").do(job)
s.every().wednesday.at("07:00").do(job)
s.every().thursday.at("07:00").do(job)
s.every().friday.at("07:00").do(job)
s.every().saturday.at("09:30").do(job_weekend)
s.every().sunday.at("09:30").do(job_weekend)

while(True):
    s.run_pending()
    time.sleep(1)