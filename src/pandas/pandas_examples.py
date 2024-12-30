import pandas as pd

from .functions import calculate_risk_score, categorize_premium


def transform_insurance_data(df):
    """
    Apply transformations to the insurance data DataFrame.
    """
    # Calculate risk score
    df["Risk Score"] = df.apply(
        lambda row: calculate_risk_score(row["Age"], row["Health Score"]), axis=1
    )

    # Categorize premium
    df["Premium Category"] = df["Premium Amount"].apply(categorize_premium)

    return df


def main():
    df = pd.read_csv("data/insurance.csv")
    transformed_df = transform_insurance_data(df)


if __name__ == "__main__":
    main()
