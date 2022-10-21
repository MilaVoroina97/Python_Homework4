from random import *
import json
films = []
def save():
    with open('films.json','w',encoding='utf-8') as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print('Our films collection was successfully saved in file films.json')

def load():
    with open('films.json','r',encoding='utf-8') as fh:
        films = json.load(fh)
    print('Film collection was successfully upload')
try:
    with open('films.json','r',encoding='utf-8') as fh:
        films = json.load(fh)
    print('Film collection was successfully upload')

except:
    films.append('Matricha')
    films.append('Solaris')
    films.append('Lord of the rings')
    films.append('Texas')
    films.append('Santa Barbora')



while True:
    command = input('Enter the comand: ')
    if command == '/start':
        print('Film list start to work')
    elif command == "/stop":
        save()
        print('Bot stoped its work.')
        break
    elif command == '/films':
        print('This is current film list: ')
        print(films)
    elif command == '/add':
        s = input('Enter the film name:')
        if s in films:
            print('Film already in your collection')
        else:
            films.append(s)
            print('Film was successfully add in colection.')
    elif command == '/all':
        print('This is your current film collection: ')
        print(films)
    elif command == '/help':
        print('Manual:')
    elif command == '/del':
        s = input('Enter the film name:')
        try:
            films.remove(s)
            print('Film was successfully deleted.')
        except:
            print('There is no such film in collection')
    elif command == '/random':
        # rnd = randint(0,len(films)-1)
        # print('We recommend you to watch film: '+ films[rnd])
        print('We recommend you to watch:' + choice(films))
    elif command == '/save':
        save()
    elif command == '/load':
        with open('films.json','r',encoding='utf-8') as fh:
            films = json.load(fh)
        print('Film collection was successfully upload')

    else:
        print('Not identified command. Please learn again /help')
