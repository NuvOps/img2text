import sys
from chalice import Chalice, Response
from chalicelib.decoder import urlencoded_decoder

app = Chalice(app_name='img2txt')

@app.route('/')
def index():
    return {'healthz': 'alive'}


@app.route('/messages', methods=['POST'],
            content_types=['application/x-www-form-urlencoded'])
def messages_in():
    request = app.current_request
    d = urlencoded_decoder(request.raw_body)

    return Response(body='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                         <Response><Message>Echo: {body} from: {state}</Message></Response>'.format(body=d['Body'],state=d['From']),
                    status_code=200,
                    headers={'Content-Type': 'application/xml'})
