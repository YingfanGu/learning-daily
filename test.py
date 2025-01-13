strs = ["eat"]
key = sorted(strs)
print(key)
    
    
    
for s in strs:
    print(s)
    key = sorted(s)
    print(key)
            
            
key = ''.join(s)
my_dict = {key: "value"}  # TypeError: unhashable type: 'list'
my_dict


("age", 25) in my_dict.items()




my_dict.items()


s = "dog cat cat dog"
words = s.split(' ')