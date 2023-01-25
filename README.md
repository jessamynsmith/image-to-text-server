# image-to-text-server

Django application providing an API to extract text from images.


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/image-to-text-server.git

System dependencies:

    brew install tesseract

Create a virtualenv using Python 3.8 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX).

    python 3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    # If you have issues with ssl on mac:
    LDFLAGS="-L/usr/local/opt/openssl/lib" CPPFLAGS="-I/usr/local/opt/openssl/include" pip install -r requirements.txt

Set up db:

    python manage.py migrate
    
Copy .env.sample into .env and set values as needed.
    
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
    