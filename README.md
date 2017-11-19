* Clone the repository
* Download the `client_secret.json` from Google Developers Console
* Put `client_secret.json` in project dir
* Create Google Sheet and give access in Sharing Options
* Change permissions of script files to not readable from web:
`chmod -R 700 client_secret.json requirements.txt README.md __pycache__/ main
.py .git* export.py`
* Run run.py
