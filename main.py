from socket import *
import optparse
from threading import *
from termcolor import colored


def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(colored(f'[+]{tgtPort}/tcp Open', 'green'))
    except:
        print(colored(f'[+]{tgtPort}/tcp Closed', 'red'))
    finally:
        sock.close()


# portScan helps check the port
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
        print(tgtIP)
    except:
        print(f'Unknown Host {tgtHost}')
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(tgtName)
        print('[+] Scan Results for: ' + tgtName[0])

    except:
        print('[*] Scan Results for :' + tgtIP)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser = optparse.OptionParser('Usage of program:  ' +
                                   '-H <target host> -p <target ports>')
    parser.add_option(
        '-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option(
        '-p',
        dest='tgtPort',
        type='string',
        help='specify target ports separated by comma')
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
