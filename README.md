# Django and Python X Youtube API

A basic video search app with Django and Youtube API.

To get started clone the repository into an existing directory in your computer.

```
git clone https://github.com/Nepul321/Django-and-Python-with-Youtube-API .
```

NOTES : 

 - On mac `python` command should be replaced by `python3` and `pip` should be replaced by `pip3`
 - `source Scripts/activate` command is a bash command on windows powershell it is `./Scripts/ activate` and on cmd it is `Scripts\activate`
  - On mac and linux `source Scripts/activate` should be `source bin/activate`

Then create a virtual environment, activate it and install requirements.

```
python -m venv .
source Scripts/activate
pip install -r requirements.txt
```

Next go to the src directory and create a dotenv file and configure the following variables,

```
SECRET_KEY=<your-secret-key>
YOUTUBE_API_KEY=<youryoutubeapikey>
```

Then migrate the databases and runserver.

```
python manage.py migrate
python manage.py runserver
```

Go to http://localhost:8000/ or http://127.0.0.1:8000/ to see the project.