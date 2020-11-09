import requests
for letter in 'abcdefghijklmnopqrstuvwxyz':
        for letter2 in 'abcdefghijklmnopqrstuvwxyz':
            myword = letter+letter2
            url = f'https://{myword}.xss.ht'
            page = requests.get(url)
            print(myword,page.status_code)