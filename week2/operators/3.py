"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
"""
print(12 >> 2)
"""
The << operator moves each bit the specified number of times to the left. Empty holes at the left are filled with 0's.
"""
print(3 << 2)