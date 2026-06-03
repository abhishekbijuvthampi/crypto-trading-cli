import logging

def get_logger(name ="api_logger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger
    
    file_handler = logging.FileHandler("data/app.log")
    formatter = logging.Formatter("%(asctime)s \n %(levelname)s\n%(message)s\n\n")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger