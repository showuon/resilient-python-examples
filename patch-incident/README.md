# Using the PATCH API

This directory contains two simple example Python application using the Resilient REST API, to demonstrate use of the
PATCH method to update a Resilient incident, using the `patch()` and `patch_with_callback()` functions in Python. 

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
* the path indicated by environment variable `APP_CONFIF_FILE`, or
* `app.config` in the current directory, or
* `app.config` in `~/.resilient`.

## Usage
```
    python patch_width_overwrite.py --incid <id> --desc <new_description>
```
Shows how to update the description of the specified incident using the PATCH method.

```
    python patch_width_handler.py --incid <id> --itype <incident_type>
```
Shows how to update the Incident Type field of the specified incident, with "smart" conflict handling.

