"""GroundSpeed Take Home Coding Assignment

Project Scope:
Companies purchase insurance policies for their fleet of motor vehicles. They must maintain an
inventory of the fleet along with aggregate and policy information. In this problem you will design
a data structure to hold the information for cars and some aggregate metrics for the fleet.

1. Design a data structure for a single car that
- Has a unique id
- Contains the properties
- Year, make, model, purchase value, VIN, license plate state, and number

2. Design a data structure that
- Contains aggregated metrics for the fleet
- Total count
- Count by year
- Total purchase price

3. Write a method that
- Take a list of car data structures
- Return an aggregated data structure

4. Design a data structure/method to provide quick lookups for automobiles by VIN.

5. How would you design a data structure/method to provide sorted lists of car data
structures by property field?

I would use .sort_values() in pandas to sort the data based on values in the column header similar to how you would
sort a spreadsheet.

Example:
    fleet.sort_values(by="year", ascending=False)

"""
import re
import pandas as pd


def vin_lookup(vin, fleet):
    """This function checks the dataframe of the fleet for a specific VIN number and returns metrics about that vehicle.

    Args:
        fleet: Dataframe read from data.csv.
        vin: This parameter is used to check the dataframe for a specific match.

    Returns:
        
        This function will return single_car which contains a dataframe with metrics for a single car that is found
        based on a matching VIN record.

    Raises: An error of "Invalid VIN. Please try again!" will be raised if the user enters something that is not a
    valid VIN number according to the VIN number format standards.

    """

    if not re.match(r'\b[(A-H|J-N|P|R-Z|0-9)]{17}\b', vin):
        print("Invalid VIN. Please try again!")
    else:
        single_car = fleet.loc[fleet['VIN'] == vin]
        print(single_car)
        return single_car


def main():
    """This is the main function that holds the rest of the code for the project. This is going to read our fleet data
    from the data.csv then print that data to show aggregated metrics for the entire fleet. This will then pull the
    metrics as defined in the project scope and print that dataframe as well. Next it will look for unique years in the
    fleet dataframe and pull metrics (count and total purchase price by year) and print those as well. Finally we will
    lookup the vin for a specific vehicle in the fleet dataframe and print the dataframe with metrics for that specific
    vehicle result.

    """

    fleet = pd.read_csv('data.csv', header=0)
    print(fleet.sort_values(by="year", ascending=False))
    metrics = pd.DataFrame({
        'Total count': [fleet['id'].count()],
        'Total purchase price': [fleet['purchase value ($)'].aggregate('sum')]
    })
    print(metrics)
    unique_years = fleet.year.unique()
    count_by_year = pd.DataFrame()

    for year in unique_years:
        rslt_df = fleet.loc[fleet['year'] == year]
        new_df_second = pd.DataFrame(
            {"year": [year], "count": [len(rslt_df)], "purchase value ($)": [sum(rslt_df['purchase value ($)'])]})
        count_by_year = pd.concat([count_by_year, new_df_second])

    print(count_by_year)
    vin = input('Please enter the VIN you are looking for: ')
    vin_lookup(vin, fleet)


if __name__ == "__main__":
    main()
