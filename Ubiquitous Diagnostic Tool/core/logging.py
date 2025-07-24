import logging
from collections import deque

class UDSLogger:
    def __init__(self, log_file='uds_tool.log', buffer_size=100):
        self.logger = logging.getLogger('UDSLogger')
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.buffer = deque(maxlen=buffer_size)

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)
        self.buffer.append((level, message))

    def get_recent(self, n=10):
        return list(self.buffer)[-n:] 