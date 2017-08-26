# Users and Groups Report

This sample produces a report of all users and groups in the organization.

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

    python users_groups.py

The result is a spreadsheet (XLSX format) with two sheets:
* Users: listing all users, alphabetically, with their attributes;
* Groups, listing all groups, with their members.

