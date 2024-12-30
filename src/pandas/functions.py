import pandas as pd


def calculate_risk_score(age, health_score):
    """
    Calculate a risk score based on age and health score.
    """
    if pd.isna(age) or pd.isna(health_score):
        return None
    return min(100, max(0, age * 0.5 + (100 - health_score) * 0.5))


def categorize_premium(premium_amount):
    """
    Categorize premium amount into low, medium, or high.
    """
    if pd.isna(premium_amount):
        return None
    if premium_amount < 1000:
        return "low"
    elif premium_amount < 2000:
        return "medium"
    else:
        return "high"


def calculate_loyalty_score(insurance_duration, customer_feedback):
    """
    Calculate a loyalty score based on insurance duration and customer feedback.

    :param insurance_duration: Number of years the customer has been insured
    :param customer_feedback: Customer feedback (Poor, Average, Good)
    :return: Loyalty score between 0 and 100
    """
    if pd.isna(insurance_duration) or pd.isna(customer_feedback):
        return None

    # Base score from insurance duration (0-50 points)
    duration_score = min(50, insurance_duration * 10)

    # Additional score from customer feedback (0-50 points)
    feedback_score = {"Poor": 0, "Average": 25, "Good": 50}.get(customer_feedback, 0)

    return duration_score + feedback_score
