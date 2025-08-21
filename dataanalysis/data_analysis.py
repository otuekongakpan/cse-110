countries = []
codes = []
years = []
life_expectancies = []

# Open the file
with open("life-expectancy.csv") as life_file:
    next(life_file)  
    # split the file content 
    for line in life_file:
        parts = line.split(",")

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

# Filtering data for the selected year
filtered_life_expectancies = []
filtered_countries = []

for i in range(len(years)):
    if years[i] == selected_year:
        filtered_life_expectancies.append(life_expectancies[i])
        filtered_countries.append(countries[i])

# Computing overall max, min, and average life expectancy
overall_max_life_expectancy = max(life_expectancies)
overall_min_life_expectancy = min(life_expectancies)
average_life_expectancy = sum(life_expectancies) / len(life_expectancies)

# Finding the countries corresponding to max/min life expectancy
max_index = life_expectancies.index(overall_max_life_expectancy)
min_index = life_expectancies.index(overall_min_life_expectancy)

overall_max_country = countries[max_index]
overall_min_country = countries[min_index]


print(f"The overall maximum life expectancy recorded was {overall_max_life_expectancy} in {overall_max_country}")
print(f"The overall minimum life expectancy recorded was {overall_min_life_expectancy} in {overall_min_country}")
print(f"The average life expectancy across all countries and years is {average_life_expectancy:.2f}")

# selected year life expectancy calculations
if filtered_life_expectancies:
    largest_so_far = filtered_life_expectancies[0]
    largest_country = filtered_countries[0]
    smallest_so_far = filtered_life_expectancies[0]
    smallest_country = filtered_countries[0]

    for i in range(len(filtered_life_expectancies)):
        if filtered_life_expectancies[i] > largest_so_far:
            largest_so_far = filtered_life_expectancies[i]
            largest_country = filtered_countries[i]

        if filtered_life_expectancies[i] < smallest_so_far:
            smallest_so_far = filtered_life_expectancies[i]
            smallest_country = filtered_countries[i]

    print(f"For the year {selected_year}:")
    print(f"The maximum life expectancy was {largest_so_far} in {largest_country}")
    print(f"The minimum life expectancy was {smallest_so_far} in {smallest_country}")
else:
    print("Invalid year or no data available for the selected year.")