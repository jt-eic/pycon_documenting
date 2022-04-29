import random
import string
from typing import Optional, Iterable

def generate_password(
    chars:int, punctuation:bool, invalid_chars: Optional[Iterable[str]]=None) -> str :
    """Some simple stuff for making a password from some inputs stuff.

    Args:
        chars (int): _description_
        punctuation (bool): _description_
        invalid_chars (Optional[Iterable[str]], optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    
    
    valid_chars = string.ascii_letters + string.digits

    # evaluate any punctuation and add to the characters
    if punctuation:
        valid_chars += string.punctuation

    # any characters that should be removed, if any
    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    # randomly selected characters and combined as a password
    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password


if __name__ == '__main__':
    char1 = input("enter some characters: ")
    punc1 = input("add some punctuation: ")
    invld = input('what could be some invalid stuff?')

    mypswd = generate_password(char1, punc1, invalid_chars=invld)

    print(f" the complete password is: {mypswd}")