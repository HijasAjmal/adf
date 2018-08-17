import csv

"""
Contains record yielders compatible with core.Adf
Basically a independant record unit as a dict
"""

def read_csv(filename):
    """
    Reads a csv and yields a record one dict at a time
    """
    with open(filename) as f:
        reader = csv.DictReader(f)  # Eh, simple enough!
        for row in reader:
            # The generator should help with the memory management somewhat
            yield row

def base_reader(reader):
    """

    :param reader:
    :return:
    """
    for row in reader:
        # The generator should help with the memory management somewhat
        yield row
