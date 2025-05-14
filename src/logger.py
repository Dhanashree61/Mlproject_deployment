import logging
import os
from datetime import datetime

LOG_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs',LOG_file)
os.makedirs(logs_path,exist_ok= True)

Log_File_path = os.path.join(logs_path,LOG_file)

logging.basicConfig(
    filename=Log_File_path ,
    level = logging.INFO
)

# if __name__ == "__main__":
#     logging.info("Logging has started")