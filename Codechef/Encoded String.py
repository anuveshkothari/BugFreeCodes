
encoded_dict = {
    "0000" : 'a',
    "0001" : 'b',
    "0010" : 'c',
    "0011" : 'd',
    "0100" : 'e',
    "0101" : 'f',
    "0110" : 'g',
    "0111" : 'h',
    "1000" : 'i',
    "1001" : 'j',
    "1010" : 'k',
    "1011" : 'l',
    "1100" : 'm',
    "1101" : 'n',
    "1110" : 'o',
    "1111" : 'p',
}

test_cases = int(input())

for i in range(test_cases):
    len_of_encoded_string = int(input())
    encoded_str = input()
    encoded_char = str()

    for j  in range(0, len(encoded_str), 4):
        encoded_char += encoded_dict.get(encoded_str[j:j+4])
    print(encoded_char)