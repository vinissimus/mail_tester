from aiohttp import web
import os
import aiohttp
import asyncio
import aiohttp_jinja2
import jinja2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = web.Application()

aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('templates'))

async def main(request):
    context = {}
    tpl = aiohttp_jinja2.render_template('index.html', request, context)
    return tpl

async def send_mail(data):
    sender = os.getenv('SMTP_USER')
    password = os.getenv('SMTP_PW') # Your SMTP password for Gmail
    recipient = data['id_mail']

    msg = MIMEMultipart()
    msg['Subject'] = data['id_subject']
    msg['From'] = sender
    msg['To'] = recipient

    html = data['id_content']

    part = MIMEText(html, 'html')

    msg.attach(part)

    smtp_server = smtplib.SMTP("smtp.office365.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender, password)


    smtp_server.sendmail(sender, recipient, msg.as_string())
    smtp_server.close()

async def mail(request):
    enviable = True

    #Check data
    data = await request.post()
    if (data['id_mail'] == "" or data['id_subject'] == "" or data['id_content'] == ""):
        enviable = False

    #Send e_mail
    if (enviable):
        await send_mail(data)

    #Load the template
    if (enviable):
        tpl = aiohttp_jinja2.render_template('mail_sent.html', request, data)
    else:
        tpl = aiohttp_jinja2.render_template('wrong_data.html', request, data)



    return tpl

app.router.add_get('/', main)
app.router.add_post('/send_mail', mail)

web.run_app(app)
