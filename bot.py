from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time
import requests

TOKEN = "
8500370995:AAEyrysu_Ik-Ei28XI6zMJIAUnGl5aC0RpA"
CHAT_ID = "-100xxxxxxxxxx"
MESSAGE = """ . روسيا والصين لن تحركا ساكنا من اجل حلفائهما. يكفي ان تنظر الى وقوفهما موقف المتفرج اثناء سقوط سوريا وفنزويلا. كل ما يعنيهما هو المصلحة الباردة وبيع السلاح تحت لافتة التحالف. اما اذا غرق الحليف فعلا فستجلسان تعزفان له سيمفونية الموت بهدوء متعال تماما كما في مشهد غرق سفينة التايتانيك.لا انقاذ ولا اندفاع ولا تضحيات. مجرد موسيقى جنائزية انيقة ومشاهدة من بعيد، لان الحلف عندهما عقد مؤقت لا اكثر، ينتهي مع اول شرخ في ميزان الربح والخسارة """


# --- Mini serveur web pour Render ---
class SimpleHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    self.wfile.write(b"Bot is running!")


def run_server():
  server = HTTPServer(("0.0.0.0", 10000), SimpleHandler)
  server.serve_forever()


# Lancer le serveur web en arrière-plan
threading.Thread(target=run_server, daemon=True).start()


# --- Votre boucle de messages ---
def send_message():
  url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": MESSAGE}
  try:
    requests.post(url, json=payload)
  except Exception as e:
    print(e)


while True:
  send_message()
  time.sleep(60)
  
