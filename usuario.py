#!C:\AnacondaInstal\python.exe

print('Content-type:text/html\n\n')

import cgi
import cgitb

from pandas.core.indexes.base import ensure_index; 
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

usuario = form.getvalue("usuario")
extensao = form.getvalue("extensao")

tweets = []
busca = tweepy.Cursor(api.user_timeline,id=usuario).items(4)


for tweet in busca:
    tweet = tweet._json
    tweets.append(tweet)

df = pd.DataFrame(tweets)

if extensao == 'csv':
    df.to_csv('resultUser.csv', sep=';')
elif extensao == 'json':
    df.to_json('resultUser.json')
elif extensao == 'excel':
    df.to_excel('resultUser.xlsx')
else:
    print("Nenhuma extensão selecionada")
        

print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("</head>")
print("<body>")
print ("<h2> Pesquisa:</h2>")
print("<a href=\"http://localhost:80/python/projeto/resultUser.xlsx\">Baixar arquivo </a>")
print("<br/>")
print ("<h2><a href=\"http://localhost/python/projeto/html.html\">Voltar a pagina de pesquisa</a></h2>")
print("</body>")
print("</html>")
