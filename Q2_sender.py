import socket

def sender():
    host = '127.0.0.1'       #Localhost
    port = 12345

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket Created")
        server.connect((host, port))
        print("Socket Connected")

        while True:
            user_input = input("Send message(type 'e' to exit): ")
            server.sendall(user_input.encode())

            if user_input.lower() == 'e':
                break

        server.close()

    except socket.error as err:
        print("\nSocket error: ", err, "-",type(err).__name__)
        
    except KeyboardInterrupt:
        print("\nExiting...")
    
    except Exception as err:
        print("\nAn unexpected error has occured:", err, "-",type(err).__name__)


if __name__ == "__main__":
    sender()
