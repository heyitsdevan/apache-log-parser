# .. Apache-log-parser

# 1. Reads a file
# 2. Finds all IP addresses and their frequency
# 3. Writes data to a csv file
# 
#
# 1/24/2020

import re
import csv
from collections import Counter

# Enter filename here
filename = ""

def reader(filename):
    with open(filename) as f:
        log = f.read()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        return ips_list


def count(ips_list):
    return Counter(ips_list)


def write_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Frequency']
        writer.writerow(header)
        for ip, amount in counter.items():
            writer.writerow((ip, amount))


if __name__ == "__main__":
    ips = reader(filename)
    data = count(ips)
    write_csv(data)
    
