#!/usr/bin/env python
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import resilient
import json
import os


class ExportArgumentParser(resilient.ArgumentParser):
    def __init__(self, config_file=None):
        super(ExportArgumentParser, self).__init__(config_file=config_file)

        self.add_argument('first_json_file',
                          help="The first JSON filename.")

        self.add_argument('second_json_file',
                          help="The second JSON filename.")

        self.add_argument('output_json_file',
                          help="The output JSON filename.")


def get_incidents_from_file(filename):
    if os.path.isfile(filename):
        incidents = []
        with open(filename) as f:
            for line in f:
                try:
                    line_json = json.loads(line)
                except ValueError:
                    raise Exception(("Parsing file {} for JSON failed.".format(filename)))

                if line_json.get("incident") is None:
                    raise Exception("Invalid JSON in file {}. Could not locate incident.".format(filename))

                incidents.append(line_json.get("incident"))

        return incidents
    else:
        raise Exception(("File {} not found.".format(filename)))

    return None


def main():
    parser = ExportArgumentParser(config_file=resilient.get_config_file())
    opts = parser.parse_args()

    first_incidents = get_incidents_from_file(opts.get("first_json_file"))
    second_incidents_array = get_incidents_from_file(opts.get("second_json_file"))

    if first_incidents is None or second_incidents_array is None:
        raise Exception("Invalid file provided.")

    if os.path.isfile(opts.get("output_json_file")):
        os.remove(opts.get("output_json_file"))

    second_incidents = []

    for incident in second_incidents_array:
        incident_id = incident.get("id")
        if incident_id is not None:
            second_incidents.append(incident_id)
            with open(opts.get("output_json_file"), "a") as outfile:
                json.dump({"incident": incident}, outfile)
                outfile.write("\n")

    for incident in first_incidents:
        incident_id = incident.get("id")
        # if valid incident
        if incident_id is None:
            continue

        # if the incident already exists, we don't want to add it
        if incident_id not in second_incidents:
            with open(opts.get("output_json_file"), "a") as outfile:
                json.dump({"incident": incident}, outfile)
                outfile.write("\n")

    print("Successfully merged JSON files into {}.".format(opts.get("output_json_file")))


if __name__ == "__main__":
    main()
