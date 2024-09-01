import json
import yaml
import logging

# ===== READ/WRITE DATA FORMAT =====
def read_yaml(file_path: str) -> dict:
    """Reads a YAML file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.   


    Returns:
        dict: The contents of the YAML file as a Python dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML content.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {e}")

# ===== STRING-DICT CONVERSION =====
def json_to_str(payload: dict) -> str:
    """Converts a Python dictionary to a JSON string.

    Args:
        payload (dict): The Python dictionary to convert.

    Returns:
        str: The JSON string representation of the dictionary.
    """
    return json.dumps(payload)

def str_to_json(payload: str) -> dict:
    """Converts a JSON string to a Python dictionary.

    Args:
        payload (str): The JSON string to convert.

    Returns:
        dict: The Python dictionary representation of the JSON string.

    Raises:
        json.JSONDecodeError: If the JSON string is invalid.
    """
    try:
        return json.loads(payload)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}")


# ===== LOGGING SYSTEM =====
def set_logger(level: int = logging.DEBUG, file_path: str = None) -> logging.Logger:
    """Sets up a logger with the specified configuration.

    Args:
        level (int, optional): The logging level. Defaults to logging.DEBUG.
        file_path (str, optional): The path to the log file. If None, logs to the console. Defaults to None.

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    formatter = logging.Formatter('[%(asctime)s] - %(levelname)7s --- %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    if file_path:
        try:
            file_handler = logging.FileHandler(file_path)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error creating log file: {e}")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger  
