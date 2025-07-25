import re
import pandas as pd

def convert_claim_items(input_file_path, output_file_path):
    # Read the input text from a .txt file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Updated regex to capture the upper limit and medication name
    pattern = r'Claim item has 1 to (\d+)\s+of\s+"(.*?)"'

    # Find matches
    matches = re.findall(pattern, input_text)
    print(f"Matches found: {len(matches)}")

    # Build output lines
    output_lines = [f'put("{medication}", {quantity});' for quantity, medication in matches]

    # Save to Excel
    df = pd.DataFrame(output_lines, columns=['limit'])
    df['limit'] = df['limit'].str.strip()
    df.to_excel(output_file_path, index=False)

    print(f"Processed list saved to {output_file_path}")


# Example usage
input_txt_file = 'input.txt'
output_excel_file = 'medications.xlsx'

convert_claim_items(input_txt_file, output_excel_file)