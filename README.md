<center><h1>Python Server/Client Cipher Messenger</h1></center>

This server and client program is used to send ciphered messages to clients connected to the server, the server cannot by default send messages but clients may send messages to the server anyway they like and as long as the client is using the correct format in the packet that is sent to the server it should be able to decipher the meesage and display to the clients connected to the server.

<center><h1>Program Description</h1></center>

The messages transmitted to the server are obfuscated through a rudimentary ciphering technique, where random characters are inserted both before and after each character of the original message. The number of these inserted characters varies, and the case of the letters in the message is randomly altered, further disguising the content. Despite these modifications, the message remains technically in plain text, but it is rendered unintelligible to the human eye.

The deciphering process relies on a specific pattern embedded within the transmitted packet, as neither the server nor the client possesses an encryption key. This pattern, included in the packet, is essential for decoding the message. Without knowledge of this pattern, the message appears as random noise. However, once the server applies the pattern, the original message is reconstructed and can be displayed to other connected clients.

# Run the Program
You need to run the server as `sudo` since the socket is being used to listen to clients. Use the command in a linux terminal `sudo ./server.py` to start the server, which should then be running and listening for client connections.

After the server is started, run the client software with `./client.py`, which will connect to the server immediately. You should now be able to send messages to the server.

<center><h1>Authors</h1></center>

This project was created and maintained by Saajaadeen M. Jeffries
