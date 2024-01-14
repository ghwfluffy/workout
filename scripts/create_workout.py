#!/usr/bin/env python3

import random
import argparse

from utils.data import get_data

#from datetime import date, datetime
#from utils.datemanip import today, DateDelta, period_to_month_multiplier

# XXX: Incorporate better
exclude = [
    "Front Squats",
    "Man Makers",
    "Wall Balls",
]

# Create the parser
def get_args():
    parser = argparse.ArgumentParser(
        description="Create workout.")

    # Add arguments
    parser.add_argument(
        "-U",
        "--upper-body",
        action="store_true",
        )

    parser.add_argument(
        "-L",
        "--lower-body",
        action="store_true",
        )

    parser.add_argument(
        "-F",
        "--full-body",
        action="store_true",
        )

    # Parse the arguments
    return parser.parse_args()

def parse_categories(args):
    upper_body = args.upper_body
    lower_body = args.lower_body
    full_body = args.full_body
    if not upper_body and not lower_body and not full_body:
        upper_body = True
        lower_body = True
        full_body = True
    categories = ["Stretching"]
    if upper_body:
        categories.append("Upper")

    if lower_body:
        categories.append("Lower")

    if full_body:
        categories.append("Full Body")

    return categories

args = get_args()
categories = parse_categories(args)
data = get_data()

#data['exercises'].sort(key=lambda x:x['lastComplete'])
data['exercises'].sort(key=lambda x:random.randint(1, 100000))

free_weights = []
machines = []
aerobics = []
stretching = []

NUM_FREEWEIGHTS=4
NUM_MACHINES=4
NUM_AEROBICS=4
NUM_STRETCHING=2

for item in data['exercises']:
    try:
        if not item['category'] in categories:
            continue
        if item['name'] in exclude:
            continue
        if item['type'] == "Aerobics" and len(aerobics) < NUM_AEROBICS:
            aerobics.append(item)
        elif item['type'] == "Free Weights" and len(free_weights) < NUM_FREEWEIGHTS:
            free_weights.append(item)
        elif item['type'] == "Machines" and len(machines) < NUM_MACHINES:
            machines.append(item)
        elif item['type'] == "Stretching" and len(stretching) < NUM_STRETCHING:
            stretching.append(item)
    except:
        print("Error processing: " + str(item))

def print_item(item):
    print("{}: {} / {}".format(item['name'], item['hypertrophy'], item['tone']))

for x in [stretching, free_weights, machines, aerobics]:
    for item in x:
        print_item(item)
