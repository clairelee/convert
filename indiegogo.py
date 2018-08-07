## INFO: ###
# File must be saved in CSV - UTF8 ENCODING #
# FILL OUT LINE 8 WITH ORIGIN CSV NAME, MUST BE SAVED IN SAME DIRECTORY #

import csv
import os

inputFileName = "test2.csv" # insert file name here (must be in same directory)
outputFileName = "updated_" + os.path.splitext(inputFileName)[0] + ".csv"

with open(inputFileName, 'rt') as inFile, open(outputFileName, 'wt') as outfile:
    r = csv.DictReader(inFile, delimiter=',')
    w = csv.writer(outfile)

    next(r)  # skip the first row from the reader, the old header
    # write new header
    w.writerow(['to_address_name', 'to_address_street1', 'to_address_street2',
    'to_address_city', 'to_address_state', 'to_address_zip', 'to_address_country',
    'to_address_phone', 'to_address_email', 'product_barcode', 'units', 'service'])

    # copy the rest
    for row in r:
        to_address_name = row['Shipping Name']
        to_address_street1 = row['Shipping Address']
        to_address_street2 = row['Shipping Address 2']
        to_address_city = row['Shipping City']
        to_address_state = row['Shipping State/Province']
        to_address_zip = row['Shipping Zip/Postal Code']
        to_address_country = row['Shipping Country']
        to_address_phone = row['Shipping Phone Number']
        to_address_email = row['Email']
        product_barcode = row['Perk']
        # units = row['Quantity:']
        units = ""
        # service = row['Shipping Delivery Notes']
        service = ""

        # write
        w.writerow([to_address_name, to_address_street1, to_address_street2,
        to_address_city, to_address_state, to_address_zip, to_address_country,
        to_address_phone, to_address_email, product_barcode, units, service])
