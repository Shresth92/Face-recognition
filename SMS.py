def SMS():
    from twilio.rest import Client
    account_xyz = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    client = Client(account_xyz, auth_token)
    message = client.messages.create(
                                  from_='+15XXXXXXXXXX',
                                  body ='Hello! This is XYZ',
                                  to ='+91XXXXXXXXXX'
                              )

    print(message.xyz)
