import csv


def get_course_fee(course_code):
    """Look up a course fee from the course data CSV file."""

    try:
        with open("data/course_data.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["course_code"].lower() == course_code.lower():
                    return (
                        f"Course: {row['course_code']}\n"
                        f"Course Name: {row['course_name']}\n"
                        f"Fee: ₹{row['fee']}"
                    )

            return f"No course found for {course_code}."

    except Exception as error:
        return f"Tool error: {error}"