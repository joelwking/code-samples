#!/usr/bin/env python
#
#      get_inventory.py    Sample program to create a dynamic inventory from a CSV file
#
#      Usage: See the companion playbook get_invy.yml
#
#      Copyright (c) 2016 World Wide Technology, Inc.
#      All rights reserved.
#
#      author: Joel W. King,  World Wide Technology
#
#      Reference: http://www.jeffgeerling.com/blog/creating-custom-dynamic-inventories-ansible
#                 Chapter 7 of Ansible for DevOps, a book on Ansible by Jeff Geerling. 
#
#
import sys
import json
import csv 
 
def main():
    "Create a dynamic Ansible inventory from a spreadsheet"

    GROUP = "F5_CREATE"                                    # Name of the group referenced in the playbook
    HOSTNAME = "STUDENT_POD"                               # Column header in the CSV file which we use as the host name
    CSV_FILE =  "f5_create.csv"                            # CSV file, this should be passed to the program

    group_output = {
                       GROUP: dict(hosts=[]),
                     "_meta": {"hostvars": dict()}
                   }
    
    #
    # Read the CSV and format
    #
    with open(CSV_FILE) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                # Append the hostname to the list of hosts under the group
            group_output[GROUP]["hosts"].append(row[HOSTNAME])
                # Create an empty dictionary in the meta data for the host
            group_output["_meta"]["hostvars"][row[HOSTNAME]] = dict()
                # Populate the host variables from each column in the spreadsheet
            for key, value in row.items():
                group_output["_meta"]["hostvars"][row[HOSTNAME]][key] = value

    return  group_output
 
 
if __name__ == '__main__':
 
    print json.dumps(main())
