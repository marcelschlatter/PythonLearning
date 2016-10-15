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