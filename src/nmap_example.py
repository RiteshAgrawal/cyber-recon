import nmap

def main():
    # Host to scan
    host = '127.0.0.1'

    # Create instance of nmap port scanner
    nm = nmap.PortScanner()

    print('------------- Starting Scan --------')
    # Start scan
    nm.scan(host, arguments='-A')
    print('---------- Host State -------------')

    # Check the host state whether host is up or not
    print(nm[host].state())

    print('---------- Open Ports List ---------')

    # Get all the open tcp ports
    print(','.join(map(str, nm[host]['tcp'].keys())))

    # https://www.stationx.net/nmap-cheat-sheet/

    # Get Details of open  tcp ports
    for port, value in nm[host]['tcp'].items():
        print('---------- Details for port {0}------------'.format(port))
        for i,j in value.items():
            print('{0}: {1}'.format(i,j))



if __name__ == '__main__':
    main()
