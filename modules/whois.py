import subprocess
import os
import re


def getWhoIS(domain):
    whois = {}

    if os.name=="nt":
        whois_path = os.path.join("tools", "whois.exe")
        data = subprocess.check_output(f"{whois_path} {domain}", shell=True)
        data = re.findall(r"(Domain Name:.*)(?:>>>)", str(data))[0].split("\\r\\n")
    elif os.name=="posix":
        data = subprocess.check_output(f"whois {domain}", shell=True)
        data = re.findall(r"(Domain Name:.*)(?:>>>)", str(data))[0].split("\\n")

    else:
        raise os.error

    for obj in data:
        key, value = obj.split(":")[0], ':'.join(obj.split(":")[1:])[1:]
        if key:
            if key in whois and type(whois[key]) != list:
                whois[key] = [whois[key]]
                whois[key].append(value)
            else:
                whois[key] = value

    return whois



if __name__ == '__main__':
    data = getWhoIS("google.com")
    print(data)
