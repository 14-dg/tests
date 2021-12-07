def compute(N):
    if N<=1:
        return 1
    return N*compute(N-1)

#zeigt 100 Fakultät oder 100!
print(compute(100))
  