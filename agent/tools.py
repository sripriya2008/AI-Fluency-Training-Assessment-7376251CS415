import csv


def read_study_data():
    """Read the student's private study data."""

    study_data = []

    with open("data/study_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            study_data.append(row)

    return study_data