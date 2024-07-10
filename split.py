import pandas as pd

# Load the Excel file with headers
input_file_path = 'extracted.xlsx'
df = pd.read_excel(input_file_path)

# Function to split the values in the 'Amount' column and handle errors
def split_values(val):
    parts = str(val).rsplit(' ', 1)
    if len(parts) == 2:
        return parts[0].replace(',', ''), parts[1].replace(',', '')
    else:
        return None, None

# Split the values in the 'Amount' column into two new columns
split_cols = df['Amount'].apply(split_values).apply(pd.Series)
split_cols.columns = ['Amount', 'Balance Remaining']

# Add " Dr" to the end of each value in the 'Balance Remaining' column, handling None values
split_cols['Balance Remaining'] = split_cols['Balance Remaining'].apply(lambda x: f"{x} Dr" if pd.notna(x) else x)

# Insert the new columns immediately after the original 'Amount' column
df = pd.concat([df.iloc[:, :2], split_cols, df.iloc[:, 3:]], axis=1)

# Save the updated DataFrame to a new Excel file preserving headers
output_file_path = 'ExtractedTable.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Updated Excel file saved as '{output_file_path}'.")
