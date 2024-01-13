#!/usr/bin/env python3

import yaml
import argparse

from utils.data import get_data

#from datetime import date, datetime
#from utils.datemanip import today, DateDelta, period_to_month_multiplier

# Create the parser
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
args = parser.parse_args()

def parse_categories():
    upper_body = args.upper_body
    lower_body = args.lower_body
    full_body = args.full_body
    if not upper_body and not lower_body and not full_body:
        upper_body = True
        lower_body = True
        full_body = True
    categories = []
    if upper_body:
        categories.append("Upper")

    if lower_body:
        categories.append("Lower")

    if full_body:
        categories.append("Full Body")

    return categories

categories = parse_categories()
data = get_data()
data['exercises'].sort(key=lambda x:x['lastComplete'])

free_weights = []
machines = []
aerobics = []

for item in data['exercises']:
    if not item['category'] in categories:
        continue
    if item['type'] == "Aerobics" and len(aerobics) < 2:
        aerobics.append(item)
    elif item['type'] == "Free Weights" and len(free_weights) < 2:
        free_weights.append(item)
    elif item['type'] == "Machines" and len(machines) < 2:
        machines.append(item)

def print_item(item):
    print("{}: {} / {}".format(item['name'], item['hypertrophy'], item['tone']))

for item in free_weights:
    print_item(item)
for item in machines:
    print_item(item)
for item in aerobics:
    print_item(item)
