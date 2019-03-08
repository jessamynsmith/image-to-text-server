# auto-scribe-backend

Django application providing an API to extract text from images.


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/auto-scribe-backend.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv auto-scribe-backend --python=/path/to/python3
    pip install -r requirements.txt

Set up db:

    python manage.py migrate
    
Run server:

    python manage.py runserver
    
Test API

    curl -X POST -F 'data=@path/to/local/file' http://127.0.0.1:8000/api/v1/ocr/
    
    
### Deployment

This project is set up for deployment to Heroku.

Make a new Heroku app, and add the following addons:

    Heroku Postgres

Add Heroku buildpacks:

    heroku buildpacks:set https://github.com/jessamynsmith/heroku-buildpack-apt -i 1
    heroku buildpacks:set heroku/python -i 2
    
    
    heroku buildpacks:set https://github.com/matteotiziano/heroku-buildpack-tesseract.git -i 3
