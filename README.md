# Treachery app #

[![Join the chat at https://gitter.im/TreacheryLarp/downtime](https://badges.gitter.im/TreacheryLarp/downtime.svg)](https://gitter.im/TreacheryLarp/downtime?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This app handles management of the Treachery downtime system. This app is optimised for Dokku.

## Installation ##
1. Create a venv `python -m venv venv`
2. Set environ `source venv/bin/activate`
3. Install dependencies `python -m pip install -r requirements.txt`
4. Migrate database
5. Create superuser
6. Run server `python manage.py runserver`

### Dependencies ###
See the requirements.txt and runtime.txt files for dependencies.
