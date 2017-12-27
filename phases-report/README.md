# History Reports

This is an example of a simple Python application using the Resilient REST API.

It produces a spreadsheet report of the time spent in each phase of an incident,
by querying the incident history, and counting the time between phase-change events.

## Pre-Requisites

* Python version 2.7.3 or later, or 3.4 or later
* Python 'resilient' and 'openpyxl' modules installed.  Install these with pip:
```
    pip install -r requirements.txt
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
    python phases_report.py [--since 2015-01-31]
```
The result is a CSV file with one row per incident, with a column
for each phase that shows the number of hours the incident was (or is)
active in that phase.
