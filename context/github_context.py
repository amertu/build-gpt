"""
Fetch code snippets from GitHub API.
"""

def get_code_context(file_path: str, line_number: int, window: int = 5) -> str:
    """
    Stub: returns dummy code context for testing purposes.

    In a real implementation, this would:
    - Use GitHub API to fetch the file content
    - Extract a window of lines around the error line

    Parameters:
        file_path (str): Relative file path in repo
        line_number (int): Line number of error (1-based)
        window (int): Number of lines before and after to include

    Returns:
        str: Code snippet
    """
    # This is just for demo/testing – simulate 10 lines of code
    dummy_code = "\n".join([
        f"{i+1}: System.out.println(\"Line {i+1}\");"
        for i in range(line_number - window - 1, line_number + window)
    ])

    return dummy_code

