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
    password = os.getenv('SMTP_PW')
    recipient = data['id_mail'].split(' ')

    msg = MIMEMultipart()
    msg['Subject'] = data['id_subject']
    msg['From'] = sender
    msg['To'] = ', '.join(recipient)

    html = data['id_content']

    part = MIMEText(html, 'html')

    msg.attach(part)

    host = os.getenv('SMTP_HOST')
    port = os.getenv('SMTP_PORT')
    smtp_server = smtplib.SMTP(host, port)
    smtp_server.starttls()
    smtp_server.login(sender, password)


    smtp_server.sendmail(sender, recipient, msg.as_string())
    smtp_server.close()

async def mail(request):

    data = await request.post()
    if (data['id_mail'] == "" or data['id_subject'] == "" or
        data['id_content'] == ""):
        return  web.Response(text="Missing data", status=422);

    await send_mail(data)

    return web.Response(text="Email sent", status=200);


app.router.add_get('/', main)
app.router.add_post('/send_mail', mail)

web.run_app(app)
