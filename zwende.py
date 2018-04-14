#!/usr/bin/env python

import binascii

BINARY_ONE = '\u200c'  # Zero Width Joiner (ZWJ)
BINARY_ZERO = '\u200d'  # Zero Width Non-Joiner (JWNJ)
#BINARY_ONE = '\u00a9'
#BINARY_ZERO = '\u00ae'
UNICODE_FORMAT = 'utf-8'


def enzero(text_to_hide: str, plain_text: str):
    # Convert text_to_hide into string of binary digits
    binary_text = bin(int.from_bytes(text_to_hide.encode(), 'big'))

    # Convert binary_text to zero width character equivalents
    zw_encoded_message = ""
    for char in binary_text:
        if char == '1':
            zw_encoded_message += BINARY_ONE
        elif char == '0':
            zw_encoded_message += BINARY_ZERO

    """
    Insert the text_to_hide right before the first "space" in plain_text.
    If there is no space in the plain_text then append to end.
    """
    position = plain_text.find(" ")
    if position > 0:
        encrypted_text = plain_text[:position + 1] + str(zw_encoded_message) + plain_text[position + 1:]
    else:
        encrypted_text = plain_text + zw_encoded_message

    return encrypted_text


def dezero(encrypted_text: str):
    # Strip visible text and decode zero width characters into a binary string
    binary_string = ''
    text_array = [char for char in encrypted_text]
    for char in text_array:
        if char == BINARY_ZERO:
            binary_string += '0'
        elif char == BINARY_ONE:
            binary_string += '1'

    # Convert binary_string into ASCII
    binary_string = int(binary_string, 2)
    print("binary_string  type = {}".format(type(binary_string)))
    return_to_text = binary_string.to_bytes((binary_string.bit_length() + 7 // 8), 'big').decode()

    return return_to_text


def main():
    # Hide a message
    message_to_hide = input("What is your message you wish to hide? ")
    plain_text_message = input("What is your visible message? ")
    message = enzero(message_to_hide, plain_text_message)
    print("The message with the embedded hidden message is:\n{}".format(message))

    # Get the hidden message
    user_inputted_message = input("Paste in the message with the embedded hidden message: ")
    exposed_message = dezero(user_inputted_message)
    print("The hidden message is:\n{}".format(exposed_message))

    for c in exposed_message:
        print("c = {}".format(ord(c)))


if __name__ == "__main__":
    main()
