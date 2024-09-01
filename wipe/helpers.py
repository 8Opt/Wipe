import json
import yaml

# ===== READ/WRITE DATA FORMAT =====
def read_yaml(file_path):
  with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
  return data


# ===== STRING-DICT CONVERSION =====
def json_to_str(payload:dict) -> str: 
  result = json.dumps(payload)
  return result

def str_to_json(payload:str) -> dict: 
  result = json.loads(payload)
  return result