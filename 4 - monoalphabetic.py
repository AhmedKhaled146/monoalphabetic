letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
           'o','p','q','r','s','t','u','v','w','x','y','z'] 

keys = ['q','w','e','r','t','y','u','i','o','p','a',
        's','d','f','g','h','j','k','k','l','z','x','c','v','b','n','m']

text = str(input("enter text: ")).lower()

cipher = []
for l in text:
    key_num = letters.index(l) # to know the index where
    new_letter = keys[key_num] # to find in keys the key num
    cipher.append(new_letter) # for takhzeen 
    
encrypt_text = ''.join(cipher) # to group them  
print(encrypt_text)