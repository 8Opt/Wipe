import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from wipe.helpers import read_yaml

load_dotenv()

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

def setup_api_key(): 
    """ Setup API key
    """
    os.environ['TAVILY_API_KEY'] = os.getenv('TAVILY_API_KEY')
    os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
    os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')


def get_config(path:str='./config.yaml') -> dict: 
    """Get .yaml configuration file. 

    Args:
        path (str, optional):  Defaults to './config.yaml'.

    Returns:
        dict: the config file.
    """
    config = read_yaml(path)
    return config