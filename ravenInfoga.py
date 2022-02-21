import argparse
from modules import whois

class Infoga:

    def __init__(self, domain):
        self.domain = domain

    def getWhoIS(self):
        whois_data = whois.getWhoIS(self.domain)

        for key in whois_data.keys():
            print(f"{key}: {whois_data[key]}")




def features():

    menu = '''
    (1) WhoIS Data
    (2) Select All
    (3) Exit
    '''

    return menu

def launcher(domain, option):

    if option==1:
        infoga = Infoga(domain=domain)
        infoga.getWhoIS()

    if option==3:
        exit()

    else:
        print("Invalid Option!")

def terminal(domain):
    while True:
        try:
            print(features())
            option = int(input("[ RavenInfoga ]>> "))
            launcher(domain=domain, option=option)

        except ValueError:
            pass

        except KeyboardInterrupt:
            exit()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", "--domain",
        help="DOMAIN",
        type=str,
        required=True
    )

    args = parser.parse_args()

    domain = args.domain
    terminal(domain)