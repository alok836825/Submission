import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    
    import pandas as pd
df = pd.read_csv(r"C:\Users\ALOK KESHARWANI\Desktop\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-3.csv")
def calculate_distance_matrix(df):
    
    # Create an empty DataFrame with unique IDs as indices and columns
    unique_ids = sorted(set(df['id_start']).union(df['id_end']))
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids).fillna(0.0)

    # Populate the distance matrix with cumulative distances
    for _, row in df.iterrows():
        distance_matrix.at[row['id_start'], row['id_end']] += row['distance']

    return distance_matrix

result_matrix = calculate_distance_matrix(df)

# Make the matrix symmetric
result_matrix = result_matrix.add(result_matrix.T, fill_value=0)

print(result_matrix)


    


def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    
    
    import pandas as pd

def unroll_distance_matrix(distance_matrix):

    # Initialize an empty list to store unrolled data
    unrolled_data = []

    # Iterate over the rows of the distance matrix
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            # Exclude same id_start to id_end combinations
            if id_start != id_end:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    # Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df
result_matrix = pd.DataFrame({
    '827': [0.0, 4.1, 0.0],
    '821': [0.0, 0.0, 0.0],
    '804': [0.0, 0.0, 0.0],
}, index=['829', '826', '825'])

result_unrolled = unroll_distance_matrix(result_matrix)
print(result_unrolled)


    


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    
    import pandas as pd

def find_ids_within_ten_percentage_threshold(df, reference_value):
  
    # Filter the DataFrame based on the reference value
    reference_data = df[df['id_start'] == reference_value]

    # Calculate the average distance for the reference value
    average_distance = reference_data['distance'].mean()

    # Calculate the threshold values within 10% of the average
    lower_threshold = average_distance - 0.1 * average_distance
    upper_threshold = average_distance + 0.1 * average_distance

    # Filter values within the threshold
    result_values = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]['id_start']

    # Remove duplicates and sort the result
    result_values = sorted(set(result_values))

    return result_values

df = pd.DataFrame({
    'id_start': [829, 829, 829, 826, 826, 826, 825, 825, 825],
    'id_end': [827, 821, 804, 827, 821, 804, 827, 821, 804],
    'distance': [0.0, 0.0, 0.0, 4.1, 0.0, 0.0, 0.0, 0.0, 0.0],
})

reference_value = 829
result_list = find_ids_within_ten_percentage_threshold(df, reference_value)
print(result_list)




def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    
    import pandas as pd

def calculate_toll_rate(distance_df):

    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Calculate toll rates for each vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        column_name = vehicle_type + '_toll'
        distance_df[column_name] = distance_df['distance'] * rate_coefficient

    return distance_df

# Assuming result_unrolled is the DataFrame generated in Question 2
result_with_toll = calculate_toll_rate(result_unrolled)
print(result_with_toll)


   


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
    
    import pandas as pd
import datetime

def calculate_time_based_toll_rates(df):
   
    # Define time ranges and discount factors
    time_ranges_weekdays = [
        (datetime.time(0, 0, 0), datetime.time(10, 0, 0)),
        (datetime.time(10, 0, 0), datetime.time(18, 0, 0)),
        (datetime.time(18, 0, 0), datetime.time(23, 59, 59)),
    ]
    time_ranges_weekends = [
        (datetime.time(0, 0, 0), datetime.time(23, 59, 59)),
    ]

    discount_factors_weekdays = [0.8, 1.2, 0.8]
    discount_factor_weekends = 0.7

    # Apply time-based toll rates
    df['start_day'] = df['end_day'] = df['start_time'] = df['end_time'] = ""
    for index, row in df.iterrows():
        id_start, id_end = row['id_start'], row['id_end']
        time_range_index = index % len(time_ranges_weekdays) if index < len(time_ranges_weekdays) else index % len(time_ranges_weekends)

        if index < len(time_ranges_weekdays):
            start_day, end_day = "Monday", "Friday"
        else:
            start_day, end_day = "Saturday", "Sunday"

        start_time, end_time = time_ranges_weekdays[time_range_index] if index < len(time_ranges_weekdays) else time_ranges_weekends[time_range_index]

        df.at[index, 'start_day'] = start_day
        df.at[index, 'end_day'] = end_day
        df.at[index, 'start_time'] = start_time
        df.at[index, 'end_time'] = end_time

        if start_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            df.at[index, 'distance'] *= discount_factors_weekdays[time_range_index]
        else:
            df.at[index, 'distance'] *= discount_factor_weekends

    return df

# Example usage:
result_with_time_columns = calculate_time_based_toll_rates(result_unrolled)
print(result_with_time_columns)




