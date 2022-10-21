from random import *

films = []
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
        print('Bot stoped its work.')
        break
    elif command == '/films':
        print('This is current film list: ')
        print(films)
    elif command == '/add':
        s = input('Enter the film name:')
        films.append(s)
        print('Film was successfully add in colection.')
    elif command == '/help':
        print('Manual:')
    elif command == '/del':
        s = input('Enter the film name:')
        if s in films:
            films.remove(s)
            print('Film was successfully deleted.')
        else:
            print('There is no such film in collection')



    else:
        print('Not identified command. Please learn again /help')
