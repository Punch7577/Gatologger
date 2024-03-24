# Keylogger with Discord Webhook *BETA*

## ⌨ A simple keylogger which logs keys into a text file and then sends it to a Discord server of your liking via its webhook.

This keylogger is a software which is easy to use, and effective. It is supposed to do as intended. It sends logged keys to a Discord server. You can use the code by itself, or you can fork this repo for whatever you would like.
*Make sure you have the requirements installed before using the keylogger. They are in the requirements file.*


*Disclaimer: This is open source software which is meant for informational purposes only. The creator does not condone or encourage any wrongdoings with this code. The creator is not responsible for any criminal activity done with this code.*
*It is strongly encouraged for users of this code to look at the laws and regulations regarding the use of software in their area, as well as the terms of service for respective third party applications and websites the user might use this code with or for.*
*Please use this code responsibly.*

## 👏 This Keylogger might be useful for the following things:

1. Extracting string data and putting it into a Discord text channel.
2. Working with other software for Discord.
3. Testing Discord Webhooks and troubleshooting them.
4. For fun of course!

## 💻 How to set up the keylogger

1. Access the code.
2. Input the Discord webhook of the text channel which you want to send logged keys to in the url variable in line #10.
3. Create a new text file and give it a name of your liking.
4. Go into the code again, and replace every 'txt' in every open() function with the name of your text file (they are on lines: #18, #37, #49, and #69).
5. Scroll down to the JSON code on line #48. Set up the Avatar of the bot, the bot's username, what you want the bot to say when it sends the keys, and the color (the avatar and color are optional. Do not change the description though).
6. Done! You can use the keylogger by running Keylogger.py by double clicking, or by using it with a command line.

## ❓ Troubleshooting

"The keylogger does not work when I double click the file".

Note that this is a common problem that a lot of people experience, and it is not related to the keylogger. Try seeing if the Python interpreter is set up to run the code properly. You can see the interpreter by going in a command 
line (CMD on Windows, terminal on MAC/Linux) and typing in 'python --version'. You can also then run 'which python' on MAC/Linux, or 'where python' on Windows to see the path of the interpreter being used on the command line. You can check if Python needs
to update. If so, run the update.


"The keylogger will not work".

Double check to see if you set up the keylogger properly. If you did, then that could potentially be an issue with Python. Check if it needs to update, or if you have it installed on your system properly. You could also try testing the code on a different website
or application to see if it works there. If this does not work, then see if the settings on your computer are blocking it from working. Also check the OS you are using, and see if it might be compatible with your system. If it still does not work, then
try seeing if the keys are being appended into the text file. If they are not, then try creating your own text file and replacing every 'txt.txt' in the code with the name of your text file.


"The backspace button does not work properly".

Yes, that is a problem that I am aware of. This is the BETA version of the keylogger, and I plan to fully resolve the issue in the final build.


"The logged keys do not get sent to the discord text channel even though I put in a webhook".

Check whether or not your webhook works, or try another webhook. Realistically, the HTTP response code you should be getting is 204. 



If there are any other problems that I did not address, you can try to contact me for help, or get some community feedback.

## ✍ Last few things

If you like this software, then you can give me a star. Or don't.

Thank you for checking out my keylogger!
