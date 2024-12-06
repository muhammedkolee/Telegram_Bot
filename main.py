from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import weather as w
import money as m
import namaz as n
import football as f
import bmi as b
# import todo as t

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"""
/greeting
Selamlama                                    

/topla [sayi1] [sayi2] 
Verilen iki sayının toplamını döndürür.
                            
/weather [Şehir İsmi]
Girilen şehrin 7 günlük hava durumunu döndürür.
                            
/currency
Anlık döviz kurlarını gösterir.
                            
/currency [sayı]
Girilen sayıyı döviz kuru olarak hesaplar.
                                    
/namaz [sehir_ismi]
Girilen şehrin o günlük namaz vakitlerini döndürür.

/bmi [boy] [kilo]
Boy ve kilo bilgilerine göre Vücut Kitle İndeksini hesaplar ve sağlıklı olup olmadığınızı söyler.                                    
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

    except Exception as e:
            await update.message.reply_text("Lütfen sayı giriniz! {e}")
    

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value = context.args
    try:
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


async def namaz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not context.args:
            await update.message.reply_text(f"Lütfen şehir ismi giriniz! -> /namaz [sehir_ismi]")
        
        elif not not context.args:
            if len(context.args) != 1:
                await update.message.reply_text(f"Birden fazla değer girişi oldu!")

            else:
                value = context.args
                await update.message.reply_text(n.vakit(str(value[0])))

    except:
        await update.message.reply_text(f"Bir hata meydana geldi. Lütfen tekrar deneyiniz.")


async def futbol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text(f.soccer())
    except Exception as e:
        await update.message.reply_text(f"Bir hata meydana geldi. Lütfen tekrar deneyiniz.")


async def bmi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not context.args:
            await update.message.reply_text(f"Lütfen sırasıyla boy ve kilo değerlerini giriniz. -> /bmi [boy] [kilo]")
        
        elif not not context.args:
            if len(context.args) != 2:
                await update.message.reply_text(f"Lütfen boy ve kilo değerleri girdiğinizden emin olun. -> /bmi [boy] [kilo]")
            elif len(context.args) == 2:
                value = context.args
                print(value[0])
                print(value[1])
                await update.message.reply_text(b.data(int(value[0]), int(value[1])))
            else:
                await update.message.reply_text(f"Bilinmeyen bir hata meydana geldi, lütfen tekrar deneyiniz. -> /bmi [boy] [kilo]")
    except Exception as a:
        await update.message.reply_text(f"Bilinmeyen bir hata meydana geldi! Lütfen tekrar deneyiniz. -> /bmi [boy] [kilo]\n{a}")
        



# async def todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # try:
    #     if not context.args:
    #         await update.message.reply_text(f"Komut alındı!")
    #         await update.message.reply_text(t.run_schedule())

    #     else:
    #         await update.message.reply_text(f"Lütfen komuttan sonra değer girmeyiniz!!")
    # except:
    #     await update.message.reply_text(f"Bir hata meydana geldi. Lütfen tekrar deneyiniz.")

if __name__ == '__main__':
    application = ApplicationBuilder().token("7322934392:AAHusoJDqdXyBHnDPSYvxKGOixa8YAAuZxo").build()

    greeting_handler = CommandHandler('greeting', greeting)
    topla_handler = CommandHandler('topla', topla)
    weather_handler = CommandHandler("weather", weather)
    currency_handler = CommandHandler("currency", currency)
    help_handler = CommandHandler("help", help)
    namaz_handler = CommandHandler("namaz", namaz)
    footbal_handler = CommandHandler("football", futbol)
    bmi_handler = CommandHandler("bmi", bmi)
    # todo_handler = CommandHandler("todo", todo)

    application.add_handler(greeting_handler)
    application.add_handler(topla_handler)
    application.add_handler(weather_handler)
    application.add_handler(currency_handler)
    application.add_handler(help_handler)
    application.add_handler(namaz_handler)
    application.add_handler(footbal_handler)
    application.add_handler(bmi_handler)
    # application.add_handler(todo_handler)

    application.run_polling()