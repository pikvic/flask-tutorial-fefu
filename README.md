# Crazy Captcha

Tutorial project using digit recognition via neural networks. Try to solve out Crazy Captcha!

# Installation

1. Clone this repo.
2. In project folder run `python -m venv venv` command. This will create virtual environment with local clean python installation.
3. Activate created virtual environment using `venv\Scripts\activate` command on Windows or `source ./venv/Scripts/activate` on Linux or MacOS.
4. Run `pip install -r requirements.txt` command to install all necessary dependencies.
5. Run `set FLASK_APP=app.py` on Windows or `FLASK_APP=app.py` on Linux or MacOS.
6. Optionnaly run `set FLASK_ENV=development` or `FLASK_ENV=development` to enable debug mode and autorestart on source code changes on Windows or Linux and MacOS respectively.
7. Run `flask run` command to start development server.
8. Run `gunicorn app:app` to start production server.