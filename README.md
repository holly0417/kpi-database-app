requires node to install vue, quasar, js, etc.
uses vue with quasar framework for frontend. 
it is an SPA, with the frontend served by the Django backend server. 

# setup requirements
(what is not in this repo but you need to add for this to run)

in another folder under root, files  `settings.py` and `urls.py` should set up the directory to static files as well as the URL setup for SPA.

under `kpi_app` should be a folder `classifications` where static files of the current GICS or ICIS categorization references are. 
I cleaned this manually so that it can be used as a reference for `models.py` to create the structure of the database. 
This may differ based on your own needs, so it is not included in this repo. 