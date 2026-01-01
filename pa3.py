NAMES = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", 
"Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"] 
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19] 

combine_list = lambda l1,l2: dict(zip(l1,l2))
combined_list=(combine_list(NAMES, AGES))
people = lambda n: [key for key, value in combined_list.items() if value == n]

print(combined_list)
print("Dan" in people(18) and  "Cathy" in people(18))
print ('Ed' in people(19) and 'Helen' in people(19) and 'Irene' in people(19) and 'Jack' in people(19) and 'Larry' in people(19)) 
print("Alice" in people(20) and "Frank" in people(20) and 'Gary' in people(20)) 
print(people(21) == ["Bob"]) 
print (people(22) == ["Kelly"]) 
print(people(23) == [])

