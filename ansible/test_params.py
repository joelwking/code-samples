#!/usr/bin/python
#
"""

     Copyright (c) 2016 World Wide Technology, Inc.
     All rights reserved.


     Revision history:

     11 August 2016  |  1.0 - initial release

"""
DOCUMENTATION = '''

---

module: test_params
author: Joel W. King, World Wide Technology
version_added: "1.0"
short_description: Simplistic example showing input arguments and output JSON

description:
    - Used for debugging variables being passed into an Ansible module

options:
    url:
        description:
            - Input data
        required: true

'''

EXAMPLES = '''

  ansible localhost -m test_params -a 'url="https://www.google.com/news"'
'''

import json
import requests
#
HEADER = {"Content-Type": "application/json"}
#
def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(type='raw')
        )
    )

    url = module.params['url']
    url_type = "%s" % type(url)
    if isinstance(url, dict):                             # Is a dict when url: '{"name": "{{item.name}}"}'
        url = json.dumps(url)

    try:
        r = requests.get(url, headers=HEADER, verify=False)
        status_code = r.status_code
    except requests.ConnectionError as e:
        status_code = 599
        response = str(e)


    module.exit_json(changed=False, status_code=status_code, url_type=url_type, msg=url)

from ansible.module_utils.basic import *
main()
