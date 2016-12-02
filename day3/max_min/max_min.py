# Function to return list of min and max number in array passed to it.
# If max and min equal, returns number of elements in array.

def find_max_min(numbers):
   max_min=[]
   minimum=min(numbers)
   maximum=max(numbers)
   if maximum == minimum:
       max_min.append(len(numbers))
   else:
       max_min.append(minimum)
       max_min.append(maximum)
   return max_min

print find_max_min([3,6,1,6])
