# Importing csv so we can work with CSV files
import csv

# Read data from a CSV file
def read_budget_data(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the first row
        data = list(csv_reader)
    return data

# Function to calculate stats from the data
def calculate_statistics(data):
    month_count = 0
    total_profit_loss = 0
    monthly_changes = []  # Store changes month to month
    months = []  # Store the names of the months
    highest_profit_increase = ["", 0]  # Initialize highest profit increase
    largest_loss = ["", float('inf')]  # Initialize largest loss

    # Get the first row to start off calculations
    first_row = data[0]
    previous_profit_loss = int(first_row[1])
    total_profit_loss += previous_profit_loss
    month_count += 1

    # Go through the rest of the data
    for row in data[1:]:  # Start at second row
        month_count += 1
        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss

        # Find the change from the last month
        profit_loss_change = current_profit_loss - previous_profit_loss
        monthly_changes.append(profit_loss_change)
        months.append(row[0])  # Save the month name
        previous_profit_loss = current_profit_loss  # Update for next iteration

        # Check if this is the biggest profit increase
        if profit_loss_change > highest_profit_increase[1]:
            highest_profit_increase = [row[0], profit_loss_change]

        # Check if this is the biggest loss
        if profit_loss_change < largest_loss[1]:
            largest_loss = [row[0], profit_loss_change]

    # Calculate the average change over the months
    average_monthly_change = sum(monthly_changes) / len(monthly_changes)

    # Return all the calculated stats in a dictionary
    return {
        "month_count": month_count,
        "total_profit_loss": total_profit_loss,
        "average_monthly_change": average_monthly_change,
        "highest_profit_increase": highest_profit_increase,
        "largest_loss": largest_loss
    }

# This function formats the stats into a readable summary
def format_summary(statistics):
    summary = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {statistics['month_count']}\n"
        f"Total: ${statistics['total_profit_loss']}\n"
        f"Average Change: ${statistics['average_monthly_change']:.2f}\n"
        f"Greatest Increase in Profits: {statistics['highest_profit_increase'][0]} "
        f"(${statistics['highest_profit_increase'][1]})\n"
        f"Greatest Decrease in Profits: {statistics['largest_loss'][0]} "
        f"(${statistics['largest_loss'][1]})\n"
    )
    return summary

# This function writes the summary to a text file
def write_summary_to_file(output_file, summary):
    with open(output_file, "w") as file:
        file.write(summary)

# This is the main function that runs everything
def main():
    # File paths for the input CSV and the output text file
    input_file = "C:/Users/chukw/OneDrive/Documents/Data Analytics Bootcamp/Assignments/Module 3/Starter_Code/PyBank/Resources/budget_data.csv"
    output_file = "C:/Users/chukw/OneDrive/Documents/Data Analytics Bootcamp/Assignments/Module 3/Starter_Code/PyBank/analysis/financial_analysis.txt"

    # Read the budget data from the CSV
    budget_data = read_budget_data(input_file)

    # Calculate the financial statistics
    financial_statistics = calculate_statistics(budget_data)

    # Create the summary
    summary = format_summary(financial_statistics)

    # Print the summary to the terminal
    print(summary)

    # Write the summary to a file
    write_summary_to_file(output_file, summary)

if __name__ == "__main__":
    main()

