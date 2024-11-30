import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import weather as w
import money as m

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"""
/topla [sayi1] [sayi2] 
Verilen iki sayının toplamını döndürür.
                            
/weather [Şehir İsmi]
Girilen şehrin 7 günlük hava durumunu döndürür.
                            
/currency
Anlık döviz kurlarını gösterir.
                            
/currency [sayı]
Girilen sayıyı döviz kuru olarak hesaplar.
                                    """)


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Merhaba {update.effective_user.first_name}!')


async def topla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    values = context.args
    try:
        if len(values) == 2:
            await update.message.reply_text(f'{values[0]} + {values[1]} = {str(int(values[0]) + int(values[1]))}')
        else:
            await update.message.reply_text("Lütfen 2 adet sayı giriniz: /topla sayı1 sayı2")

    except:
            await update.message.reply_text("Lütfen sayı giriniz!")
    

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value = context.args
    try:
        print(value)
        print(value[0])
        await update.message.reply_text(w.hava(str(value[0])))

    except:
        await update.message.reply_text(f"Bir hata meydana geldi! Şehir ismini doğru yazdığınızdan emin olun (Şehir isimleri UTF-8 formatına uygun değildir.), tekrar denemek için -> /weather")


async def currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not context.args:
            await update.message.reply_text(m.para())
        elif not not context.args:
            if len(context.args) != 1:
                await update.message.reply_text(f"Birden fazla değer girişi oldu!")
            
            else:
                value = context.args
                await update.message.reply_text(m.para(int(value[0])))
    
    except:
        await update.message.reply_text(f"Bir hata meydana geldi! Lütfen bilgileri doğru girdiğinizden emin olun.")


if __name__ == '__main__':
    application = ApplicationBuilder().token('7322934392:AAHicDOumOq6XCDKk5r-NSnOk2rzmqdn2Jw').build()
    
    greeting_handler = CommandHandler('greeting', greeting)
    topla_handler = CommandHandler('topla', topla)
    weather_handler = CommandHandler("weather", weather)
    currency_handler = CommandHandler("currency", currency)
    help_handler = CommandHandler("help", help)

    application.add_handler(greeting_handler)
    application.add_handler(topla_handler)
    application.add_handler(weather_handler)
    application.add_handler(currency_handler)
    application.add_handler(help_handler)

    application.run_polling()