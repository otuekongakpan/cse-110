countries = []
codes = []
years = []
life_expectancies = []

# Open the file
with open("life-expectancy.csv") as life_file:
    next(life_file)  # Skip the header
    for line in life_file:
        parts = line.strip().split(",")

        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        countries.append(country)
        codes.append(code)
        years.append(year)
        life_expectancies.append(life_expectancy)

# User input
selected_year = int(input("Enter year of interest: "))

# Filter data for the selected year
filtered_life_expectancies = []
filtered_countries = []

for i in range(len(years)):
    if years[i] == selected_year:
        filtered_life_expectancies.append(life_expectancies[i])
        filtered_countries.append(countries[i])

# Ensure there is data for the selected year
if filtered_life_expectancies:
    largest_so_far = filtered_life_expectancies[0]
    largest_country = filtered_countries[0]
    smallest_so_far = filtered_life_expectancies[0]
    smallest_country = filtered_countries[0]

    # Find highest and lowest life expectancy
    for i in range(len(filtered_life_expectancies)):
        if filtered_life_expectancies[i] > largest_so_far:
            largest_so_far = filtered_life_expectancies[i]
            largest_country = filtered_countries[i]

        if filtered_life_expectancies[i] < smallest_so_far:
            smallest_so_far = filtered_life_expectancies[i]
            smallest_country = filtered_countries[i]

    # Print final results
    print(f"The highest life expectancy in {selected_year} was {largest_so_far} in {largest_country}")
    print(f"The lowest life expectancy in {selected_year} was {smallest_so_far} in {smallest_country}")
else:
    print("Invalid year or no data available for the selected year.")