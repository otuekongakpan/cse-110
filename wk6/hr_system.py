# open the file
with open("hr_system.txt") as hr_file:
    next(hr_file)

    # read through the file line by line
    for line in hr_file:
        # get the various parts of the record into variables
        parts = line.split(" ")

        name = parts[0]
        id = int(parts[1])
        job_title = parts[2]
        salary = int(parts[3])

        paycheck_amount = salary / 24

        if job_title.lower() == "engineer":
                paycheck_amount = paycheck_amount + 1000
        # print out the values
        print(f"{name} (ID: {id}, {job_title} - ${paycheck_amount:.2f})")
