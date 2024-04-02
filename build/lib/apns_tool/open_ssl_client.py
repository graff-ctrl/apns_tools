import sys
import OpenSSL.crypto as crypto


class OpenSSLClient:

    def open_cert(self, path, password: str):
        with open(path, 'rb') as pkcs12_file:
            pkcs12_data = pkcs12_file.read()
        return crypto.load_pkcs12(pkcs12_data, password)

        # self.parse_cert(p12)
        # self.parse_private_key(p12)

    def parse_cert(self, p12: crypto.PKCS12):
        val = p12.get_certificate()
        return crypto.dump_certificate(crypto.FILETYPE_PEM, val)

    def parse_private_key(self, p12: crypto.PKCS12):

        return crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())