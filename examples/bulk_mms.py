from autosms import AutoSMS

bot = AutoSMS("ABCD123", "321DCBA")
my_file = "https://example.com/image.png"
users = ["+8734562190", "+4743210963", "+1277400082", "+1673992104"]
bot.send_multi_mms("+1234567890", users, "Hakuna-Matata", my_file)