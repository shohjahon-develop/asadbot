# from bot import main as start_bot
#
# if __name__ == "__main__":
#     print("Bot serverda ishga tushmoqda 🚀")
#     start_bot()

from flask import Flask
import threading
import asyncio
from bot import application  # Bu bot.py faylida yaratilgan Application obyekti bo‘ladi

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 AsadBot ishga tushdi va faol holatda!"

def run_bot():
    asyncio.run(application.run_polling())

if __name__ == "__main__":
    # Botni fon rejimda ishga tushiramiz
    threading.Thread(target=run_bot).start()
    # Flask web-serverni ishga tushiramiz (Render uchun zarur)
    app.run(host="0.0.0.0", port=10000)



# import os
# import threading
# from flask import Flask
# from bot import start_bot
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return "🤖 Bot is running successfully!"
#
# if __name__ == '__main__':
#     # Botni fon (thread)da ishga tushiramiz
#     t = threading.Thread(target=start_bot)
#     t.start()
#
#     # Flask web serverni ishga tushiramiz
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)
