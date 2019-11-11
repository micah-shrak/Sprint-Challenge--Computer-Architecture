#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) != 2:
    print("Please submit the filename")
    print(sys.stderr)
    sys.exit(1)

else:

    cpu = CPU()

    cpu.load()
    cpu.run()
