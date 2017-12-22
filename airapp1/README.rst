Airapp1
=========

The index page has a list of UK air pollution monitoring sites. On loading pages for the individual sites, graphs of annual mean pariculate matter concentrations are generated. 


Install
=========

Dependencies:

 - Python 3

   - https://www.python.org

 - PIP (Python package manager)

   - https://pypi.python.org/pypi/pip


Configure and run server:
------------------------

After cloning or downloading project files, run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt

    python manage.py runserver 
    
The app can then be accessed at: http://localhost:8000/sites/
