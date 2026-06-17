# File names
input_file = r"C:\Users\ACER\Downloads\city_temperatures.txt"
error_file = r"C:\Users\ACER\Downloads\temperature_errors.txt"
output_file = r"C:\Users\ACER\Downloads\average_temperatures.txt"

def process_temperature_data():
    city_data = {}
    errors = []

    try:
        with open(input_file, "r") as file:
            for line in file:
                line = line.strip()
                try:
                    city, date, temperature = line.split(",")
                    if temperature.lower() in ["invalid", "missing"]:
                        raise ValueError(f"Invalid temperature value: {temperature}")
                    
                    temperature = float(temperature)  # Convert to float

                    if city not in city_data:
                        city_data[city] = []
                    city_data[city].append(temperature)

                except ValueError as e:
                    errors.append(f"Error in line '{line}': {e}")

    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        return

    # Write errors to the error file
    with open(error_file, "w") as err_file:
        for error in errors:
            err_file.write(error + "\n")

    # Calculate averages and write to the output file
    averages = {}
    with open(output_file, "w") as out_file:
        for city, temperatures in city_data.items():
            if temperatures:
                avg_temp = sum(temperatures) / len(temperatures)
                averages[city] = avg_temp
                out_file.write(f"{city}: {avg_temp:.2f}\n")

    # Display averages
    print("Average Temperatures:")
    for city, avg_temp in averages.items():
        print(f"{city}: {avg_temp:.2f}")

if __name__ == "__main__":
    process_temperature_data()
