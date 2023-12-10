import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\ALOK KESHARWANI\Desktop\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv")

def generate_car_matrix(data):
    result_df = data.pivot(index='id_1', columns='id_2', values='car')
    result_df.fillna(0, inplace=True)

    # Set diagonal elements to 0
    np.fill_diagonal(result_df.values, 0)

    return result_df

generate_car_matrix(df)
print(generate_car_matrix(df))

    


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    
import pandas as pd
df = pd.read_csv(r"C:\Users\ALOK KESHARWANI\Desktop\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv")

def get_type_count(data):
    
    # Add a new categorical column 'car_type'
    data['car_type'] = pd.cut(data['car'], bins=[-float('inf'), 15, 25, float('inf')],
                             labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each car_type
    type_counts = data['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

result_dict = get_type_count(df)
print(result_dict)


    


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    
    import pandas as pd
df = pd.read_csv(r"C:\Users\ALOK KESHARWANI\Desktop\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv")
def get_bus_indexes(data):
   
    # Calculate the mean value of the 'bus' column
    bus_mean = data['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    selected_indexes = data[data['bus'] > 2 * bus_mean].index.tolist()

    # Sort the indices in ascending order
    selected_indexes.sort()

    return selected_indexes

result_indexes = get_bus_indexes(df)
print(result_indexes)


    


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    
    import pandas as pd
df = pd.read_csv(r"C:\Users\ALOK KESHARWANI\Desktop\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv")
def filter_routes(data):
    
    # Group by 'route' and calculate the average of the 'truck' column
    route_avg_truck = data.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' column is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes

result_routes = filter_routes(df)
print(result_routes)


    


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    
    import pandas as pd
df = pd.read_csv(r"C:\Users\ALOK KESHARWANI\Desktop\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv")
def multiply_matrix(input_matrix):
  
    # Copy the input matrix to avoid modifying the original DataFrame
    modified_matrix = input_matrix.copy()

    # Apply the specified logic to modify values
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    # Round values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix


result_df = pd.DataFrame({
    '827': [0.0, 4.1, 0.0],
    '821': [0.0, 0.0, 0.0],
    '804': [0.0, 0.0, 0.0],
}, index=['829', '826', '825'])
modified_result = multiply_matrix(result_df)
print(modified_result)

    


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    
 import pandas as pd

def check_time_completeness(df):
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], errors='coerce')
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], errors='coerce')

    # Drop rows with NaT (invalid timestamp)
    df.dropna(subset=['start_timestamp', 'end_timestamp'], inplace=True)

    df['duration'] = df['end_timestamp'] - df['start_timestamp']
    grouped = df.groupby(['id', 'id_2'])
    completeness_check = grouped.apply(lambda x: (
        (x['duration'].min() >= pd.Timedelta(days=1)) and
        (x['duration'].max() <= pd.Timedelta(days=1, seconds=1)) and
        (x['start_timestamp'].dt.dayofweek.nunique() == 7)
    ))
    return completeness_check

# Example usage:
df = pd.read_csv(r"C:\Users\ALOK KESHARWANI\Desktop\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-2.csv")
result_series = check_time_completeness(df)
print(result_series)


    
