def g(x):
  def h():
    nonlocal x
    x = x + 7
  x = x + 1
  h()
  return x

x = 3
z = g(x)
print(z)