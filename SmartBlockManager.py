from SmartBlockChain import SmartBlockChain
from SmartBlock import SmartBlock

user_name = "user1"
file_name = "UserData.json"

chain = SmartBlockChain(user_name, file_name)

for i in chain.decode_block_chain()[user_name]:
    print("Your score delta is {}, your factor type is {}, and here is all the extra data: {}".format(i["score_delta"], i["factor_type"], i["data"]))