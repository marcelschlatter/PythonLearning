
# coding: utf-8

# In[216]:

def Encode(input_string):
    
    Original_message = input_string.ljust((3-len(input_string)%3)+len(input_string))
       
    part1 = Original_message[::3]
    part2 = Original_message[1::3]
    part3 = Original_message[2::3]

    Encoded_message = part1 + part2 + part3
    
    return Encoded_message


# In[217]:

def Decode(input_string):
    
    L=len(input_string)//3
    a,b,c = input_string[0:L], input_string[L:2*L], input_string[2*L:3*L]

    la=list(a)
    lb=list(b)
    lc=list(c)

    Decoded_message = [" "]

    L=len(input_string)-1
    count = 0
    
    while (count < L): 
        Decoded_message.append(" ") 
        count = count + 1

    Decoded_message[::3]=la
    Decoded_message[1::3]=lb
    Decoded_message[2::3]=lc
   
    return "".join(Decoded_message)


# In[221]:

encoded = Encode ("eva hadimegagern")
print(encoded)
decoded = Decode(encoded)
print(decoded)


# In[220]:

decoded = Decode(Encode("Annabelle du bist so unkonventionell"))
print(decoded)

# In[ ]:



