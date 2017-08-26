# -*- coding: utf-8 -*-

"""Action Module circuits component to add an incident manually"""

import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent
import resilient
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'multi_org_incident'


class AddIncidentComponent(ResilientComponent):
    """Adds an incident once a menu item is clicked"""

    # This component adds an incident once a manual action is clicked

    def __init__(self, opts):
        super(AddIncidentComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'addincident'
        self.channel = "actions." + self.options.get("queue", "addincident")

        # Read the configuration options that tell us how to connect to the second org
        self.to_org_name = self.options.get('to_org_name')
        self.to_org_address = self.options.get('to_org_address')
        self.to_org_username = self.options.get('to_org_username')
        self.to_org_password = self.options.get('to_org_password')
        self.to_org_verify_tls = self.options.get('verify')

        # The 'verify' option can be a path to a certificate file, or 'False' to disable all verification
        if str(self.to_org_verify_tls).lower() == "false":
            self.to_org_verify_tls = False

        if not all([self.to_org_name, self.to_org_address, self.to_org_username, self.to_org_password]):
            raise Exception("Required configuration options are missing.")

    @handler("escalate_incident_between_orgs")
    def _add_incident(self, event, *args, **kwargs):
        """Function to add an incident to another org."""

        # get information about the incident, such as its ID
        incident = event.message["incident"]
        inc_id = incident["id"]

        LOG.info("Connecting to alternate org...")
        resilient_client = resilient.SimpleClient(self.to_org_name,
                                                  self.to_org_address,
                                                  verify=self.to_org_verify_tls)

        LOG.info("Authenticating with alternate org...")
        resilient_client.connect(self.to_org_username,
                                 self.to_org_password)

        LOG.info("Creating new incident data...")
        # NOTE: The other organization is likely to have different schema from the originating org
        # (custom fields, and different valid values for 'select' fields).  Ensure that all required
        # fields are set in the new incident, and that copied values are mapped appropriately.
        new_incident = {'name': 'New Incident Copied From Other Org',
                        'description': 'Incident created from incident '+str(inc_id),
                        'discovered_date': incident['discovered_date']}

        LOG.info("Posting new incident to alternate org...")
        new_incident = resilient_client.post('/incidents', new_incident)

        LOG.info("Finished incident posting! New incident ID is %s", new_incident["id"])

        return "Incident Created"
    # end _add_incident
