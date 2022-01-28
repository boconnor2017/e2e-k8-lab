#!/usr/bin/env python
#Run python3 demo-passvar-into-script.py <INT> <INT>
#Will return 'Total: <SUM>

import sys
total = int(sys.argv[1])+int(sys.argv[2])
print("Total: "+str(total))
