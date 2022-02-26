import requests

def getWhoIS(domain):
    try:
        whois = {}

        whois_response = requests.get(f"https://lookup.icann.org/api/whois?q={domain}").json()
        whois_response = whois_response["records"][0]
        whois_response = whois_response["serverResponse"]["rawResponse"]
        whois_response = whois_response.split(">>>")[0].split('\n')[:-2]

        for obj in whois_response:
            key, value = obj.split(':')[0], ':'.join(obj.split(':')[1:])

            if key:
                if key in whois and type(whois[key]) != list:
                    whois[key] = [whois[key]]
                    whois[key].append(value)
                else:
                    whois[key] = value

        return whois

    except IndexError:
        return None


if __name__ == '__main__':
    data = getWhoIS("google.com")

    if data:

        for key in data.keys():
            if type(data[key]) not in [list, set]:
                print(f"{key}: {data[key]}")

            else:
                for obj in data[key]:
                    print(f"{key}: {obj}")