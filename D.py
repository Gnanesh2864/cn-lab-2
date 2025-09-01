import socket
import dns.resolver
import logging

logging.basicConfig(filename="dns_log.txt", level=logging.INFO)

domain = "example.com"

try:
    ip = socket.gethostbyname(domain)
    print(f"A Record (IP Address) for {domain}: {ip}")
    logging.info(f"A Record (IP Address) for {domain}: {ip}")
except Exception as e:
    logging.error(f"Failed to resolve A record: {e}")

try:
    answers = dns.resolver.resolve(domain, "MX")
    for rdata in answers:
        print(f"MX Record: {rdata.exchange} (priority {rdata.preference})")
        logging.info(f"MX Record: {rdata.exchange} (priority {rdata.preference})")
except Exception as e:
    logging.error(f"Failed to resolve MX records: {e}")

try:
    answers = dns.resolver.resolve(domain, "CNAME")
    for rdata in answers:
        print(f"CNAME Record: {rdata.target}")
        logging.info(f"CNAME Record: {rdata.target}")
except Exception as e:
    logging.error(f"Failed to resolve CNAME records: {e}")
