import argparse
from modules import whois
import re


class Infoga:

    def __init__(self, domain):
        self.domain = domain

    def getWhoIS(self):
        whois_data = whois.getWhoIS(self.domain)

        for key in whois_data.keys():
            print(f"{key}: {whois_data[key]}")


class Controller:

    def __init__(self, domain):
        self.domain = domain

    def clean_domain(self):
        self.domain = re.sub("http://", "", self.domain)
        self.domain = re.sub("https://", "", self.domain)

    def features(self):

        menu = '''
        (1) WhoIS Data
        (2) Select All
        (3) Exit
        '''

        return menu


    def launcher(self, option):

        if option==1:
            infoga = Infoga(domain=self.domain)
            infoga.getWhoIS()

        elif option==3:
            exit()

        else:
            print("Invalid Option")


    def terminal(self):
        self.clean_domain()
        while True:
            try:
                print(self.features())
                option = int(input("[ RavenInfoga ]>> "))
                self.launcher(option=option)

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

    controller = Controller(domain=domain)
    controller.terminal()
