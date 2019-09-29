import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 9001))

last_message = ''

while last_message != 'see ya':

    expected_data_size = int(sock.recv(4).decode())
    print("Len = {} \n".format(expected_data_size))

    received_data = ''
    while len(received_data) < expected_data_size:
        received_data += sock.recv(4).decode()

    print(received_data)

    message = received_data
    if last_message == 'see ya':
        break

    message = raw_input("message: ").strip()
    length = len(message)

    sock.sendall(str(length).zfill(4).encode())

    sock.sendall(message.encode())

sock.close()
