#!/usr/bin/env python

import sys
import json
from printer import mimo_print


json_file = sys.argv[1] 

with open(json_file) as f:
    user_data = json.load(f)
    mimo_print(user_data)
    f.close()



