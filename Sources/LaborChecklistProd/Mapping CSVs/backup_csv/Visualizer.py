import os
import csv
import pandas as pd

def analyze_headers(directory_path):
    """
    Analyze CSV headers from all files in the specified directory and create a summary CSV.
    
    Args:
        directory_path (str): Path to the directory containing CSV files
    """
    # Initialize list to store results
    results = []
    
    # Get all CSV files in the directory
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    
    # Process each CSV file
    for filename in csv_files:
        try:
            # Read the CSV file
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            
            # Get headers
            headers = list(df.columns)
            
            # Pad headers list with None if less than 8 columns
            headers.extend([None] * (8 - len(headers)))
            
            # Create row with filename and headers
            row = {
                'File Name': filename,
                'Column 1 Header': headers[0],
                'Column 2 Header': headers[1] if len(headers) > 1 else None,
                'Column 3 Header': headers[2] if len(headers) > 2 else None,
                'Column 4 Header': headers[3] if len(headers) > 3 else None,
                'Column 5 Header': headers[4] if len(headers) > 4 else None,
                'Column 6 Header': headers[5] if len(headers) > 5 else None,
                'Column 7 Header': headers[6] if len(headers) > 6 else None,
                'Column 8 Header': headers[7] if len(headers) > 7 else None
            }
            
            results.append(row)
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
    
    # Create output DataFrame
    output_df = pd.DataFrame(results)
    
    # Save to new CSV
    output_path = os.path.join(directory_path, 'header_analysis.csv')
    output_df.to_csv(output_path, index=False)
    print(f"Analysis complete. Results saved to: {output_path}")

# Usage
if __name__ == "__main__":
    # Replace with your directory path
    directory_path = r"C:\Users\Faria Shaw\Documents\GitHub\LaborChecklist\MMO_Downloads"
    analyze_headers(directory_path)