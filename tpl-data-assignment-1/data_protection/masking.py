def mask_phone(phone):
    #phone[-2:] antaa merkkijonon 2 viimeistä merkkiä
    #len(phone) antaa merkkijonon pituuden.

    phone_len = len(phone) - 2
    masking_len = "*" * phone_len
    last_two = phone[-2:]
    mask = masking_len + last_two
    return mask
    
def mask_name(name):
    
    name_len = len(name) - 1    
    masking_len = "*" * name_len
    first_letter = name[0]
    mask = first_letter + masking_len
    return mask

if __name__ == "__main__":
    print(mask_phone("1-770-736-8031 x56442"))
    print(mask_name("Leanne Graham"))