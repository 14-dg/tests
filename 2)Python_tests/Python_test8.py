def round_sum(a, b, c):
  total=a, b, c
  ans=0
  for i in total:
     ans+=round(round(i, -1), None)
  return ans

print(round_sum(4, 5.1, 14.44444444445))
