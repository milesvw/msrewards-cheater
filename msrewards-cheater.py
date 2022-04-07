import webbrowser, time
from random_word import RandomWords
r = RandomWords()

# Create a URL that searches Bing for a random word picked from a wordlist
def url():

    # Pick a random word
    word = r.get_random_word()

    # Set the base URL to be concatenated with a search word
    baseurl = "https://www.bing.com/search?q="

    url = baseurl + word

    return url

# Open tabs searching Bing
for i in range(4):

    # Open the URL in a new tab in the browser
    webbrowser.open(url())

    # Give time for the page to load
    time.sleep(2)