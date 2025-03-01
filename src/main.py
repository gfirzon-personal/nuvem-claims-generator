import os
import pandas as pd
from tqdm import tqdm

from generator import (generate_claim_record)

def main(count):
    # Define the directory containing the text file and the persistent directory
    data_dir = "/app/data"

    output_file_name = f"test_claim_set_{count}.csv"
    output_file_name_json = f"test_claim_set_{count}.json"

    # Define the directory containing the text file and the persistent directory
    #current_dir = os.path.dirname(os.path.abspath(__file__))
    persistent_directory = os.path.join(data_dir, "output")    
    output_csv_file_path = os.path.join(persistent_directory, output_file_name)
    output_json_file_path = os.path.join(persistent_directory, output_file_name_json)

    # Create the persistent directory if it does not exist
    if not os.path.exists(persistent_directory):
        os.makedirs(persistent_directory)

    # Generate the dataset
    data = [generate_claim_record() for _ in tqdm(range(count), desc="Generating Records")]

    # Convert to a DataFrame 
    df = pd.DataFrame(data)

    # Save the DataFrame as CSV
    df.to_csv(output_csv_file_path, index=False)

    # Save the DataFrame as JSON
    #df.to_json(output_json_file_path, orient='records', lines=True)
    df.to_json(output_json_file_path, orient='records')

    print(f"CSV file '{output_file_name}' with {count:,} records created successfully!")
    print(f"JSON file '{output_file_name_json}' with {count:,} records created successfully!")

if __name__ == "__main__":
    user_entry = input("Enter the number of records to generate: ")
    num_records = int(user_entry.replace(",", ""))

    main(num_records)
