import os

contact = input("Enter contact name: ")
body = input("Enter message: ")
cmd = "osascript -e 'tell application \"Messages\" to send \""+str(body)+"\" to buddy \""+str(contact)+"\"\'"

os.system(cmd)

