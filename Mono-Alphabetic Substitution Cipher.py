from re import sub


def substitution_cypher_encryption(text,key):
        alphapet="abcdefghijklmnopqrstuvwxyz"
        result=""
        for letter in text:
            if letter in alphapet:
                result+=key[alphapet.find(letter)]
            else:
                result+=letter
        print(result)

        
def substitution_cypher_decryption(text,key):
        alphapet="abcdefghijklmnopqrstuvwxyz"
        result=""
        for letter in text:
            if letter in key:
                result+=alphapet[key.find(letter)]          
            else:
                result+=letter
        print(result)






##cipher_text=substitution_cypher_encryption("abc de","lorfwsevamcpndbqgjtyiuxhzk")
##print(cipher_text)

plain_text=substitution_cypher_decryption("fbooatlsjwwwps","lorfwsevamcpndbqgjtyiuxhzk")
print(plain_text)