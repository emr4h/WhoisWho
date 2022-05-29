import whois
import argparse
import random
from pyfiglet import Figlet

print("\n\n")

fontList = ["big","bulbhead","roman","epic","larry3d","speed","nancyj","stampatello","smslant","slscript","serifcap","rounded","puffy","o8","letters","colossal","basic"]
fontType = random.choice(fontList)
f = Figlet(font=fontType)
print(f.renderText('WhoisWho'))

print("by emr4h\n")

print("-"*50)

parser = argparse.ArgumentParser(prog="WhoisWho\n",description="Who is Lookup Tool", usage="python3 whoiswho.py -d <domain>")

parser.add_argument("-d", type=str, help="Please give a domain")

args = parser.parse_args()

def registered(domain):

    try:
        whoisInfo = whois.whois(domain)
    except Exception:
        return False
    else:
        return bool(whoisInfo.domain)

def details(domain):

    whoisInfo = whois.whois(domain)

    print("DETAILS\n")

    print("* Domain Name: {}\n".format(whoisInfo.domain_name))
    print("* Domain Register: {}\n".format(whoisInfo.registrar))
    print("* Whois server: {}\n".format(whoisInfo.whois_server))
    print("* Creation Date: {}\n".format(whoisInfo.creation_date))
    print("* Expiration Date: {}\n".format(whoisInfo.expiration_date))
    print("* Name Servers: {}\n".format(whoisInfo.name_servers))
    print("* Emails: {}\n".format(whoisInfo.emails))
    print("* Country: {}\n".format(whoisInfo.country))

if __name__ == "__main__":

    if registered(args.d) == True:
        print("+ {} is registered\n\n".format(args.d))
        details(args.d)
    else:
        print("{} is available\n".format(args.d))
