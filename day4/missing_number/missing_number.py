# Function that when passed two arrays of positive integers
# returns missing number in one of the arrays and not the other.
# Returns 0 if both arrays empty both have the same numbers.

def find_missing(first_array, second_array):
  first_array = set(first_array)
  second_array = set(second_array)
  if first_array != second_array:
      final_array = list(second_array - first_array)
      for element in final_array:
          return element
  else:
      return 0
