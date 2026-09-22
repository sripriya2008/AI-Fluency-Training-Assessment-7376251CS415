import csv

print("====================================")
print("      RULE-BASED WORKFLOW")
print("====================================")

print()
print("Reading private study data...")
print()

recommended_subject = None
reason = ""

with open("data/study_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        subject = row["Subject"]
        progress = int(row["Progress"])
        priority = row["Priority"]

        # Predefined rule
        if priority == "High" and progress < 70:
            recommended_subject = subject
            reason = (
                f"{subject} has {progress}% progress "
                f"and {priority} priority."
            )
            break

print("Workflow Decision:")

if recommended_subject:
    print()
    print("Recommended Subject:", recommended_subject)
    print("Reason:", reason)
    print()
    print("Rule used:")
    print("Priority = High AND Progress < 70%")
else:
    print("No subject matched the predefined rule.")