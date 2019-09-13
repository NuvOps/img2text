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

    return Response(body='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                         <Response><Message>Hello from Lambda</Message></Response>',
                    status_code=200,
                    headers={'Content-Type': 'application/xml'})

    # parsed = parse_qs(app.current_request.raw_body.decode())
    # return {
    #     'states': parsed.get('states', [])
    # }
