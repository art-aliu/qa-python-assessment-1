

var1 = int(input("Enter a number: "))

if var1 % 3 == 0:
		print ("Fizz")
elif var1 % 5 == 0:
		print ("buzz")
elif var1 % [3, 5] == 0:
		print ("fizzbuzz")
else:
		print ("null")

print(var1)


# def vowel_count(str):
  
#     count = 0
    
#     vowel = set("a,e,i,o,u,A,E,I,O,U")
  
#     for alphabet in str:
      
#         if alphabet in vowel:
#             count = count + 1
      
#     print("No. of vowels : ", count)


