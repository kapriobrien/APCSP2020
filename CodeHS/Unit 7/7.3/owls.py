def owl_count(text):
    owl_count = 0
    char_check = 0
    realText = text.lower()
    for char in list(realText):
        if char == 'o' or char == 'w' or char == 'l':
            char_check += 1
            if char_check == 3:
                owl_count += 1
        else:
            char_check = 0
    print(owl_count)
    return owl_count
            
        
owl_count('I love owls, owl is cool, owl owl owl')
