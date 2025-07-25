import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
csv_path = os.getenv("csv_path")

def generate_put_statements(csv_path: str) -> None:
    """
    Reads a CSV file with columns 'Claim_text' and 'max_qty', and prints each row as a formatted statement:
    put("Claim_text", max_qty);
    Also saves the output to 'output_csv.csv'.

    Parameters:
    ----------
    csv_path : str
        Path to the CSV file. The file must contain 'Claim_text' and 'max_qty' columns.

    Example Output:
    ---------------
    put("Arteeter", 3);
    put("Arteether", 3);
    """
    
    df = pd.read_csv(csv_path)

    output_lines = []

    print("****working magic****")
    for _, row in df.iterrows():
        key = str(row['Claim_text']).strip().replace('"', r'\"')  # escape double quotes
        value = int(row['max_qty']) if pd.notnull(row['max_qty']) else 0
        line = f'put("{key}", {value});'
        print(line)
        output_lines.append(line)

    # Save to output_csv.csv
    pd.DataFrame({'put_statement': output_lines}).to_csv('output_csv.csv', index=False)
    print("job done")

generate_put_statements(csv_path)