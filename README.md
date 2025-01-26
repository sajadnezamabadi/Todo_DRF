## Requirements
- [Python]
- [pip]
- [virtualenv]

## Installation
- ```bash
git clone https://github.com/username/repo-name.git
cd repo-name

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/
