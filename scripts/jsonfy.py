import argparse
import json
import csv
import collections
import brotli

OrderedDict = collections.OrderedDict


arguments = argparse.ArgumentParser(
    description='Read a TSV file and compress in into a JSON with indexed key '
                'storage. This assumes a sufficient degree of field value '
                'repetitions'
)

arguments.add_argument(
    'input',
    help='The TSV file to compress',
)
arguments.add_argument(
    'output',
    help='The JSON file to compress the input file to',
)

args = arguments.parse_args()
# disable direct storage of values
args.switch = 0


titles = ["taxon","lineage","probability","pangoLEARN_""version","status","note"]

parsed_data = []
with open(args.input, "r") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")
    for row in reader:
        parsed_data.append(OrderedDict(zip(titles, row)))

with open(args.output, 'w') as jsonfile:
    # json.dump(parsed_data, jsonfile, indent=2)
    json.dump(parsed_data, jsonfile, separators=(',', ':'))
