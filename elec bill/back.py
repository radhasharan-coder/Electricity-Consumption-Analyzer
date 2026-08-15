import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# ELECTRICITY CONSUMPTION ANALYZER
# ============================================================

data = pd.DataFrame(columns=["Month", "Units", "Bill"])


# ============================================================
# 1. ADD MONTHLY ELECTRICITY DATA
# ============================================================

def add_monthly_data():

    global data

    try:
        n = int(input("\nHow many months do you want to enter? "))

        if n <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Invalid input.")
        return

    months = []
    units = []

    for i in range(n):

        month = input(f"\nEnter month {i + 1}: ").strip()

        while True:
            try:
                unit = float(input(f"Enter electricity consumption for {month} (units): "))

                if unit < 0:
                    print("Consumption cannot be negative.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        months.append(month)
        units.append(unit)

    rate = float(input("\nEnter electricity rate per unit (₹): "))

    units_array = np.array(units)

    bills = units_array * rate

    new_data = pd.DataFrame({
        "Month": months,
        "Units": units_array,
        "Bill": bills
    })

    data = pd.concat([data, new_data], ignore_index=True)

    print("\nData added successfully!")


# ============================================================
# 2. VIEW DATA
# ============================================================

def view_data():

    if data.empty:
        print("\nNo data available.")
        return

    print("\n========== ELECTRICITY DATA ==========")
    print(data.to_string(index=False))


# ============================================================
# 3. TOTAL CONSUMPTION
# ============================================================

def total_consumption():

    if data.empty:
        print("\nNo data available.")
        return

    total = np.sum(data["Units"].to_numpy())

    print(f"\nTotal Consumption: {total:.2f} units")


# ============================================================
# 4. AVERAGE CONSUMPTION
# ============================================================

def average_consumption():

    if data.empty:
        print("\nNo data available.")
        return

    average = np.mean(data["Units"].to_numpy())

    print(f"\nAverage Monthly Consumption: {average:.2f} units")


# ============================================================
# 5. MAXIMUM CONSUMPTION
# ============================================================

def maximum_consumption():

    if data.empty:
        print("\nNo data available.")
        return

    maximum = np.max(data["Units"].to_numpy())

    index = data["Units"].idxmax()
    month = data.loc[index, "Month"]

    print(f"\nMaximum Consumption: {maximum:.2f} units")
    print(f"Month: {month}")


# ============================================================
# 6. MINIMUM CONSUMPTION
# ============================================================

def minimum_consumption():

    if data.empty:
        print("\nNo data available.")
        return

    minimum = np.min(data["Units"].to_numpy())

    index = data["Units"].idxmin()
    month = data.loc[index, "Month"]

    print(f"\nMinimum Consumption: {minimum:.2f} units")
    print(f"Month: {month}")


# ============================================================
# 7. TOTAL BILL
# ============================================================

def total_bill():

    if data.empty:
        print("\nNo data available.")
        return

    total = np.sum(data["Bill"].to_numpy())

    print(f"\nTotal Electricity Bill: ₹{total:.2f}")


# ============================================================
# 8. AVERAGE BILL
# ============================================================

def average_bill():

    if data.empty:
        print("\nNo data available.")
        return

    average = np.mean(data["Bill"].to_numpy())

    print(f"\nAverage Monthly Bill: ₹{average:.2f}")


# ============================================================
# 9. MAXIMUM BILL
# ============================================================

def maximum_bill():

    if data.empty:
        print("\nNo data available.")
        return

    maximum = np.max(data["Bill"].to_numpy())

    index = data["Bill"].idxmax()
    month = data.loc[index, "Month"]

    print(f"\nMaximum Bill: ₹{maximum:.2f}")
    print(f"Month: {month}")


# ============================================================
# 10. MINIMUM BILL
# ============================================================

def minimum_bill():

    if data.empty:
        print("\nNo data available.")
        return

    minimum = np.min(data["Bill"].to_numpy())

    index = data["Bill"].idxmin()
    month = data.loc[index, "Month"]

    print(f"\nMinimum Bill: ₹{minimum:.2f}")
    print(f"Month: {month}")


# ============================================================
# 11. SEARCH MONTH
# ============================================================

def search_month():

    if data.empty:
        print("\nNo data available.")
        return

    month = input("\nEnter month to search: ").strip()

    result = data[
        data["Month"].str.lower() == month.lower()
    ]

    if result.empty:
        print("\nMonth not found.")
    else:
        print("\n========== SEARCH RESULT ==========")
        print(result.to_string(index=False))


# ============================================================
# 12. HIGH CONSUMPTION DETECTION
# ============================================================

def high_consumption():

    if data.empty:
        print("\nNo data available.")
        return

    try:
        limit = float(
            input("\nEnter consumption limit (units): ")
        )
    except ValueError:
        print("Invalid number.")
        return

    result = data[data["Units"] > limit]

    if result.empty:
        print("\nNo month has consumption above this limit.")
    else:
        print("\n========== HIGH CONSUMPTION ==========")
        print(result.to_string(index=False))


# ============================================================
# 13. SORT DATA
# ============================================================

def sort_data():

    if data.empty:
        print("\nNo data available.")
        return

    sorted_data = data.sort_values(
        by="Units",
        ascending=False
    )

    print("\n========== HIGHEST TO LOWEST ==========")
    print(sorted_data.to_string(index=False))


# ============================================================
# 14. STATISTICAL ANALYSIS
# ============================================================

def statistical_analysis():

    if data.empty:
        print("\nNo data available.")
        return

    units = data["Units"].to_numpy()

    print("\n========== STATISTICAL ANALYSIS ==========")

    print(f"Total: {np.sum(units):.2f}")
    print(f"Mean: {np.mean(units):.2f}")
    print(f"Median: {np.median(units):.2f}")
    print(f"Maximum: {np.max(units):.2f}")
    print(f"Minimum: {np.min(units):.2f}")
    print(f"Standard Deviation: {np.std(units):.2f}")


# ============================================================
# 15. APPLIANCE-WISE CONSUMPTION
# ============================================================

def appliance_analysis():

    appliances = [
        "Fan",
        "AC",
        "Refrigerator",
        "TV",
        "Lights",
        "Computer",
        "Washing Machine",
        "Other"
    ]

    power = []
    hours = []
    days = []

    print("\n========== APPLIANCE DETAILS ==========")

    for appliance in appliances:

        print(f"\n--- {appliance} ---")

        while True:
            try:
                watt = float(
                    input(f"Enter power of {appliance} in watts: ")
                )

                if watt < 0:
                    print("Power cannot be negative.")
                else:
                    break

            except ValueError:
                print("Enter a valid number.")

        while True:
            try:
                daily_hours = float(
                    input(f"How many hours per day is {appliance} used? ")
                )

                if daily_hours < 0 or daily_hours > 24:
                    print("Hours must be between 0 and 24.")
                else:
                    break

            except ValueError:
                print("Enter a valid number.")

        while True:
            try:
                number_of_days = int(
                    input("Number of days used in the month: ")
                )

                if number_of_days < 0 or number_of_days > 31:
                    print("Days must be between 0 and 31.")
                else:
                    break

            except ValueError:
                print("Enter a valid number.")

        power.append(watt)
        hours.append(daily_hours)
        days.append(number_of_days)

    power = np.array(power)
    hours = np.array(hours)
    days = np.array(days)

    # Electricity consumption formula:
    # Units = Power(W) × Hours × Days / 1000

    appliance_units = (power * hours * days) / 1000

    appliance_data = pd.DataFrame({
        "Appliance": appliances,
        "Power_W": power,
        "Hours_Per_Day": hours,
        "Days": days,
        "Units": appliance_units
    })

    print("\n========== APPLIANCE CONSUMPTION ==========")
    print(appliance_data.to_string(index=False))

    total = np.sum(appliance_units)

    print(f"\nTotal Appliance Consumption: {total:.2f} units")

    max_index = np.argmax(appliance_units)
    min_index = np.argmin(appliance_units)

    print(
        f"Highest Consuming Appliance: "
        f"{appliances[max_index]} "
        f"({appliance_units[max_index]:.2f} units)"
    )

    print(
        f"Lowest Consuming Appliance: "
        f"{appliances[min_index]} "
        f"({appliance_units[min_index]:.2f} units)"
    )

    # Appliance graph

    plt.figure(figsize=(10, 6))

    plt.bar(
        appliance_data["Appliance"],
        appliance_data["Units"]
    )

    plt.xlabel("Appliance")
    plt.ylabel("Electricity Consumption (Units)")
    plt.title("Appliance-wise Electricity Consumption")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# ============================================================
# 16. CONSUMPTION GRAPH
# ============================================================

def consumption_graph():

    if data.empty:
        print("\nNo data available.")
        return

    plt.figure(figsize=(10, 5))

    plt.plot(
        data["Month"],
        data["Units"],
        marker="o"
    )

    plt.xlabel("Month")
    plt.ylabel("Consumption (Units)")
    plt.title("Monthly Electricity Consumption")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()
    plt.show()


# ============================================================
# 17. BILL GRAPH
# ============================================================

def bill_graph():

    if data.empty:
        print("\nNo data available.")
        return

    plt.figure(figsize=(10, 5))

    plt.bar(
        data["Month"],
        data["Bill"]
    )

    plt.xlabel("Month")
    plt.ylabel("Electricity Bill (₹)")
    plt.title("Monthly Electricity Bill")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# ============================================================
# 18. SAVE DATA TO CSV
# ============================================================

def save_data():

    if data.empty:
        print("\nNo data available to save.")
        return

    data.to_csv("electricity_data.csv", index=False)

    print("\nData saved successfully as electricity_data.csv")


# ============================================================
# 19. COMPLETE REPORT
# ============================================================

def complete_report():

    if data.empty:
        print("\nNo data available.")
        return

    units = data["Units"].to_numpy()
    bills = data["Bill"].to_numpy()

    print("\n")
    print("=" * 50)
    print("          ELECTRICITY CONSUMPTION REPORT")
    print("=" * 50)

    print("\nMonthly Data:")
    print(data.to_string(index=False))

    print("\nSummary:")
    print(f"Total Consumption   : {np.sum(units):.2f} units")
    print(f"Average Consumption : {np.mean(units):.2f} units")
    print(f"Maximum Consumption : {np.max(units):.2f} units")
    print(f"Minimum Consumption : {np.min(units):.2f} units")

    print(f"\nTotal Bill          : ₹{np.sum(bills):.2f}")
    print(f"Average Bill        : ₹{np.mean(bills):.2f}")
    print(f"Maximum Bill        : ₹{np.max(bills):.2f}")
    print(f"Minimum Bill        : ₹{np.min(bills):.2f}")

    max_index = data["Units"].idxmax()
    min_index = data["Units"].idxmin()

    print(
        f"\nHighest Consumption Month: "
        f"{data.loc[max_index, 'Month']}"
    )

    print(
        f"Lowest Consumption Month: "
        f"{data.loc[min_index, 'Month']}"
    )

    print("=" * 50)


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n")
    print("=" * 50)
    print("       ELECTRICITY CONSUMPTION ANALYZER")
    print("=" * 50)

    print("1.  Add Monthly Data")
    print("2.  View Data")
    print("3.  Total Consumption")
    print("4.  Average Consumption")
    print("5.  Maximum Consumption")
    print("6.  Minimum Consumption")
    print("7.  Total Electricity Bill")
    print("8.  Average Electricity Bill")
    print("9.  Maximum Electricity Bill")
    print("10. Minimum Electricity Bill")
    print("11. Search Month")
    print("12. Find High Consumption")
    print("13. Sort Consumption")
    print("14. Statistical Analysis")
    print("15. Appliance-wise Analysis")
    print("16. Consumption Graph")
    print("17. Bill Graph")
    print("18. Save Data to CSV")
    print("19. Complete Report")
    print("20. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_monthly_data()

    elif choice == "2":
        view_data()

    elif choice == "3":
        total_consumption()

    elif choice == "4":
        average_consumption()

    elif choice == "5":
        maximum_consumption()

    elif choice == "6":
        minimum_consumption()

    elif choice == "7":
        total_bill()

    elif choice == "8":
        average_bill()

    elif choice == "9":
        maximum_bill()

    elif choice == "10":
        minimum_bill()

    elif choice == "11":
        search_month()

    elif choice == "12":
        high_consumption()

    elif choice == "13":
        sort_data()

    elif choice == "14":
        statistical_analysis()

    elif choice == "15":
        appliance_analysis()

    elif choice == "16":
        consumption_graph()

    elif choice == "17":
        bill_graph()

    elif choice == "18":
        save_data()

    elif choice == "19":
        complete_report()

    elif choice == "20":
        print("\nThank you for using Electricity Consumption Analyzer!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 20.")