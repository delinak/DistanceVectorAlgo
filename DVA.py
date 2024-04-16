#Delina Kiflom
#Michael Tewoldmedhin
import threading
import socket
import random

class DistanceVectorAlgo:
    def __init__(self, matrix):
        self.matrix = matrix

    def network_init(distance_vector):
        sockets = {}

        def setup_conn(): 
            for neighbor in distance_vector:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    neighbor_ip = '127.0.0.1'
                    neighbor_port = random.randint(200,2000)
                    sock.connect((neighbor_ip, neighbor_port))
                    # save sockets
                    sockets[neighbor] = sock
                except Exception as e:
                    print(f"Cannot set up connection")

        setup_conn()

if __name__ == '__main__':
    matrix = []
    filename = 'network.txt'
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbers = line.strip().split()
                row = [int(num) for num in numbers]
                matrix.append(row)
    except FileNotFoundError:
        print(f"Error reading file")

    threads = []
    for node in range(len(matrix)):
        distance_vector = []
        # create neighbor list distance vector
        for i in range (len(matrix)):
            distance_vector.append(matrix[node][i])
        thread = threading.Thread(target=DistanceVectorAlgo.network_init, args=(distance_vector))
        threads.append(thread)
        thread.start()

    

