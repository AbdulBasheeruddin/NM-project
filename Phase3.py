import pandas as pd
import numpy as np

# Define a function for quality control
def quality_control(df, spec_ranges):
    """
    Perform quality control by checking if product attributes fall within specified ranges.
    
    :param df: DataFrame containing product attributes
    :param spec_ranges: Dictionary with attribute names as keys and tuples with (min_value, max_value) as values
    :return: DataFrame with a quality status (Pass/Fail) for each product
    """
    quality_status = []

    for _, row in df.iterrows():
        status = "Pass"
        for attribute, (min_val, max_val) in spec_ranges.items():
            if not (min_val <= row[attribute] <= max_val):
                status = "Fail"
                break
        quality_status.append(status)

    df["Quality_Status"] = quality_status
    return df

# Sample data: Product ID, Weight, Size
data = {
    'Product_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Weight': [12.5, 15.1, 11.2, 14.0, 16.1],   # in kilograms
    'Size': [20, 22, 19, 21, 23]                # in centimeters
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define quality control specifications
specifications = {
    'Weight': (12.0, 15.0),  # Weight should be between 12.0 and 15.0 kg
    'Size': (20, 22)         # Size should be between 20 and 22 cm
}

# Apply quality control
df_quality = quality_control(df, specifications)

# Output the result
print(df_quality)
