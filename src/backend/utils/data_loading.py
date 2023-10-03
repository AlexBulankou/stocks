from google.cloud import bigquery
from google.oauth2 import service_account

def load_data(project_id, query):
    """
    Load data from BigQuery into a DataFrame.

    :param project_id: The GCP project ID.
    :param query: SQL query to fetch data from BigQuery.
    :return: Loaded DataFrame.
    """

    # Set up BigQuery client with credentials
    client = bigquery.Client(project=project_id)

    # Load the dataset from BigQuery
    df = client.query(query).to_dataframe()

    # Display information about the loaded data
    _display_data_info(df)

    return df

def _display_data_info(df):
    """
    Display column information, row count, and sample rows for a DataFrame.

    :param df: DataFrame to display information about.
    """

    # Enumerate all columns
    print("Columns:")
    for idx, column in enumerate(df.columns, 1):
        print(f"{idx}. {column}")

    # List row count
    print(f"\nTotal Rows: {len(df)}")

    # List 2 sample rows
    print("\nSample Rows:")
    print(df.sample(2))
