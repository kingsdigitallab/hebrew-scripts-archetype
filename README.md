# hebrew-scripts-archetype
Archetype instance for the Hebrew Scripts research project
https://github.com/kingsdigitallab/hebrew-scripts-archetype

# Pre requisites

* linux environment (ubuntu/debian)
* python2, with pip and virtualenv
* postgresql 9+
* git
* nodejs > npm > lessc, typescript

# Local deployment

## pull code

```
cd AROOT # AROOT is the root path where you'll install archetype
git clone -b develop git@github.com:kcl-ddh/digipal.git digipal_github
git clone git@github.com:kingsdigitallab/hebrew-scripts-archetype.git
```

## project folders

```
cd AROOT
cd hebrew-scripts-archetype
ln -s ../digipal_github/digipal
ln -s ../digipal_github/digipal_text
ln -s ../digipal_github/build
```

## pythonvirtual environment
```
cd AROOT
python2 -m virtualenv venv
. venv/bin/activate
pip install -r hebrew-scripts-archetype/build/requirements.txt
```

## database
```
sudo su postgres
psql
    create user app_hebrew_scripts_archetype with password 'XXX';
    \q
createdb -E 'utf-8' -T template0 -O app_hebrew_scripts_archetype app_hebrew_scripts_archetype_lcl
```

## local_settings.py

local_settings.py SHOULD NOT be part of github repo, it is reserved for any sensitive information like database connections, address to image server, etc. and for anything specific to a particular instance of your site.

settings_hebscripts.py contains your project customisations, anything which is not sensitive and is shared between all instances (local, development, staging, live) of the projects.

## create db tables
`pipenv shell`
`./manage.py migrate`

# run server
`./manage.py runserver`

# browse your site

open browser as http://localhost:8000/
