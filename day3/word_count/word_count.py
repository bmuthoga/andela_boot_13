# Function to count frequency of occurrence of a word in a string

def words(word):
   words = word.split()
   string_dict = {}
   for word in words:
       if word.isdigit():
           word = int(word)
       if word in string_dict:
           string_dict[word]+=1
       else:
           string_dict[word] = 1
   return string_dict
