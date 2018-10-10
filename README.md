# conference_system
A mini project under the course of 'Software Engineering' to learn the documentation processes in the industry.

## Installation

1. Install Python and set up virtual environment 
```    
Install python 3.7
Run this command to create a virtual env : python3 -m venv myvenv
To make the terminal execute from the virtual env in Linux/OSX, execute this command : source  myvenv/bin/activate
If using Windows, execute this command : myvenv\Scripts\activate

```

2. Install rest of the dependencies :
```
python3 -m pip install --upgrade pip 
pip install -r requirements.txt
```

3. Install MySQL DBMS and create the database. 
```
CREATE DATABASE conference_system;

create new user using :

CREATE USER 'cs_root'@'localhost' IDENTIFIED BY 'group_123';
GRANT ALL ON conference_system.* TO 'cs_root'@'localhost';

```

4. Run the following commands in the project folder
```
source myvenv/bin/activate or myvenv\Scripts\activate
python manage.py makemigrations
python manage.py migrate
python manage.py runscript initialize
python manage.py runserver

```
