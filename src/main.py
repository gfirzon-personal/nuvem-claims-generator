import pandas as pd
from tqdm import tqdm

from generator import (
    generate_data, 
    generate_claim_record)

def main(count):
    # Generate the dataset
    #data = [generate_data() for _ in tqdm(range(num_records), desc="Generating Records")]
    data = [generate_claim_record() for _ in tqdm(range(count), desc="Generating Records")]

    # Convert to a DataFrame and save as CSV
    df = pd.DataFrame(data)

    output_file = f"test_claim_set_{count}.csv"
    df.to_csv(output_file, index=False)

    print(f"CSV file '{output_file}' with {count:,} records created successfully!")

if __name__ == "__main__":
    user_entry = input("Enter the number of records to generate: ")
    num_records = int(user_entry.replace(",", ""))

    main(num_records)
