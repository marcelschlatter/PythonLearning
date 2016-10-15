def Encode(input_string):
    
    Original_message = input_string.ljust((3-len(input_string)%3)+len(input_string))
       
    part1 = Original_message[::3]
    part2 = Original_message[1::3]
    part3 = Original_message[2::3]

    Encoded_message = part1 + part2 + part3
    
    return Encoded_message