# Creating an incident with the REST API

This directory contains two simple example Python application using the Resilient REST API,
to demonstrate creating an incident and setting its properties.

## Pre-Requisites

* Python version 2.7.3 or later, or 3.4 or later
* Python 'resilient' module installed.  Install this with pip:
```
    pip install --upgrade resilient
```
Parameters for the connection to Resilient can be specified on the
command line, or using a configuration file.
An example configuration file is provided (`app.config.example`).
The configuration file is found by
* the path indicated by environment variable `APP_CONFIG_FILE`, or
* `app.config` in the current directory, or
* `app.config` in `~/.resilient`.

## Usage
```
    python create_incident.py -n <name> -d <description> -t Malware
```
Shows how to create a basic incident, setting its name, description and (optionally)
incident type(s).  The `discovered_date` is set to the current time.
Note: if you have additional "required" fields, this will not be able to create an incident!

```
    python create_with_values.py -n <name> -d <description> -t Malware -c cyber_kill_chain=Installation custom1=value1 custom2=value2
```
Shows how to create an incident, specifying values for custom fields.
The incident name, description and (optional) incident type(s) are specified as before.
Additional parameters to "--custom" or "-c" specify the API names of custom fields, and
values that will be set for those fields.  These values are assumed to be string or 'select' values.


