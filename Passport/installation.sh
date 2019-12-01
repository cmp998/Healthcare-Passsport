#!/bin/sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip install flask
pip install flask_sqlalchemy
pip install flask_migrate
pip install flask_bootstrap
pip install flask_wtf
echo "---------------------------------------------------------------"
echo "Successfully installed all depedencies for Healthcare Passport."
echo "Use flask run to start the database and the website."
echo "---------------------------------------------------------------"