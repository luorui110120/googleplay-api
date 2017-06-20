# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_US" # can be en_US, fr_FR, ...
ANDROID_ID      = "66cff1602d2f1825" # "3bcff1602d2f1825"
GOOGLE_LOGIN    = "xxxxxxx@gmail.com" # "username@gmail.com"
GOOGLE_PASSWORD = "passwd"
AUTH_TOKEN      = "xxxxdLBu2lkcKd2IeMRTqQy_GOFZ9SnCzZXTtzxd0VVDUO6S596rLCsvDp6R7zWVsWKh9A." # "yyyyyyyyy"

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

