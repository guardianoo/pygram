from instagrapi import Client
import json
import requests

client = Client()

client.login(  'levimendes.agro' , 'XXl3visXX'  )

url = 'https://www.instagram.com/p/CiNIUH3t2tB/'

post_id = client.media_id(client.media_pk_from_url(url))

word_keys = ['valor', 'preço', 'preco']

comments = client.media_comments(post_id )

client.media_comment(post_id, 'Qual o preço da espátula?')

for comment in comments:
    
    if word_keys in comment.text.lower():
        print(comment)

print(peguei['full_name'].split()[0])

print(type(comments[-1].user))



post_rec = requests.get(url)
post_rec = post_rec.json()

print(post_rec)
post.scrape()

comments = post.get_recent_comments()

for comment in comments:
    print(f'{comment.username} => {comment.text}')

print("teste de upload")

print('atualização')
