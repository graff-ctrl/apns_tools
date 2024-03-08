import sys
from .open_ssl_client import OpenSSLClient
from .string_formatter import CertStringFormatter
import pyperclip as pc
import pkg_resources
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    path = sys.argv[1]

    # Helper for OpenSSL and formatting
    client = OpenSSLClient()
    string_formatter = CertStringFormatter()

    password = input("Enter passphrase: ")

    pem = client.open_cert(str(path), password)
    certificate = client.parse_cert(pem)
    private_key = client.parse_private_key(pem)

    partner = input("Enter the partner name: ")

    string_certificate = string_formatter.format("cert", certificate, partner)
    string_private_key = string_formatter.format("privateKey", private_key, partner)
    output = f"{string_certificate},{string_private_key}"
    pc.copy(output)
    print(output)
    print("copied to clipboard")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Path to .p12 cert
    main()
