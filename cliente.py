import socket

def run_client():
    server_address = ('localhost', 8080)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    filepath = input("Enter the file path: ")
    client_socket.send(filepath.encode())

    response = client_socket.recv(1024).decode()
    print("Number of palindromes:", response)

    client_socket.close()

run_client()
