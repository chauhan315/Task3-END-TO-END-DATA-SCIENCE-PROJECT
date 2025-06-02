import pandas as pd
import joblib

# Load saved artifacts
medians = joblib.load('Model/numeric_medians.pkl')
binary_maps = joblib.load('Model/binary_mappings.pkl')

def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Preprocess input data for prediction.
    - data: dict with keys matching form input names
    
    Returns:
    - pd.DataFrame with one row, cleaned and ready for model.
    """

    # Copy data to avoid mutation
    data = data.copy()

    # Map yes/no to 1/0 for binary fields
    for col in ['Stage_fear', 'Drained_after_socializing']:
        val = data.get(col)
        if val is not None:
            # Make lowercase to be safe
            val = val.lower()
            data[col] = binary_maps[col].get(val, 0)
        else:
            # If missing, fill with mode (0)
            data[col] = 0

    # Convert numeric fields to float or int and fill missing with medians
    numeric_cols = ['Time_spent_Alone', 'Social_event_attendance', 'Going_outside', 'Friends_circle_size', 'Post_frequency']
    for col in numeric_cols:
        val = data.get(col)
        if val is None or val == '':
            data[col] = medians[col]
        else:
            if col == 'Friends_circle_size':
                data[col] = int(data[col])
            else:
                data[col] = float(data[col])

    # Create DataFrame with single row
    df = pd.DataFrame([data])

    return df
