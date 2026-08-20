from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time
import requests

TOKEN = "8500370995:AAEyrysu_Ik-Ei28XI6zMJIAUnGl5aC0RpA"
CHAT_ID = "-1004374575953"
MESSAGE = """ 23. حقيقة: علي أولى الناس بكم بعد النبي.  https://www.youtube.com/watch?v=1GlmN1WKw1A السؤال: إذا لم يكن علي هو المقصود بالأولوية، فما تفسير النصوص التي تضعه في هذه المنزلة الخاصة؟


24. «من كنت مولاه فهذا علي مولاه».  https://www.youtube.com/watch?v=3_iquynE3wQ السؤال: لماذا تجعلون «مولى» بمعنى المحبة فقط عندما يتعلق الأمر بعلي، مع أن للكلمة معاني أوسع في العربية والحديث؟


25.حقيقة عائشة — كانت تؤذي رسول الله.  https://www.youtube.com/watch?v=u9YSdOncnkg السؤال: إذا كانت أذية النبي محرمة، فهل نناقش الروايات التي تثبتها أم تصبح «أم المؤمنين» فوق النقد؟


26. حقيقة عائشة 2 — عائشة تطعن وتسب وتشتم.  https://www.youtube.com/watch?v=XiwXw4KqZHw السؤال: هل معياركم هو احترام الشخص مهما ورد في الروايات، أم تطبيق نفس منهج النقد على الجميع؟


27. حقيقة عائشة 3 — موت عائشة يوم فرح وسرور عند رسول الله.  https://www.youtube.com/watch?v=Mf5J50RtMOQ السؤال: إن كانت الرواية باطلة، فلماذا لا تُردّ بالدليل بدل منع النقاش حولها؟


28. حقيقة عائشة 4 — كانت تبغض عليًا عليه السلام.  https://www.youtube.com/watch?v=gKns1nsjixU السؤال: كيف تفسرون وقوف عائشة في الجمل ضد علي، مع الإصرار على أن العلاقة بينهما لم تكن تحمل خلافًا سياسيًا حقيقيًا؟   """


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
  
