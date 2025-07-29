import dis


def double_1(x: int) -> int:
    return x * x


def double_2(x: int) -> int:
    return x**2


def double_3(x: int) -> int:
    return pow(x, 2)


print(dis.dis(double_1))
print(dis.dis(double_2))
print(dis.dis(double_3))

"""
  4           0 RESUME                   0

  5           2 LOAD_FAST                0 (x)
              4 LOAD_FAST                0 (x)
              6 BINARY_OP                5 (*)
             10 RETURN_VALUE
None
  8           0 RESUME                   0

  9           2 LOAD_FAST                0 (x)
              4 LOAD_CONST               1 (2)
              6 BINARY_OP                8 (**)
             10 RETURN_VALUE
None
 12           0 RESUME                   0

 13           2 LOAD_GLOBAL              1 (NULL + pow)
             12 LOAD_FAST                0 (x)
             14 LOAD_CONST               1 (2)
             16 CALL                     2
             24 RETURN_VALUE
None
"""

"""
# From: https://github.com/python/cpython/blob/4e40f2bea7edfa5ba7e2e0e6159d9da9dfe4aa97/Lib/operator.py#L132C1-L134C18
def pow(a, b):
    "Same as a ** b."
    return a ** b
"""
