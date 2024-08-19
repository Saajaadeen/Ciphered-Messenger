#!/usr/bin/python3
import socket
import threading

def decipher(ciphered_message, first_skip, subsequent_skip):
    original_message = ''
    i = first_skip
    while i < len(ciphered_message):
        if i < len(ciphered_message):
            original_message += ciphered_message[i]
        i += subsequent_skip + 1
    return original_message

def clientHandler(conn, address):
    print("[!] Client connected: ", address)
    try:
        while True:
            
            data = conn.recv(32768).decode()
            if not data:
                print(f"[x] Client {address}, killed its session.")
                break
            
            try:
                count, ciphered_message = data.split('::::', 1)
            except ValueError:
                print(f"[!] Message was too large: {address}")
                continue
            
            count = int(count)
            
            first_skip = count + 1
            subsequent_skip = count * 2
            
            original_message = decipher(ciphered_message, first_skip, subsequent_skip)
            
            if len(ciphered_message) > 1:
                print(f"[+] {address}: {original_message.lower()}")
            if len(ciphered_message) < 1:
                continue
    
    except ConnectionResetError:
        print(f"[x] Client {address} killed its session.")
    finally:
        conn.close()
        print("[/] Waiting for client connection...")

def server():
    host = socket.gethostname()
    port = 8080

    try:
        serverSocket = socket.socket()
        serverSocket.bind((host, port))
        serverSocket.listen(2)
        print("\n[/] Waiting for client connection...")
    except PermissionError:
        print("[!] Please start server as 'sudo'.")    

    try:
        while True:
            conn, address = serverSocket.accept()
            threading.Thread(target=clientHandler, args=(conn, address)).start()
    except KeyboardInterrupt:
        print("[x] Server shutting down...")
    except OSError:
        print("\n")
    
    finally:
        serverSocket.close()
        print("[x] Unbinding socket...")

if __name__ == '__main__':
    server()