import socket


class SocketWrapper(object):
    def __init__(self, server, port=43):
        self.server = server
        self.port = port

    def get_details(self, data):
        # Creating a python socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connecting to the server
        s.connect((self.server, self.port))

        data += '\r\n'

        # Sending data to the server
        s.send(data.encode())
        message = ''

        # Receiving data from server
        while True:
            return_data = s.recv(50000)
            if not return_data:
                break

            message += return_data.decode('utf-8', 'ignore')

        return message


def main():
    domain = input('Enter Domain: ')
    # https://raw.githubusercontent.com/whois-server-list/whois-server-list/master/whois-server-list.xml
    domain_server = 'whois.verisign-grs.com'
    print(domain)
    details = SocketWrapper(domain_server).get_details(domain)
    print( details)


if __name__ == '__main__':
    main()
