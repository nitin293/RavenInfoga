import socket


class DNSLookUp:

    def __init__(self, host):
        self.HOST = host
        self.DNS = {}

    def recordA(self):
        try:
            recA = socket.gethostbyname(self.HOST)
            self.DNS["A"] = recA

            return recA

        except:
            recA = None
            self.DNS["A"] = recA

            return recA

    def recordAAAA(self):
        try:
            s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            s.connect_ex((self.HOST, 80))
            recAAAA = s.getsockname()[0]
            s.close()

            self.DNS["AAAA"] = recAAAA

            return recAAAA

        except:
            recAAAA = None
            self.DNS["AAAA"] = recAAAA

            return recAAAA

    def recordPTR(self):
        try:
            recPTR = socket.gethostbyaddr(self.HOST)
            self.DNS["PTR"] = recPTR

            return recPTR

        except:
            recPTR = None
            self.DNS["PTR"] = recPTR

            return recPTR

    def recordNS(self):
        return




    def recALL(self):
        self.recordA()
        self.recordAAAA()
        self.recordPTR()


if __name__ == '__main__':
    dnslookup = DNSLookUp("google.com")
    # dnslookup = DNSLookUp("www.alpharithms.com")
    dnslookup.recALL()
    print(dnslookup.DNS)

