from __future__ import print_function

import csv


def get_shares_list():
    """
        This function operates on the structured csv file which contains
        companies shares information on specific times. Uses csv module to
        parse the csv data. Returns the list of companies with their
        highest corresponding share rate along with other data
    """

    company_shares_list = []

    try:
        with open('test_shares_data.csv', 'rb') as csvfile:
            shares_reader = csv.DictReader(csvfile, delimiter=',')

            company_names = shares_reader.fieldnames[2:]
            YEAR_FIELD_NAME, MONTH_FIELD_NAME = shares_reader.fieldnames[:2]
            MAX_PRICE_FIELD_NAME = 'Max Price'

            shares_list = list(shares_reader)  # Makes sure that we can iterate
                                               # over list again and again
            for company_name in company_names:
                max_for_company = max(
                    shares_list, key=lambda x: int(x[company_name]))

                company_shares_list.append({
                    company_name: {
                        MONTH_FIELD_NAME: max_for_company[MONTH_FIELD_NAME],
                        YEAR_FIELD_NAME: int(max_for_company[YEAR_FIELD_NAME]),
                        MAX_PRICE_FIELD_NAME: int(max_for_company[company_name])
                        }})

    except IOError:
        pass

    return company_shares_list


def main():
    entries = get_shares_list()

    if not entries:
        # Cannot do this in module level execution, hence the main function
        return

    for entry in entries:
        for key, value in entry.items():
            print("{} - ".format(key), end=' ')
            for k, v in value.items():
                print("{} - {},".format(k, v), end=' ')
            print()


if __name__ == "__main__":
    main()
