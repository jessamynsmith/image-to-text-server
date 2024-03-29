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

##### Elastic Beanstalk.

Initialize the repository:

    eb init -p python-3.6 image-to-text
    
Set up SSH:

    eb init

Create environment:
    
    eb create image-to-text-env

##### Ubuntu

Ssh into Ubuntu server.

Install native dependencies:

    sudo apt install libpng-dev libtesseract-dev libtesseract-ocr redis-server

Get source code:

    git clone git@github.com:jessamynsmith/image-to-text-server.git image2text

Copy gunicorn service file into system folder:

    sudo cp config/image2text.service /etc/systemd/system/image2text.service

After service config change:

    sudo systemctl daemon-reload

Restart image2text service:

    sudo systemctl restart image2text

View gunicorn logs:

    sudo journalctl -u image2text.service --no-pager -f

View Django logs:

    tail -f /home/django/log/error_image2text.log 

Copy nginx config into nginx directory and create symlink:

    sudo cp config/image2text /etc/nginx/sites-available/image2text
    sudo ln -s /etc/nginx/sites-available/image2text /etc/nginx/sites-enabled/image2text

Set up SSL:

    sudo certbot --nginx -d image2text.jessamynsmith.ca

Restart nginx:

    sudo systemctl restart nginx
