#String helpers



headers={'Content-Type': 'application/xml'}

body_invalid_type='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                     <Response><Message>{name}: I can only process images =( </Message></Response>'


body_success='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                     <Response><Message>{name}: {body}</Message></Response>'



body_error='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                     <Response><Message>{name}: Sorry, I\'m broken =( </Message></Response>'



body_no_image='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                     <Response><Message>{name}: Send me an image with text</Message></Response>'



body_multiple_images='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                     <Response><Message>{name}: One image at a time</Message></Response>'
