from flask import Flask, render_template
import os
import time
app = Flask(__name__)

app.secret_key=os.urandom(30)

#GO TO INDEX PAGE
@app.route('/')
def a():
    starttime = time.time()

    hostname = "web.whatsapp.com" #example
    response = os.system("ping -c 1 " + hostname)
    whatsapp=""
    
#and then check the response...
    if response == 0:
      whatsapp="Green"  
      print(hostname+"up")
    else:
      whatsapp="red"
      print(hostname+'is down!')
        
    hostname = "google.com" #example
    response = os.system("ping -c 1 " + hostname)
    google=""
    
#and then check the response...
    if response == 0:
      google="Green"  
      print("up")
    else:
      google="red"
      print('is down!')
        
    
    
    return render_template("index.html",whatsapp=whatsapp,google=google)

if __name__ == '__main__':
    app.run(use_reloader = True,debug=True)
