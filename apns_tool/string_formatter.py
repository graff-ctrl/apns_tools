

class CertStringFormatter:

    def format(self, type, cert, partner):
        cert_string = cert.decode("utf-8").replace("\n", "\\n")
        cert_string = cert_string[:-2]
        return f'"{type}-{partner}":"{cert_string}"'
