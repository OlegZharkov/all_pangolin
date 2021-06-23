import argparse
import json
import csv
import collections

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


titles = ["Sample", "POS", "REF", "ALT", "AF", "EFFECT", "CODON", "TRID", "AA"]

parsed_data = []
with open(args.input, "r") as tsvfile:
    # skip headers
    reader = csv.reader(tsvfile, delimiter="\t")
    headers = next(reader)
    for row in reader:
        parsed_data.append(OrderedDict(zip(titles, row)))


with open(args.output, 'w') as output_file:
    dw =csv.DictWriter(output_file, titles, delimiter='\t')
    # dw.writeheader()
    dw.writerows(parsed_data)
