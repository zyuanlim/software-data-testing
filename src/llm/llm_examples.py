import json

from dotenv import load_dotenv
from litellm import completion

load_dotenv()


def extract_cv_data(text: str) -> dict:
    """
    Extract CV information from text.

    Args:
        text (str): Input CV text to extract data from

    Returns:
        dict: structured CV data
    """
    prompt = f"Extract CV information from the text:\n{text}"

    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        json_data = json.loads(response.choices[0].message.content)
        return json_data
    except (json.JSONDecodeError, ValueError) as e:
        raise ValueError(f"Failed to parse CV data: {str(e)}")
