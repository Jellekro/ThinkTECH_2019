from  SmartBlock import SmartBlock
import datetime
import json

class SmartBlockChain:

    def __init__(self, user_name, file_name):
        self.user_name = user_name
        self.file_name = file_name
        self.first = SmartBlock.create_genesis_block()
        self.size = 1
        self.last = self.first
        self.build_block_chain()

    def build_block_chain(self):
        file_reader = open(self.file_name, "r")
        json_text = file_reader.read()
        file_reader.close()
        json_object = json.loads(json_text)
        json_array = json_object[self.user_name]
        for block in json_array:
            self.add(block)

    def add(self, json_object):
        self.last = SmartBlock(self.last, json_object["score_delta"], json_object["factor_type"], json_object["data"],
                           datetime.datetime.now())
        self.size += 1

    def get_last(self):
        return self.last

    def decode_block_chain(self):
        json_array = []
        curr_block = self.last
        while curr_block.prev_SmartBlock!=None:
            json_object = {"score_delta":curr_block.score_delta, "factor_type":curr_block.factor_type, "data":curr_block.data}
            json_array.append(json_object)
            curr_block = curr_block.prev_SmartBlock
        return {self.user_name:json_array}