### Write image from Twilio MMS to an tmp file
### Return a dictionary
import requests
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def img_process(url,from_number,ssmid,image_type,S3_BUCKET):

    d = {}
    twilio_img_url = url
    image_name = from_number + '/' + ssmid + '.' + image_type[6:]
    tmp_image_name = '/tmp/' + ssmid + '.' + image_type[6:]
    tmp_img = requests.get(twilio_img_url)

    #Write tmp file
    with open(tmp_image_name,'wb') as f:
        f.write(tmp_img.content)
    d['tmp_img'] = tmp_image_name
    d['image_name'] = image_name

    ##Upload to S3
    try:
        s3_client.upload_file(d['tmp_img'], S3_BUCKET, d['image_name'])
        return (d)
    except:
        return ('error occurred during upload: %s' % e.response['Error']['Message'])
