# AutoSMS
## Efficient, easy to use Python class/package to send worldwide SMS using Twilio.

Import this class to your project to send bulk or individual SMS or MMS messages.
Pass your own Twilio account credentials while making an instance of this class.

```
Start connection to the Twilio server.
account_sid = Twilio account SID.
auth_token = Twilio auth token.
```

```
reconnect() method.
Establish a new Twilio server connection using new credentials.
account_sid = Twilio account SID.
auth_token = Twilio auth token.
```

```
send_sms() method.
Send an SMS message.
sender = From mobile phone, alpha-numeric ID, or shortcode.
receiver = To mobile phone.
content = Plain/text message.
```

```
send_multi_sms() method.
Send a bulk SMS campaign.
sender = From mobile phone, alpha-numeric ID, or shortcode.
receivers = To mobile phone numbers array.
content = Plain/text message.
```

```
send_mms() method.
Send an MMS message.
sender = From mobile phone, alpha-numeric ID, or shortcode.
receiver = To mobile phone.
content = Plain/text message.
media_url = MMS media attachment URL.
```

```
send_multi_sms() method.
Send a bulk MMS campaign.
sender = From mobile phone, alpha-numeric ID, or shortcode.
receivers = To mobile phone numbers array.
content = Plain/text message.
media_url = MMS media attachment URL.
```

```
Basic SMS example.
bot = AutoSMS("ABCD123", "321DCBA")
bot.send_sms("+1234567890", "+0987654321", "Hakuna-Matata")
```

```
Basic MMS example.
bot = AutoSMS("ABCD123", "321DCBA")
my_file = "https://example.com/image.png"
bot.send_mms("+1234567890", "+0987654321", "Hakuna-Matata", my_file)
```

```
Bulk MMS example.
bot = AutoSMS("ABCD123", "321DCBA")
my_file = "https://example.com/image.png"
users = ["+8734562190", "+4743210963", "+1277400082", "+1673992104"]
bot.send_multi_mms("+1234567890", users, "Hakuna-Matata", my_file)
```

### Imad Elakhal | Smartest Programmer Ever Lived.
