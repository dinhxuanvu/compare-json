#!/usr/bin/env python

"""Compare templates and imagestreams json from various sources"""

import argparse
import json
import os
import glob
import logging
import sys
from jsondiff import diff

# CONST
TEMPLATES_DIR = "templates/examples/"
LIBRARY_TEMPLATES_DIR = "templates/"
IMAGES_DIR = "imagestreams/"
STARTER_DIR = "online-starter/"
PRO_DIR = "online-professional/"
FREE_DIR = "free/"
PAID_DIR = "paid/"
LIBRARY_DIR = "library/"

# Fail flag
diff_fail = False
# Set logger level
logging.getLogger().setLevel(logging.INFO)

def compare_template(tier, name, library_data, online_data):
    """ Compare two templates and log the differences

    Args:
        tier (string): free or paid tier
        name (string): name of the file
        library_data (json): json data for library template
        online_data (json): json data for online template

    """
    global diff_fail
    result = diff(library_data, online_data)
    if result:
        msg = "Upstream imagestream is different with Online %s imagestream %s:" % (tier, name)
        logging.error(msg)
        # try:
        #     logging.error(json.dumps(result))
        # except TypeError:
        #     logging.warning("TypeError prevents the JSON diff to be converted properly. Please compare manually.")
        #     pass
        diff_fail = True

def compare_imagestream(tier, name, library_data, online_data):
    """ Compare two image-streams and log the differences

    Args:
        tier (string): free or paid tier
        name (string): name of the file
        library_data (json): json data for library imagestream
        online_data (json): json data for online imagestream

    """
    global diff_fail
    result = diff(library_data, online_data)
    if result:
        msg = "Upstream imagestream is different with Online %s imagestream %s:" % (tier, name)
        logging.error(msg)
        # try:
        #     logging.error(json.dumps(result))
        # except TypeError:
        #     logging.warning("TypeError prevents the JSON diff to be converted properly. Please compare manually.")
        #     pass
        diff_fail = True

def main():
    """ Runs the main program, gets the data from the YAML file(s)
        and compare them

    """
    global diff_fail

    # Compare templates for free
    if os.path.exists(os.path.join(FREE_DIR, TEMPLATES_DIR)):
        online_list = glob.glob(FREE_DIR + TEMPLATES_DIR + "*.json")
        for item in glob.glob(LIBRARY_DIR + STARTER_DIR + LIBRARY_TEMPLATES_DIR + "*.json"):
            name = os.path.basename(item)
            online_name = FREE_DIR + TEMPLATES_DIR + name
            if online_name in online_list:
                with open(item) as library_file:
                    library_data = json.load(library_file)
                with open(online_name) as online_file:
                    online_data = json.load(online_file)
                compare_template("Free", name, library_data, online_data)
            else:
                logging.error("Online Free directory is missing template " + name)
                diff_fail = True
    else:
        logging.error("Templates directory for Online Free doesn't exist.")
        diff_fail = True

    logging.info("Finished comparing templates for Online Free.")

    # Compare imagestreams for free
    if os.path.exists(os.path.join(FREE_DIR, IMAGES_DIR)):
        online_list = glob.glob(FREE_DIR + IMAGES_DIR + "*.json")
        for item in glob.glob(LIBRARY_DIR + STARTER_DIR + IMAGES_DIR + "*.json"):
            name = os.path.basename(item)
            online_name = FREE_DIR + IMAGES_DIR + name
            if online_name in online_list:
                with open(item) as library_file:
                    library_data = json.load(library_file)
                with open(online_name) as online_file:
                    online_data = json.load(online_file)
                compare_imagestream("Free", name, library_data, online_data)
            else:
                logging.error("Online Free directory is missing imagestream " + name)
                diff_fail = True
    else:
        logging.error("Imagestreams directory for Online Free doesn't exist.")
        diff_fail = True

    logging.info("Finished comparing imagestreams for Online Free.")

    # Compare templates for paid
    if os.path.exists(os.path.join(PAID_DIR, TEMPLATES_DIR)):
        online_list = glob.glob(PAID_DIR + TEMPLATES_DIR + "*.json")
        for item in glob.glob(LIBRARY_DIR + PRO_DIR + LIBRARY_TEMPLATES_DIR + "*.json"):
            name = os.path.basename(item)
            online_name = PAID_DIR + TEMPLATES_DIR + name
            if online_name in online_list:
                with open(item) as library_file:
                    library_data = json.load(library_file)
                with open(online_name) as online_file:
                    online_data = json.load(online_file)
                compare_template("Paid", name, library_data, online_data)
            else:
                logging.error("Online Paid directory is missing template " + name)
                diff_fail = True
    else:
        logging.error("Templates directory for Online Paid doesn't exist.")
        diff_fail = True

    logging.info("Finished comparing templates for Online Paid.")

    # Compare imagestreams for paid
    if os.path.exists(os.path.join(PAID_DIR, IMAGES_DIR)):
        online_list = glob.glob(PAID_DIR + IMAGES_DIR + "*.json")
        for item in glob.glob(LIBRARY_DIR + PRO_DIR + IMAGES_DIR + "*.json"):
            name = os.path.basename(item)
            online_name = PAID_DIR + IMAGES_DIR + name
            if online_name in online_list:
                with open(item) as library_file:
                    library_data = json.load(library_file)
                with open(online_name) as online_file:
                    online_data = json.load(online_file)
                compare_imagestream("Paid", name, library_data, online_data)
            else:
                logging.error("Online Paid directory is missing imagestream " + name)
                diff_fail = True
    else:
        logging.error("Imagestreams directory for Online Paid doesn't exist.")
        diff_fail = True

    logging.info("Finished comparing imagestreams for Online Paid.")

    if diff_fail:
        print "Differences in templates/imagestreams are found!"
        sys.exit(1)

    print "No differences are found in templates/imagestreams."

if __name__ == '__main__':
    main()
