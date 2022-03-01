import webbrowser, random, time

# Set the base URL to be concatenated with a search word
baseurl = "https://www.bing.com/search?q="

# Open 30 tabs searching Bing with a different word each time
for i in range(30):
    with open("words.txt", "r", encoding="utf-8") as file:
        allText = file.read()
        words = allText.split()
        word = random.choice(words)
        url = baseurl + word
        
        # Open the URL in a new tab in the browser
        webbrowser.open(url)

	    # Give time for the page to load
        time.sleep(1)