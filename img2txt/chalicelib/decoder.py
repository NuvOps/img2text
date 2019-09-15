##Twilio POSTed 'application/x-www-form-urlencoded'
##Function convert application/x-www-form-urlencoded to a dictionary

from urllib.parse import unquote_plus


def urlencoded_decoder(raw_form):
    l = []
    d = {}
    decode = raw_form.decode('ascii')
    decode = unquote_plus(decode)
    for i in decode.split('&'):
       l = i.split('=')
       d[l[0]] = l[1]

    #return a dictionary
    return d
