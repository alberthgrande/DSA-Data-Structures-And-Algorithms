"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

"""
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	                                                Example	
and 	    Returns True if both statements are true	                x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
"""

"""
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	                                                Example
is 	        Returns True if both variables are the same object	        x is y	    => refers to the memory
is not	    Returns True if both variables are not the same object	    x is not y  => refers to the memory
"""

"""
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	                                                                            Example
in 	        Returns True if a sequence with the specified value is present in the object	        x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	    x not in y
"""

"""
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	                    Description	                                                                                                Example	
& 	        AND	                        Sets each bit to 1 if both bits are 1	                                                                    x & y	
|	        OR	                        Sets each bit to 1 if one of two bits is 1	                                                                x | y	
^	        XOR	                        Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y	
~	        NOT	                        Inverts all the bits	                                                                                    ~x	
<<	        Zero fill left shift	    Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
>>	        Signed right shift	        Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2
"""

# Bitwise &
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


# Bitwise |
print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


# Bitwise ^
print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


# Bitwise ~
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""


# Bitwise <<
print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


# Bitwise >>
print(8 >> 2)

"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""