#!/usr/bin/env python
"""

    pw_chckr.py  - Checks the password strength using a REST API call to www.passable.io

    Copyright (c) 2016 World Wide Technology, Inc.
    All rights reserved.
    Revision history:
     23 May  2016  |  1.0 - initial release

"""

import requests
import csv
import hashlib
import argparse
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

HEADERS = {"Content-Type": "application/json"}
MD5_URL = "https://www.passable.io/searcher/md5/"
STATUS = {0: "OK", 1: "Not safe", None: "not checked, connection error"}


def read_csv(input_file):
    """ Read the CSV file specified and check the strength of each row in
        the file, ignoring blank rows. The CSV file must have at least two
        columns with headers URL and Password. Print out the URL and 
        password status for the rows. Password Corral 
        http://www.cygnusproductions.com/freeware/pc.asp
        can be used to export a clear text CSV file, but it will not include
        column headers.
    """
    row_counter = 0
    try:
        with open(input_file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                if row['Password'] is "":
                    continue
                row_counter += 1
                ret_code = call_passable(MD5_URL + hash_password(row['Password']))
                print "%s %s" % (row['URL'], password_status(ret_code))
    except IOError:
        print "IOError on input file: %s" % input_file
        return None

    print "Processed %s rows" % row_counter
    csvfile.close()
    return None


def hash_password(clear_text):
    """ Use hashlib to create the MD5 hash of the clear text password, return the hash.
    """
    md5 = hashlib.md5()
    md5.update(clear_text)
    return md5.hexdigest()


def password_status(indicator):
    """Reply with the status message of the password checked."
    """
    try:
        return STATUS[indicator]
    except KeyError:
        return "Unknown status!"


def call_passable(URL):
    """ Call passable.io with the URL specified, a return value of '1' means the
        password is not safe, a value of "0" means OK. Convert values to integers
        so we can test for True or False. If we cannot return an integer, return
        the status code, which will evaluate to True. True is bad, False is good.
    """
    try:
        r = requests.get(URL, headers=HEADERS, verify=False)
    except requests.ConnectionError as e:
        print "ConnectionError %s" % e.message
        return None
    try:
        return int(r.content)
    except ValueError:
        return r.status_code


def main():
    """ Parse arguments and call the CSV or interactive logic, print help if no arguments provided.
    """
    parser = argparse.ArgumentParser(description='Checks the password strength using a REST API call to www.passable.io')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', dest="input", help='specify clear text password from command line')
    group.add_argument('-f', dest="filename", help='specify a Password Coral file to read')
    args = parser.parse_args()

    if args.filename:
        read_csv(args.filename)
        return
    if args.input:
        ret_code = call_passable(MD5_URL + hash_password(args.input))
        print "Password is %s" % password_status(ret_code)
    else:
        parser.print_help()
    return

if __name__ == '__main__':
    main()