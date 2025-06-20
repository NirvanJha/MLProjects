import logging
import os 
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_FILE_PATH=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'



)
