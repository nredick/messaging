# Simple SMS messaging script!
Bare-bones script for sending SMS messages in the US & Canada.


## Deploying the Script

The script runs locally from the terminal/command line. 

To utilize the script, clone the repository to your local machine. Install all packages 
from requirements.txt. Then, create a file named 'sms_config.py' with two global variables 'email' and 'secret':

Works with a gmail address. You will need to create a 16-digit Google 'App Password' to use instead of your normal gmail password for the 'secret' variable. More info at https://support.google.com/accounts/answer/185833
```
pip install -r requirements.txt
python sms_msg.py
```

## Repository Organization

This repository contains requirement.txt and the messaging script. 

- sms_msg.py 

- requirements.txt

