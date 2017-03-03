import time
e = 5
n = 299
d = 53

LUT_encryption = dict()
LUT_decryption = dict()
def encrypt_message(msg):
    encrypted_msg = ""
    for letter in msg:
        if letter in LUT_encryption:
            encrypted_msg += LUT_encryption[letter] 
        else :
            numerize = ord(letter) 
            encrypt = pow(numerize, e, n)
            LUT_encryption[letter] = unichr(encrypt)
            encrypted_msg += unichr(encrypt) 
    return encrypted_msg
    
def decrypt_message(msg):
    decrypted_msg = ""
    for number in msg:
        if number in LUT_decryption:
            decrypted_msg += LUT_decryption[number]
            print ("joe")
        else :
            numerize = ord(number)
            decrypt = pow(numerize, d, n)
            LUT_encryption[number] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)
    return decrypted_msg
       
        

start = time.time()
message ="mississippi"
final_encrypted_message = encrypt_message(message)
print final_encrypted_message
print decrypt_message(final_encrypted_message)
end = time.time()
print(end-start)
