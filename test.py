#!/usr/bin/env python3
import os

test_stage = os.getenv("TEST_STAGE")

print(f"test stage: {test_stage}")
print("OK")