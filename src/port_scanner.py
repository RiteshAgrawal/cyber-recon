import socket
import sys

def main(ip, port_range='1-1024'):
    # Create a tuple for start and end port
    port_details = map(int, port_range.split('-'))

    for port in range(*port_details):
        # Create a socket of the AF_INET family which
        # takes address of ipaddress and SOCK_STREAM defines
        # TCP socket type
        #TODO: Enhance the comment
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to connect to the given host and port
        result = s.connect_ex((ip, port))

        status = 'Close'
        if result == 0:
            status = 'Open'

        print('{0}: {1}'.format(port, status))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Invalid Arguments')
        sys.exit(1)

    port_range = '1-1024'
    if len(sys.argv) == 3:
        port_range = sys.argv[2]

    main(sys.argv[1], port_range)
