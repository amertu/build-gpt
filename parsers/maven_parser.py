import re

import re

def parse_maven_log(log_text: str) -> dict | None:
    # Regex to capture file path, line number, and message from the first error line
    pattern = re.compile(r"\[ERROR\] ([^\[]+\.java):\[(\d+),\d+\] (.+)")
    lines = log_text.splitlines()
    for i, line in enumerate(lines):
        print(line)
        match = pattern.match(line)
        if match:
            file_path = match.group(1).strip()
            line_num = int(match.group(2))
            message = match.group(3).strip()
            return {
                "file": file_path,
                "line": line_num,
                "message": message
            }
    return None


