# Recogito Similarity Scan

This repository contains scripts to experiment with different approaches to 
establish 'similarity' between documents in Recogito. This work is part of
the Mellon-funded work plan for the Pelagios 7 project, specifically the 
work item 'enhancing discovery'.

## Ruby Scripts

Proof-of-concept scripts in the `ruby` folder. Run `bundle install` to install 
dependencies before running the scripts. All scripts assume an instance
of Recogito to be running locally.

You may need to modify settings within the script code, according to your 
own environment. 

## Python Scripts

`pip install textdistance[JaroWinkler]`

`pip install elasticsearch==5.5.3`

Create a copy of `config.ini.template` named `config.ini` and modify according to your DB settings.

## Notes

- Jaro-Winkler comparison is twice as fast in Ruby than in Python

