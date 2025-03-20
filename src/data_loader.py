import json
import pandas as pd
import requests
import os

def fetch_json_data(json_path=None, json_url=None):
    """
    Fetch JSON data from a local file or a remote URL.

    Args:
        json_path (str, optional): Local path to the JSON file.
        json_url (str, optional): URL to fetch JSON data.

    Returns:
        list: Parsed JSON data.
    """
    if json_url:
        response = requests.get(json_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch JSON data. Status code: {response.status_code}")

    elif json_path and os.path.exists(json_path):
        with open(json_path, "r") as f:
            return json.load(f)
    
    else:
        raise ValueError("Provide either a valid JSON file path or a URL.")

def boa_to_df(boa):
    """Convert a single JSON entry to a Pandas DataFrame row."""
    if len(boa['opponents_reps']) == 0:
        opponents = pd.DataFrame()
    else:
        opponents = pd.concat([
            pd.DataFrame({f"Opponent {i+1}": [v[0]], f"Representative {i+1}": [v[1]]})
            for i, v in enumerate(boa['opponents_reps'])
        ], axis=1)

    return pd.concat([
        pd.DataFrame.from_dict({
            "Decision date": [boa['date']],
            "Case number": [boa['case_number']],
            "Application number": [boa['application_number']],
            "Publication number": [boa['publication_number']],
            "IPC pharma": [boa['IPC pharma']],
            "IPC biosimilar": [boa['IPC biosimilar']],
            "IPCs": [", ".join(boa['IPC'])],
            "Language": [boa['lang']],
            "Title of Invention": [boa['title_of_invention']],
            "Patent Proprietor": [boa['patent_proprietor']],
            "Headword": [boa['headword']],
            "Provisions": [", ".join(boa['provisions'])],
            "Keywords": [", ".join(boa['keywords'])],
            "Decisions cited": [", ".join(boa['decisions_cited'])],
            "Summary": ['\n\n'.join(boa['summary'])],
            "Decision reasons": ['\n\n'.join(boa['decision_reasons'])],
            "Order": [", ".join(boa['order'])],
            "Order status": [boa['Order_status']],
            "Order status web": [boa['Order_status_web']],
            "Order status manual": [boa['Order_status_manual']],
            "Opponents": [", ".join(boa['opponents'])]
        }),
        opponents
    ], axis=1)

def process_and_save_data(json_path=None, json_url=None, output_excel="data/BOA_database.xlsx"):
    """
    Fetch, process, and save JSON data as an Excel file.

    Args:
        json_path (str, optional): Path to the local JSON file.
        json_url (str, optional): URL to fetch the JSON data.
        output_excel (str): Output Excel file name.
    """
    boa_data = fetch_json_data(json_path, json_url)
    boa_table = pd.concat([boa_to_df(boa) for boa in boa_data], axis=0)

    # Save the DataFrame to an Excel file
    boa_table.to_excel(output_excel, index=False)
    print(f"Data successfully saved to {output_excel}")