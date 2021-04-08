python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip freeze > requirements.txt
set FLASK_APP=app
set FLASK_DEBUG=1
flask run