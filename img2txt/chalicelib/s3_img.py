### Write image from Twilio MMS to an tmp file
### Return a dictionary
import requests

def img_process(url,from_number,ssmid,image_type):

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
    return (d)
