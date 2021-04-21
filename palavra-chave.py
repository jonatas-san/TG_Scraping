#!C:\AnacondaInstal\python.exe

print('Content-type:text/html\n\n')

import cgi
import cgitb;
cgitb.enable()
import os
import tweepy
import pandas as pd

form = cgi.FieldStorage()

consumer_key='gz3BgvgTtYi9cFsq6xsd0dco0'
consumer_secret= 'dCATgD0m3Ugo190rGQHyWL9o74mgGEgBgOitPbiAMiX9D6K3fn'

access_token='1315133403147239424-7Eu936LHrOCgE8Kju7qI7oIFPjApus'
access_token_secret='w9vrQhE4gCuoh7UKlzl89W8oOwm8j003ZVd81lwuWN1Cy'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


plchave = form.getvalue("plchave")

tweets = []
busca = tweepy.Cursor(api.search, 
          plchave,
          dtinipl = form.getvalue("dtinipl"),
          dtfimpl = form.getvalue("dtfimpl"),
          ).items(10)

for tweet in busca:
    tweet = tweet._json
    tweets.append(tweet)

df = pd.DataFrame(tweets)

df.to_csv('ResultKeyWord.csv', sep=';')


print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("</head>")
print("<body>")
print ("<h2> Pesquisa:</h2>")
print("<a href=\"http://localhost:80/python/projeto/ResultKeyWord.csv\">Baixar arquivo </a>")
print("<br/>")
print ("<h2><a href=\"http://localhost/python/projeto/html.html\">Voltar a pagina de pesquisa</a></h2>")

print("</body>")
print("</html>")

# df.to_json('json_rec.json', orient="records")
# df.to_json('json_index.json', orient="index")
# df.to_json('json_columns.json', orient="columns")