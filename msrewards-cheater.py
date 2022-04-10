import platform, pyautogui, time, random

# Set the base URL to be concatenated with a search word
baseurl = "https://www.bing.com/search?q="

# Figure out the host system to use the correct keyboard shortcuts
os = platform.system()
if os == 'Darwin':
    metakey = 'command' # MacOS
elif os == 'Windows':
    metakey = 'win' # Windows
# else:
    # Not sure how to do this for Linux yet

# Set the meta key for the appropriate operating system
metakey = "command"

# Open the Edge browser
pyautogui.hotkey(metakey, 'space', interval=0.05)
pyautogui.typewrite('edge')
pyautogui.press('enter')

time.sleep(10) # Give time for the browser to load

for i in range(4):
    for j in range(8):
        with open("words.txt", "r", encoding="utf-8") as file:
            allText = file.read()
            words = allText.split()
            word = random.choice(words)
            url = baseurl + word

        # Open the URL in a new tab
        pyautogui.hotkey(metakey, 't', interval=0.05)
        pyautogui.typewrite(url)
        pyautogui.press('enter')

        time.sleep(1.5) # Give time for the page to load

    time.sleep(2)

    for j in range(8):
        pyautogui.hotkey(metakey, 'w', interval=0.05)

# Close Microsoft Edge
pyautogui.hotkey(metakey, 'shift', 'w', interval=0.05)
pyautogui.hotkey(metakey, 'q', interval=0.05)