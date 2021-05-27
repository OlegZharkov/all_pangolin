import argparse
import csv
from datetime import datetime



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

with open(args.input, "r") as tsvfile:
    # skip headers
    reader = csv.reader(tsvfile, delimiter="\t")
    headers = next(reader)
    with open(args.output, 'w') as line:
        tsv_writer = csv.writer(line, delimiter='\t')
        tsv_writer.writerow(headers)
        for row in reader:
            row[3] = datetime.strptime(row[3],'%Y-%m-%d').strftime('%m/%d/%Y')
            tsv_writer.writerow(row)

        


