# Stock-Django-Api

Backend part for full stack web development Flipr Hackathon 5.0

## Getting Started

Clone this repo to your local machine, setup a virtual enviroment(also activate it) and then follow the installation steps inside the project directory.
It's not interconnetec with its react frontend, so you have to run that on another server Frontend link-> https://github.com/GAUTAMSAHARAN/stock_frontend

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
pip  install -r requirements.txt
```

And change setting for database in settings.py (inside the api folder), also create a database of name stock in mysql in your local machine.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stock',
        'USER': 'your mysql user',
        'PASSWORD': 'password for that user',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '8000',
    }
}
```
Then run
``` 
python manage.py migrate
```
Then 
```
python manage.py runserver
```
If some error occur console will tell you, otherwise your project is up and running.

## Data Import
I added csv file of data, so if you are using mysql you can use phpmyadmin to import data from csv to your database.

### Steps to import data 

First select the table you want to update in phpmyadmin

Then
```
Browse your file, choose format = 'CSV USING LOAD DATA'
```
Then change from this
```
Columns separated with: ;  ->  Columns separated with: ,
```
Then select checkbox in phpmyadmin
```
Use LOCAL keyword 
```
That's all now you are good to go.


