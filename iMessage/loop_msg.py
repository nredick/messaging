import os
import csv
import time

contact = input("Enter contact name: ")

with open('realdonaldtrump-tweets.csv') as f:
    #reader = csv.reader(f)
    data = [next(csv.reader(f)) for x in range(40)]
    for row in data:
        body = f"@{row[2]}\n{row[3]}"
        cmd = f"osascript -e 'tell application \"Messages\" to send \"{body}\" to buddy \"{contact}\"'"
        os.system(cmd)
        time.sleep(1.5)
