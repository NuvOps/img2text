import os
import boto3
from chalice import Chalice, Response
from botocore.exceptions import ClientError
from chalicelib.decoder import urlencoded_decoder
from chalicelib.s3_img import img_process
from chalicelib.rekognition import imgTotext
from chalicelib import response_helper

app = Chalice(app_name='img2txt')
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
    ### Logging to Cloudwatch ######
    print (d)

    #Check if there is an Image attached
    if d['NumMedia'] == '0':
        return Response(body=response_helper.body_no_image.format(name=bot_name),
                        status_code=200,
                        headers=response_helper.headers)

    ## No support for multiple images
    if d['NumMedia'] != '1':
        return Response(body=response_helper.body_multiple_images.format(name=bot_name),
                        status_code=200,
                        headers=response_helper.headers)

    #Check if the MMS is an image
    if 'image' in d['MediaContentType0']:
        ###Upload to S3
        #return a dictionary
        try:
            tmp=img_process(d['MediaUrl0'],d['From'],d['SmsSid'],d['MediaContentType0'],S3_BUCKET)
        except:
            return Response(body=response_helper.body_error.format(name=bot_name),
                            status_code=200,
                            headers=response_helper.headers)

    #Only images allowed
    else:
        return Response(body=response_helper.body_invalid_type.format(name=bot_name),
                        status_code=200,
                        headers=response_helper.headers)

    #string of words
    words = imgTotext(S3_BUCKET,tmp['image_name'])

    return Response(body=response_helper.body_success.format(name=bot_name,body=words),
                    status_code=200,
                    headers=response_helper.headers)
