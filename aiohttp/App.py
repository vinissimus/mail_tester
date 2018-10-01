from aiohttp import web
import os
import aiohttp
import asyncio
import aiohttp_jinja2
import jinja2
import smtplib


app = web.Application()

aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('templates'))

async def main(request):
    context = {}
    tpl = aiohttp_jinja2.render_template('tmpl.html', request, context)
    return tpl

async def send_mail(data):

    sender = os.getenv('SMTP_USER')
    password = os.getenv('SMTP_PW') # Your SMTP password for Gmail

    recipient = data['id_mail']
    subject = data['id_subject']
    text = data['id_content']

    smtp_server = smtplib.SMTP("smtp.office365.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender, password)
    message = "Subject: {}\n\n{}".format(subject, text)
    print(message)
    smtp_server.sendmail(sender, recipient, message)
    smtp_server.close()

async def mail(request):
    enviable = True

    #Comprovar dades
    data = await request.post()
    if (data['id_mail'] == "" or data['id_subject'] == "" or data['id_content'] == ""):
        enviable = False

    #Enviar email
    if (enviable):
        await send_mail(data)

    #Carregar template en funció del resultat
    if (enviable):
        tpl = aiohttp_jinja2.render_template('mail_sent.html', request, data)
    else:
        tpl = aiohttp_jinja2.render_template('wrong_data.html', request, data)



    return tpl

app.router.add_get('/', main)
app.router.add_post('/send_mail', mail)

web.run_app(app)
