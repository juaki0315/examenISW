import socket

def count_palindromes(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word == word[::-1]:
                    count += 1
    return count

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    filename = data.strip()
    count = count_palindromes(filename)
    response = str(count)
    client_socket.send(response.encode())
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print("Server listening on port 8080...")

    while True:
        client_socket, address = server_socket.accept()
        print("Connected with client:", address)
        handle_client(client_socket)

run_server()
