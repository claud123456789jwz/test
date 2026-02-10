import nmap

class NmapRST:
    def __init__(self, target):
        self.target = target
        self.nm = nmap.PortScanner()  

    def scan(self):
        self.nm.scan(self.target)
        return self.nm[self.target]

    def get_results(self):
        return self.nm[self.target]['tcp'] if self.nm.all_hosts() else {}

if __name__ == '__main__':
    target_ip = '192.168.1.1'  # Replace with your target IP
    scanner = NmapRST(target_ip)
    scanner.scan()
    results = scanner.get_results()
    print(results)