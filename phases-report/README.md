# History Reports

This sample produces a report by querying the history of each incident,
and counting the time between phase-change events in that history.

## Pre-Requisites

Python, with the 'resilient' and 'openpyxl' modules installed.  Install these with pip:

    pip install -r requirements.txt

Parameters for the connection to Resilient can be specified on the
command line, or using a configuration file.
An example configuration file is provided (`app.config.example`).
The configuration file is found by
* the path indicated by environment variable `APP_CONFIF_FILE`, or
* `app.config` in the current directory, or
* `app.config` in `~/.resilient`.

## Usage

    python phases_report.py [--since 2015-01-31]

The result is a CSV file with one row per incident, with a column
for each phase that shows the number of hours the incident was (or is)
active in that phase.

Connection parameters are specified in `report.config` and can be
overridden with command-line options if necessary.
