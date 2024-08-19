#!/usr/bin/python3
import socket
import time
import random
import string

array_str_upper = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
array_str_lower = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
array_int = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
array_spc = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '_', '=', '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '?', '/', '|', '\\', '~', '`']

def cipher(message, count):

    ciphered_message = random.choice(array_str_lower)

    for char in message:
        for _ in range(count):
            array_choice = random.choice([array_str_lower, array_str_upper, array_int, array_spc])
            ciphered_message += random.choice(array_choice)

        if random.choice([True, False]):
            char = char.upper()
        else:
            char = char.lower()

        ciphered_message += char

        for _ in range(count):
            array_choice = random.choice([array_str_upper, array_str_lower, array_int, array_spc])
            ciphered_message += random.choice(array_choice)
    return ciphered_message

def client():
    
    try:
        host = socket.gethostname()
        port = 8080
        clientSocket = socket.socket()
        clientSocket.connect((host, port))
        print("[+] Connected to server!")

        username_count = 10
        username = ''.join(random.choices(string.ascii_lowercase + 
                                          string.ascii_uppercase +
                                          string.ascii_letters +
                                          string.digits +
                                          string.punctuation, k=username_count))

        while True:
            message = input(f"{str(username)}:~$ ")
            count = random.randint(250,500)

            if len(message) < 8:
                count > 250
            if len(message) > 1:
                count > 350

            ciphered_message = f"{count}::::{cipher(message, count)}"
            clientSocket.send(ciphered_message.encode())

    except KeyboardInterrupt:
        print("\n[x] Client Shutting down...")
        clientSocket.close()
    except ConnectionRefusedError:
        time.sleep(3)
        print("\n[x] Connection refused.")
    except BrokenPipeError:
        print("\n[!] Session broken.")
    except ConnectionResetError:
        print("\n[!] Server connection reset.")

if __name__ == '__main__':
    client()