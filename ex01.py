"""
  >>> type(thing1)
  <class 'list'>
  >>> type(thing2)
  <class 'tuple'>
  >>> type(thing3)
  <class 'str'>
"""
thing1 = [1, 2]
thing3 = "happy"
thing2 = ('a', 'b')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
