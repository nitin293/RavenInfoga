from modules import whois

class Infoga:

    def __init__(self, domain):
        self.domain = domain

    def getWhoIS(self):
        whois_data = whois.getWhoIS(self.domain)



def features():

    menu = '''
    (1) WhoIS Data
    (2) Select All
    (3) Exit
    '''

    return menu

def launcher(option):
    print(option)
    if option==3:
        exit()


if __name__ == '__main__':
    while True:
        try:
            print(features())
            option = int(input("[ RavenInfoga ]>> "))
            launcher(option=option)

        except ValueError:
            pass

        except KeyboardInterrupt:
            exit()