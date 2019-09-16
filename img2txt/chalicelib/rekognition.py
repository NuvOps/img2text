#From a imagage object stored in S3
# return words strings

import boto3
reko_client=boto3.client('rekognition')

def imgTotext(S3_BUCKET,image_name):

    words = ''
    detect=reko_client.detect_text(Image={'S3Object':{'Bucket':S3_BUCKET,'Name':image_name}})
    textDetections=detect['TextDetections']

    for text in textDetections:
        if text['Type'] == 'WORD':
           words = words + ' ' + text['DetectedText']
    return words
