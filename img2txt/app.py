import os
import boto3
from chalice import Chalice, Response
from botocore.exceptions import ClientError
from chalicelib.decoder import urlencoded_decoder
from chalicelib.s3_img import img_process
from chalicelib.rekognition import imgTotext
from chalicelib import response_helper

app = Chalice(app_name='img2txt')
s3_client = boto3.client('s3')
bot_name='img2txt-bot'
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
    #Only images allowed
    else:
        return Response(body=response_helper.body_invalid_type.format(name=bot_name),
                        status_code=200,
                        headers=response_helper.headers)


    #string of words
    words = imgTotext(S3_BUCKET,tmp['image_name'])

    # ################################
    # ### Logging to Cloudwatch ######
    print (d)
    ################################

    return Response(body=response_helper.body_success.format(name=bot_name,body=words),
                    status_code=200,
                    headers=response_helper.headers)
