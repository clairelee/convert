## INFO: ###
# File must be saved in CSV - UTF8 ENCODING #
# FILL OUT LINE 8 WITH ORIGIN CSV NAME, MUST BE SAVED IN SAME DIRECTORY #

import csv
import os

inputFileName = "test3.csv" # insert file name here (must be in same directory)
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
        to_address_name = row['Address Name']
        to_address_street1 = row['Address Line 1']
        to_address_street2 = row['Address Line 2']
        to_address_city = row['Address City']
        to_address_state = row['Address State']
        to_address_zip = row['Address Postal Code']
        to_address_country = row['Address Country']
        to_address_phone = row['Address Phone Number']
        to_address_email = row['Email']
        product_barcode = row['SKU1']
        units = row['qty1']
        # service = row['Shipping Delivery Notes']
        service = ""

        # write
        w.writerow([to_address_name, to_address_street1, to_address_street2,
        to_address_city, to_address_state, to_address_zip, to_address_country,
        to_address_phone, to_address_email, product_barcode, units, service])

        # check if more items ordered
        if row['SKU2'] != "":
            product_barcode = row['SKU2']
            units = row['qty2']

            w.writerow([to_address_name, to_address_street1, to_address_street2,
            to_address_city, to_address_state, to_address_zip, to_address_country,
            to_address_phone, to_address_email, product_barcode, units, service])

        if row['SKU3'] != "":
            product_barcode = row['SKU3']
            units = row['qty3']

            w.writerow([to_address_name, to_address_street1, to_address_street2,
            to_address_city, to_address_state, to_address_zip, to_address_country,
            to_address_phone, to_address_email, product_barcode, units, service])

        if row['SKU4'] != "":
            product_barcode = row['SKU4']
            units = row['qty4']

            w.writerow([to_address_name, to_address_street1, to_address_street2,
            to_address_city, to_address_state, to_address_zip, to_address_country,
            to_address_phone, to_address_email, product_barcode, units, service])
