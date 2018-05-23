#!/usr/bin/env python
#
"""
    APIC_stress_test.py

    Copyright (c) 2018 World Wide Technology, Inc.
    All rights reserved.

    Author: Joel W. King (joel.king@wwt.com)

    This program was written to help debug an issue with Application Policy Infrastructure Controller Version: 3.1(2o).

    Requirements:
        wget https://raw.githubusercontent.com/joelwking/ansible-aci/master/AnsibleACI.py

    to a directory where python can locate the file.

    Set environmental variables to provide input to the program.

    export ACI_USERNAME=kingjoe
    export ACI_PASSWORD=secret
    export ACI_HOST=aci-demo.sandbox.wwtatc.local
    export ACI_TENANT=tetration_policy_enforce

    Usage: python APIC_stress_test.py

    Linted with flake8

    [flake8]
    max-line-length = 160
    ignore = E402

"""
# Imports
import AnsibleACI
import os
import random
import time

# Constants
HOUR = 3600
OK = (200,)
STATE_OPTIONS = {'present': '', 'absent': 'status="deleted"'}
PREFIX = 'foo'
END = 300


def contract(apic=None, contract='foo123', tenant='bar', desired_state='absent'):
    """
        Formats the URL and XML to send to the APIC to create or delete a contract
    """
    response = '(...)'
    state = STATE_OPTIONS.get(desired_state)
    if state is None:
        print "Incorrect desired_state: %s" % state
        return

    # Create the XML and URL to send

    URI = '/api/mo/uni/tn-%s/brc-%s.xml' % (tenant, contract)
    apic.setgeneric_URL("%s://%s" + URI + "?rsp-subtree=modified")

    xml_template = '<vzBrCP  %s descr="%s" dn="uni/tn-%s/brc-%s" name="%s"/>' % (state, os.environ["ACI_USERNAME"], tenant, contract, contract)
    apic.setgeneric_XML(xml_template)

    # Post to the APIC

    rc = apic.genericPOST()
    if rc not in OK:
        response = apic.content                            # display outout for debugging

    print "login: %s %s rc: %s %s %s" % (apic.aaaLogin(), URI, rc, state, response)
    response = '(...)'


def main():
    """
        Create the connection object and set up the environment. Attempt to login to validate the
        credentials. Randomly add contracts and then clean them up at the end.
    """
    end_timer = time.time() + HOUR
    tenant = os.environ["ACI_TENANT"]

    cntrl = AnsibleACI.Connection()
    cntrl.setcontrollerIP(os.environ["ACI_HOST"])
    cntrl.setUsername(os.environ["ACI_USERNAME"])
    cntrl.setPassword(os.environ["ACI_PASSWORD"])
    cntrl.setDebug(False)

    if cntrl.aaaLogin() not in OK:
        print ("Unable to login to controller")
        return

    print "Running for %s seconds, use CNTL + C to exit." % HOUR

    # Add contracts
    while time.time() < end_timer:
        item = PREFIX + str(random.randint(0, END))
        contract(apic=cntrl, contract=item, tenant=tenant, desired_state='present')

    # Clean up
    for number in range(0, END):
        item = PREFIX + number
        contract(apic=cntrl, contract=item, tenant=tenant, desired_state='absent')


if __name__ == '__main__':
    main()
