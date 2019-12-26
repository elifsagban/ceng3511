import csv


def get_column(filename, column):
    with open(filename) as f:
        reader = csv.DictReader(f)
        results = []

        for row in reader:
            entry = row[column]

            try:
                results.append(float(entry))
            except ValueError:
                print(
                    "Could not convert '{}' to "
                    "a float...skipping.".format(entry)
                )

        return results


result = get_column('test.csv','clock_speed')

print(result)
