def machine():
    keys = "abcdefghijklmnopqrstuvwxyz *"
    value = keys[-1] + keys[0:-1]

    encrytDict = dict(zip(keys,value))
    decryptDict = dict(zip(value,keys))

    message = input("Please enter your secret message:")
    mode = input("Please entre the mode: Encode(E) or Decode(D)")

    if mode.upper() == "E":
        newMessage =''.join([encrytDict.get(letter,letter)
                              for letter in message.lower()])
    elif mode.upper() == "D":
        newMessage =''.join([decryptDict.get(letter,letter) 
                              for letter in message.lower()])
    else:
        print("Please enter the correct choice")
        return
    
    return newMessage

print(machine())