from chalice import Chalice, Response
import boto3
import os
from botocore.exceptions import ClientError
from chalicelib.decoder import urlencoded_decoder
from chalicelib.s3_img import img_process

app = Chalice(app_name='img2txt')
s3_client = boto3.client('s3')
bot_name='saludobot'
S3_BUCKET=os.environ['S3_BUCKET']


@app.route('/')
def index():
    return {'healthz': 'alive'}


@app.route('/messages', methods=['POST'],
            content_types=['application/x-www-form-urlencoded'])
def messages_in():
    request = app.current_request
    #Twilio x-www-form-urlencoded to a dictionary
    d = urlencoded_decoder(request.raw_body)

    #Check if the MMS is an image
    if 'image' in d['MediaContentType0']:
        #Write Twilio img to a tmp file
        #return a dictionary
        tmp=img_process(d['MediaUrl0'],d['From'],d['SmsSid'],d['MediaContentType0'])

        ##Upload to S3
        try:
            s3_client.upload_file(tmp['tmp_img'], S3_BUCKET, tmp['image_name'])
        except ClientError as e:
            return 'error occurred during upload: %s' % e.response['Error']['Message']
    else:
        return Response(body='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                             <Response><Message>{name}: I can only process images =( </Message></Response>'.format(name=bot_name),
                        status_code=200,
                        headers={'Content-Type': 'application/xml'})


    ################################
    #### Logging to Cloudwatch ####
    print (d)
    ################################
    return Response(body='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                         <Response><Message>{name}: {body} from: {state}</Message></Response>'.format(name=bot_name,body=d['Body'],state=d['From']),
                    status_code=200,
                    headers={'Content-Type': 'application/xml'})
