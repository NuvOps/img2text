import sys
from chalice import Chalice, Response
from urllib.parse import urlparse, parse_qs

app = Chalice(app_name='img2txt')

@app.route('/')
def index():
    return {'healthz': 'alive'}


@app.route('/messages', methods=['POST'],
            content_types=['application/x-www-form-urlencoded'])
def messages_in():
    request = app.current_request
    raw=request.raw_body
    raw = raw.decode('ascii')

    l = []
    d = {}
    for i in raw.split('&'):
       l = i.split('=')
       d[l[0]] = l[1]

    return Response(body='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                         <Response><Message>Echo: %s </Message></Response>' %d['Body'],
                    status_code=200,
                    headers={'Content-Type': 'application/xml'})


    # parsed = parse_qs(app.current_request.raw_body.decode())
    # return {
    #     'states': parsed.get('states', [])
    # }
