from autosms import AutoSMS

bot = AutoSMS("ABCD123", "321DCBA")
my_file = "https://example.com/image.png"
bot.send_mms("+1234567890", "+0987654321", "Hakuna-Matata", my_file)