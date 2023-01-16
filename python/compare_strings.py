"""
Compare two strings in python
eg hello and heoll should be equal

"""

def compareString(str1, str2):
   if len(str1) != len(str2):
      print("Strings not the same. They are of different lengths...")
      return False

   str1=str1.lower()
   str2=str2.lower()

   str1=''.join(sorted(str1))
   str2=''.join(sorted(str2))

   for i in range(len(str1)):
      if str1[i] != str2[i]:
         print("Strings not the same")
         return False
   print("Strings are the same")
   return True


compareString("Hello", "oLHel")