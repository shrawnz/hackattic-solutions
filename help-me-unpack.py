from utils import *
import json
from struct import unpack

input = json.loads(get_challenge("help_me_unpack"))
print(input)
input_bytes = base64decode(input["bytes"])

output = {}

# https://docs.python.org/3/library/struct.html

output["int"] = unpack("i", input_bytes[:4])[0]
output["uint"] = unpack("I", input_bytes[4:8])[0]
output["short"] = unpack("h", input_bytes[8:10])[0]
output["float"] = unpack("f", input_bytes[12:16])[0]
output["double"] = unpack("d", input_bytes[16:24])[0]
output["big_endian_double"] = unpack("!d", input_bytes[24:32])[0]

result = submit_challenge("help_me_unpack", json.dumps(output))
print(result)
