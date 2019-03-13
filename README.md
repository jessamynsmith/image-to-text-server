# image-to-text-server

Django application providing an API to extract text from images.


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/image-to-text-server.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv image-to-text-server --python=/path/to/python3
    pip install -r requirements.txt

Set up db:

    python manage.py migrate
    
Set environment variables, e.g.

    export DJANGO_DEBUG=1
    export DJANGO_ENABLE_SSL=0
    
Run server:

    python manage.py runserver
    
Test API

    curl -vk -X POST -F 'data=@path/to/local/file' http://127.0.0.1:8000/api/v1/ocr/data/
    
    curl -vk -X POST -F 'url=<image_url>' http://127.0.0.1:8000/api/v1/ocr/url/
    
### Deployment

This project is set up for deployment to Elastic Beanstalk.

Initialize the repository:

    eb init -p python-3.6 image-to-text
    
Set up SSH:

    eb init

Create environment:
    
    eb create image-to-text-env
    