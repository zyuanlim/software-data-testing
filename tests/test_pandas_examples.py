import numpy as np

import pandas as pd
from pandas.testing import assert_frame_equal
from src.pandas.functions import calculate_risk_score, categorize_premium
from src.pandas.pandas_examples import transform_insurance_data


def test_calculate_risk_score():
    assert calculate_risk_score(30, 80) == 25
    assert calculate_risk_score(60, 40) == 60
    assert calculate_risk_score(100, 0) == 100
    assert calculate_risk_score(0, 100) == 0
    assert calculate_risk_score(50, 50) == 50
    assert calculate_risk_score(np.nan, 50) is None
    assert calculate_risk_score(50, np.nan) is None


def test_categorize_premium():
    assert categorize_premium(500) == "low"
    assert categorize_premium(1500) == "medium"
    assert categorize_premium(2500) == "high"
    assert categorize_premium(1000) == "medium"
    assert categorize_premium(1999) == "medium"
    assert categorize_premium(2000) == "high"
    assert categorize_premium(np.nan) is None


def test_transform_insurance_data():
    # Create a sample DataFrame
    data = {
        "Age": [30, 45, 60, np.nan],
        "Health Score": [80, 60, 40, 70],
        "Premium Amount": [800, 1500, 2200, np.nan],
    }
    df = pd.DataFrame(data)

    # Apply transformations
    transformed_df = transform_insurance_data(df)

    # Expected results
    expected_df = df.copy()
    expected_df["Risk Score"] = [25.0, 42.5, 60.0, np.nan]
    expected_df["Premium Category"] = ["low", "medium", "high", None]

    # Assert equality
    assert_frame_equal(transformed_df, expected_df)
