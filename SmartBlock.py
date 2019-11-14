import hashlib
import datetime
import json

class SmartBlock:
    def __init__(self, prev_SmartBlock, score_delta, factor_type, data, timestamp):
        self.prev_SmartBlock = prev_SmartBlock
        self.score_delta = score_delta
        self.factor_type = factor_type
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()

    #staticmethod
    def create_genesis_block():
        return SmartBlock(None, 0, "", {}, datetime.datetime.now())

    def get_hash(self):
        header_bin = (str(self.prev_SmartBlock) +
                      str(self.score_delta) +
                      str(self.factor_type) +
                      str(self.data) +
                      str(self.timestamp)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    def get_prev_SmartBlock(self):
        return self.prev_SmartBlock

    def get_score_delta(self):
        return self.score_delta

    def get_factor_type(self):
        return self.factor_type

    def get_data(self):
        return self.data