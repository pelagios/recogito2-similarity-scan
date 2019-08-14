# Recogito Similarity Scan

This repository contains scripts to experiment with approaches to establish 
'similarity' between documents in Recogito. This work is part of
the Mellon-funded work plan for the Pelagios 7 project, specifically the 
work item 'enhancing discovery'.

## Ruby Scripts

I did some first proof-of-concept scripts in Ruby (see `ruby` folder). 
Run `bundle install` to install dependencies before running the scripts.
All scripts assume an instance of Recogito to be running locally, but don't
write back to the DB.

There's no config file. You may need to modify settings within the script 
code directly, according to your own environment. 

## Python Scripts

Because Python is already set up on the [Recogito](https://recogito.pelagios.org) 
production server, I ported (and completed) the scripts to Python.

### Pre-requisites

The scripts have a few dependencies (and sub-dependencies) for database/index access 
and text processing: [SQLAlchemy](https://www.sqlalchemy.org/),
[elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/) and
[textdistance](https://pypi.org/project/textdistance/).

```
$ pip install sqlalchemy
$ pip install psycopg2  # used by SQLAlchemy
$ pip install textdistance[extras] 
$ pip install textdistance[JaroWinkler]
$ pip install elasticsearch==5.5.3 # 5.x required for Recogito - don't use newer ones!
```

Create a copy of `config.ini.template` named `config.ini` and modify according to your DB settings.

