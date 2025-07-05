"""
GPT prompting and response processing module.
"""

def analyze_with_gpt(log_type: str, error_info: dict, code_context: str) -> dict:
    """
    Mock GPT analysis:
    - Takes parsed error info and code snippet
    - Returns a dummy explanation and suggested fix

    Replace with real OpenAI API calls later.
    """

    explanation = (
        f"The error in your {log_type} build indicates: '{error_info.get('message')}'. "
        f"Check the file '{error_info.get('file')}' around line {error_info.get('line')}."
    )

    suggested_fix = "Please verify imports and method names in the indicated file and line."

    return {
        "explanation": explanation,
        "fix": suggested_fix
    }

