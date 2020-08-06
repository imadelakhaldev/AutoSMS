# Imad Elakhal | Smartest Programmer Ever Lived.

from twilio.rest import Client


class AutoSMS:
    class AutoSMSMessage:
        def __init__(self, status, date, price):
            self.status = status
            self.date_sent = date
            self.price = price

    def __init__(self, account_sid, auth_token):
        print("######### STARTING AUTOSMS #########")
        try:
            self.client = Client(account_sid, auth_token)
            print("Twilio client created successfully.")
        except Exception as ex:
            print("Unable to initialize AutoSMS.")
            print(ex)

    def reconnect(self, account_sid, auth_token):
        try:
            self.client = Client(account_sid, auth_token)
            print("Twilio client re-connected successfully.")
        except Exception as ex:
            print("Unable to re-connect AutoSMS.")
            print(ex)

    def send_sms(self, sender, receiver, content):
        try:
            message = self.client.messages \
                .create(
                    body=content,
                    from_=sender,
                    to=receiver
                )

            revalue = self.AutoSMSMessage(message.status, message.date_sent, message.price)

            if message.status == "sent" or message.status == "queued" or message.status == "delivered":
                print("SMS has been sent successfully.")
                return revalue
            else:
                print("Unable to send an SMS.")
                return revalue
        except Exception as ex:
            print("Unable to send an SMS.")
            print(ex)

    def send_mms(self, sender, receiver, content, media_url):
        try:
            message = self.client.messages \
                .create(
                    body=content,
                    from_=sender,
                    media_url=[media_url],
                    to=receiver
                )

            revalue = self.AutoSMSMessage(message.status, message.date_sent, message.price)

            if message.status == "sent" or message.status == "queued" or message.status == "delivered":
                print("MMS has been sent successfully.")
                return revalue
            else:
                print("Unable to send an SMS.")
                return revalue
        except Exception as ex:
            print("Unable to send an MMS.")
            print(ex)

    def send_multi_sms(self, sender, receivers, content):
        for receiver in receivers:
            self.send_sms(sender=sender, receiver=receiver, content=content)

    def send_multi_mms(self, sender, receivers, content, media_url):
        for receiver in receivers:
            self.send_mms(sender=sender, receiver=receiver, content=content, media_url=media_url)

