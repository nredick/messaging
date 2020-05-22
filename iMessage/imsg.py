import os

contact = input("Enter contact name: ")
body = input("Enter message: ")
cmd = f"osascript -e 'tell application \"Messages\" to send \"{body}\" to buddy \"{contact}\"'"

os.system(cmd)

