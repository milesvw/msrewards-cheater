import webbrowser, random, time

# Create a URL that searches Bing for a random word picked from a wordlist
def url():
    with open("words.txt", "r", encoding="utf-8") as file:
        allText = file.read()
        words = allText.split()
        word = random.choice(words)

        # Set the base URL to be concatenated with a search word
        baseurl = "https://www.bing.com/search?q="

        url = baseurl + word
        return url

# Open tabs searching Bing
for i in range(5):

    # Open the URL in a new tab in the browser
    webbrowser.open(url())

    # Give time for the page to load
    time.sleep(1)