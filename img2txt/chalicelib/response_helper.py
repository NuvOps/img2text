#String helpers



headers={'Content-Type': 'application/xml'}

body_invalid_type='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                     <Response><Message>{name}: I can only process images =( </Message></Response>'


body_success='<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                     <Response><Message>{name}: {body}</Message></Response>'
