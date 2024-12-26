import json


class JsonResult:
    """
    Represents the outcome of reading/parsing a JSON file:
    - success: A boolean indicating if the operation succeeded.
    - data: Holds the successfully parsed JSON as a dictionary, if any.
    - error: An error message if the operation failed.
    """

    def __init__(self, success, data=None, error=None):
        self.success = success
        self.data = data
        self.error = error

    def __repr__(self):
        if self.success:
            return f"JsonResult(success=True, data={self.data})"
        return f"JsonResult(success=False, error='{self.error}')"


def read_json_file(file_path):
    """
    Attempts to open and parse a JSON file, returning a JsonResult object.
    - If successful, contains the parsed data as a Python dictionary.
    - If the file is missing or invalid JSON, it returns a failure with an error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            parsed_data = json.loads(contents)
            return JsonResult(success=True, data=parsed_data)
    except FileNotFoundError:
        return JsonResult(success=False, error=f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        return JsonResult(success=False, error=f"File '{file_path}' contains invalid JSON.")
    except Exception as e:
        return JsonResult(success=False, error=str(e))


def file_result_simulator():
    result_company = read_json_file("company_config.json")
    if result_company.success:
        print("[Company Config - Success]")
        print("Parsed data:", result_company.data)
    else:
        print("[Company Config - Error]")
        print("Issue:", result_company.error)

    result_user = read_json_file("user_config.json")
    if result_user.success:
        print("[User Config - Success]")
        print("Parsed data:", result_user.data)
    else:
        print("[User Config - Error]")
        print("Issue:", result_user.error)

    result_broken = read_json_file("broken_config.json")
    if result_broken.success:
        print("[User Config - Success]")
        print("Parsed data:", result_broken.data)
    else:
        print("[Broken Config - Error]")
        print("Issue:", result_broken.error)

    result_missing = read_json_file("missing_config.json")
    if result_missing.success:
        print("[Missing Config - Success]")
        print("Parsed data:", result_missing.data)
    else:
        print("[Missing Config - Error]")
        print("Issue:", result_missing.error)


if __name__ == "__main__":
    file_result_simulator()
