import telegram.ext 
import requests
import http.client
import ssl
import subprocess

TOKEN = "5591863640:AAHqDldhR_IeWV8vvegVa3zsnJ_947XBt0s"

def start(update, context):
    update.message.reply_text("""
    Hello!!! Selamat datang di DAO Official!
    
    Silahkan pilih menu yang kamu butuhkan:

    /start -> Welcome message
    /Restart_QRIS_service -> Restart service
    /Capture_grafana_NDS -> Capture dashboard live AADC NDS
    /contact -> DAO on duty
    """)
def Restart_QRIS_service(update, context):
    update.message.reply_text("running restart service QRIS")
    p = subprocess.run(['python','python_2.py', 'shell=True'])

def Capture_grafana_NDS(update, context):
    update.message.reply_text("Maaf, Fitur ini masih dalam tahap pengembangan T_T")

def contact(update, context):
    update.message.reply_text("Kontak tim kami di 083829320227")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("Restart_QRIS_service", Restart_QRIS_service))
disp.add_handler(telegram.ext.CommandHandler("Capture_grafana_NDS", Capture_grafana_NDS))

updater.start_polling()
updater.idle()