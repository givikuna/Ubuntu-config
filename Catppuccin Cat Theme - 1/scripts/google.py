import webbrowser

query: str = input('search: ')
newurl: str = "https://www.google.com/search?q=" + query.strip().replace('\n', ' ').replace('\t', ' ').replace(' ', '+')

webbrowser.open(newurl)
