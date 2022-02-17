def same_first_last(nums):
  first_number=nums[0]
  if nums[-1]==first_number:
    return first_number
  else:
    return "no"

print(same_first_last([1, 3, 5, 14]))
