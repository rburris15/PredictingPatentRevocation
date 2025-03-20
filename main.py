##%%
from src.data_loader import process_and_save_data

# Load data
df=process_and_save_data(json_path="data/BOA_database_for_exercise_from_2020.json")

# URL example (if data is online)
# process_and_save_data(json_url="https://example.com/BOA_database.json")
#%%
