# ApiDemo_Vacaciones

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework


# Si haces cmabios en la base de datos
python manage.py makemigrations
python manage.py migrate



# Run code
python manage.py runserver
