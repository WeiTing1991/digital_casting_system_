import json
import csv


class DataGathering():
    """
    TBC...
    """
    def __init__(self):
        pass

    def func(self):
        pass



def write_dict_to_json(filepath, data):
    # Write the python dictionary to json file
    with open(filepath, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=5)
        print('\nThe json file is sucessfully exported!!!')


def write_dict_to_csv(filepath, data, header):
    # Write the python dictionary to csv file
    with open(filepath, 'w+', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
        print('\nThe csv file is sucessfully exported!!!')


