#!C:\AnacondaInstal\python.exe

print('Content-type:text/html\n\n')

import cgi
import cgitb
import requests
from pandas.core.indexes.base import ensure_index; 
cgitb.enable()
import os
import tweepy
import pandas as pd

form = cgi.FieldStorage()

consumer_key='gz3BgvgTtYi9cFsq6xsd0dco0'
consumer_secret= 'dCATgD0m3Ugo190rGQHyWL9o74mgGEgBgOitPbiAMiX9D6K3fn'

access_token = '1315133403147239424-7Eu936LHrOCgE8Kju7qI7oIFPjApus'
access_token_secret='w9vrQhE4gCuoh7UKlzl89W8oOwm8j003ZVd81lwuWN1Cy'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

usuario = form.getvalue("usuario")
extensao = form.getvalue("extensao")
geocode = form.getvalue("Geocode")
limitpl = form.getvalue("limitpl")

'''
if geocode == "BR":
    geo =  '-14.235004,-51.925280,8514876km'
elif geocode == "US":
    geo='37.0902,-95.7129,9834000km'
'''

tweets = []
busca = tweepy.Cursor(api.user_timeline,id=usuario).items(int(limitpl))


for tweet in busca:
    tweet = tweet._json
    tweets.append(tweet)

df = pd.DataFrame(tweets)

response = requests.get("http://localhost/python/projeto/html.html")

if extensao == 'csv':
    df.to_csv('resultUser.csv', sep=';')

    print("<html>")
    print("<head>")
    print("<meta charset=\"utf-8\">")
    print("<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">")
    print("</head>")
    print("<body>")
    print ("<h2> Pesquisa:</h2>")
    print("<h1 id=\"baixar\"><a href=\"http://localhost:80/python/projeto/resultUser.csv\"><button>Baixar arquivo</button></a></h1>")
    print("<br/>")
    print ("<h2 id=\"voltarhome\"><a href=\"http://localhost/python/projeto/html.html\">Voltar a pagina de pesquisa</a></h2>")
    print("</body>")
    print("</html>")

elif extensao == 'json':
    df.to_json('resultUser.json')
    print("<html>")
    print("<head>")
    print("<meta charset=\"utf-8\">")
    print("<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">")
    print("</head>")
    print("<body>")
    print ("<h2> Pesquisa:</h2>")
    print("<h1 id=\"baixar\"><a href=\"http://localhost:80/python/projeto/resultUser.json\"><button>Baixar arquivo</button></a></h1>")
    print("<br/>")
    print ("<h2 id=\"voltarhome\"><a href=\"http://localhost/python/projeto/html.html\">Voltar a pagina de pesquisa</a></h2>")
    print("</body>")
    print("</html>")

elif extensao == 'excel':
    df.to_excel('resultUser.xlsx')
    print("<html>")
    print("<head>")
    print("<meta charset=\"utf-8\">")
    print("<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">")
    print("</head>")
    print("<body>")
    print ("<h2> Pesquisa:</h2>")
    print("<h1 id=\"baixar\"><a href=\"http://localhost:80/python/projeto/resultUser.xlsx\"><button>Baixar arquivo</button></a></h1>")
    print("<br/>")
    print ("<h2 id=\"voltarhome\"><a href=\"http://localhost/python/projeto/html.html\">Voltar a pagina de pesquisa</a></h2>")
    print("</body>")
    print("</html>")

else:
    print("Nenhuma extensão selecionada")