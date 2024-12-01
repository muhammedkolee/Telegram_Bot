import time
import schedule as s

async def run_schedule():
    def run():
        def job():
            return "Montunuzu giymeyi unutmayın Narin hanım!!!!"

        def job_weekend():
            return "Dışarı çıkacak olursanız montunuzu giymeyi sakın unutmayın Narin hanım!!!!"

        s.every().monday.at("07:00").do(job)
        s.every().tuesday.at("07:00").do(job)
        s.every().wednesday.at("07:00").do(job)
        s.every().thursday.at("07:00").do(job)
        s.every().friday.at("07:00").do(job)
        s.every().saturday.at("09:30").do(job_weekend)
        s.every().sunday.at("09:30").do(job_weekend)

        while(True):
            s.run_pending()

    def run2():
        def jobs():
            print("Komut çalışıyor...")
            return "merhaba..."

        s.every().seconds.do(jobs)

        while True:
            s.run_pending()


    while True:
        run2()
