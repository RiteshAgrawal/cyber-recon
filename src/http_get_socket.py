from whois_example import SocketWrapper

s = SocketWrapper('localhost', 9001)
response = s.get_details("GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
print(response)
