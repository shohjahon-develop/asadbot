# from bot import main as start_bot
#
# if __name__ == "__main__":
#     print("Bot serverda ishga tushmoqda 🚀")
#     start_bot()
#
# from flask import Flask
# import threading
# import asyncio
# from bot import application  # Bu bot.py faylida yaratilgan Application obyekti bo‘ladi
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return "🤖 AsadBot ishga tushdi va faol holatda!"
#
# def run_bot():
#     asyncio.run(application.run_polling())
#
# if __name__ == "__main__":
#     # Botni fon rejimda ishga tushiramiz
#     threading.Thread(target=run_bot).start()
#     # Flask web-serverni ishga tushiramiz (Render uchun zarur)
#     app.run(host="0.0.0.0", port=10000)


from flask import Flask
import asyncio
import os
from bot import main as bot_main # bot.py dagi main funksiyasini import qilamiz

app = Flask(__name__)

@app.route('/')
async def home(): # Bu yerda async funksiya bo'lishi shart emas, lekin hozircha qolaversin
    return "🤖 AsadBot ishga tushdi va faol holatda!"

@app.route('/health')
async def health_check():
    # Render servisning ishlashini tekshirish uchun oddiy endpoint
    return "OK", 200

def run_bot_in_thread():
    """Botni o'zining event loop'ida ishga tushiradi."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot_main() # bot.py dagi main funksiyasini chaqiramiz

if __name__ == "__main__":
    # Botni alohida thread'da ishga tushiramiz
    import threading
    bot_thread = threading.Thread(target=run_bot_in_thread)
    bot_thread.start()

    # Flask web-serverni ishga tushiramiz (Render uchun zarur)
    # Render odatda PORT environment o'zgaruvchisini ishlatadi.
    port = int(os.environ.get("PORT", 5000)) # Odatda Render 8080 yoki o'zi bergan portni kutadi.
                                             # Sizning skrinshotingizda 10000 ishlatilgan, shunga moslab qo'yaylik.
                                             # Ammo yaxshisi Renderning default PORT o'zgaruvchisini ishlating.
    app.run(host="0.0.0.0", port=port, debug=False)


