import socket

def receiver():
    host = '127.0.0.1'       #Localhost
    port = 12345
    n_conn = 2

    try:
        receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Initializing socket
        receiver.bind((host, port))
        receiver.listen(n_conn)                 #n connections are kept waiting, increase as per requirement
        conn, address = receiver.accept()
        print("Connected to", address)

        while True:
            rec_msg = conn.recv(1024)           #1024 can be increased if expected message is longer
            print("Received message:", rec_msg.decode())

        conn.close()
        receiver.close()

    except socket.error as err:
        print("\nSocket error: ", err, "-",type(err).__name__)
        
    except KeyboardInterrupt:
        print("\nExiting...")
    
    except Exception as err:
        print("\nAn unexpected error has occured:", err, "-",type(err).__name__)

if __name__ == "__main__":
    receiver()
