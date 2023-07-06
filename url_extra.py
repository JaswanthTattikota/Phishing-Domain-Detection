import urllib
from urllib.parse import urlparse, parse_qs
import pandas as pd
import requests
import whois
import dns.resolver
from datetime import datetime, timezone
import whois
import ipaddress
import ipwhois

import logging

# Create a logger
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler and set the formatter
file_handler = logging.FileHandler('url_extra.log')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

def get_domain_info(url):
    try:
        domain = whois.whois(url)
        today = datetime.now()

        activation_days = days_since_registration(domain.creation_date, today)
        expiration_days = days_until_expiration(domain.expiration_date, today)

        return activation_days, expiration_days
    except whois.parser.PywhoisError:
        return None, None

def days_since_registration(creation_date, today):
    if isinstance(creation_date, list):
        creation_date = creation_date[0]  # Use the first element in the list

    if creation_date:
        diff = today - creation_date.replace(tzinfo=None)
        return diff.days
    else:
        return None

def days_until_expiration(expiration_date, today):
    if isinstance(expiration_date, list):
        expiration_date = expiration_date[0]  # Use the first element in the list

    if expiration_date:
        diff = expiration_date.replace(tzinfo=None) - today
        return diff.days
    else:
        return None

def extract_asn(url):
    try:
        ip = ipaddress.ip_address(url)
        domain = ipwhois.IPWhois(ip)
        result = domain.lookup_rdap()

        if 'asn' in result:
            return result['asn']
        else:
            return None
    except (ValueError, ipaddress.AddressValueError):
        return None

import dns.resolver

def extract_ttl(url):
    try:
        hostname = url.split("//")[-1].split("/")[0]
        answers = dns.resolver.resolve(hostname, 'A')
        ttl = answers.rrset.ttl
        return ttl
    except dns.resolver.NXDOMAIN:
        return None
    except dns.resolver.Timeout:
        return None
    except dns.exception.DNSException as e:
        return None

def url_to_columns(url):
    parsed_url = urlparse(url)
    ttl = extract_ttl(url)
    activation_days, expiration_days = get_domain_info(url)
    ip_address = url.split("//")[-1].split("/")[0]
    asn = extract_asn(ip_address)

    qty_slash_url = url.count('/')
    length_url = len(url)
    domain_length = len(parsed_url.netloc)
    qty_dot_directory = parsed_url.path.count('.')
    qty_hyphen_directory = parsed_url.path.count('-')
    qty_underline_directory = parsed_url.path.count('_')
    qty_slash_directory = parsed_url.path.count('/')
    qty_questionmark_directory = parsed_url.path.count('?')
    qty_equal_directory = parsed_url.path.count('=')
    qty_and_directory = parsed_url.path.count('&')
    qty_exclamation_directory = parsed_url.path.count('!')
    qty_plus_directory = parsed_url.path.count('+')
    qty_hashtag_directory = parsed_url.path.count('#')
    qty_percent_directory = parsed_url.path.count('%')
    directory_length = len(parsed_url.path)
    qty_dot_file = parsed_url.path.split('/')[-1].count('.')
    qty_underline_file = parsed_url.path.split('/')[-1].count('_')
    qty_space_file = parsed_url.path.split('/')[-1].count(' ')
    qty_tilde_file = parsed_url.path.split('/')[-1].count('~')
    qty_percent_file = parsed_url.path.split('/')[-1].count('%')

    response = requests.get(url)
    time_response = response.elapsed.total_seconds()
    asn_ip = asn
    time_domain_activation = activation_days
    time_domain_expiration = expiration_days
    ttl_hostname = ttl

    logger.info(f"Extracting features for URL: {url}")

    # Replace None values with -1
    qty_slash_url = qty_slash_url if qty_slash_url is not None else 0
    length_url = length_url if length_url is not None else 0
    domain_length = domain_length if domain_length is not None else 0
    qty_dot_directory = qty_dot_directory if qty_dot_directory is not None else -1
    qty_hyphen_directory = qty_hyphen_directory if qty_hyphen_directory is not None else -1
    qty_underline_directory = qty_underline_directory if qty_underline_directory is not None else -1
    qty_slash_directory = qty_slash_directory if qty_slash_directory is not None else -1
    qty_questionmark_directory = qty_questionmark_directory if qty_questionmark_directory is not None else -1
    qty_equal_directory = qty_equal_directory if qty_equal_directory is not None else -1
    qty_and_directory = qty_and_directory if qty_and_directory is not None else -1
    qty_exclamation_directory = qty_exclamation_directory if qty_exclamation_directory is not None else -1
    qty_plus_directory = qty_plus_directory if qty_plus_directory is not None else -1
    qty_hashtag_directory = qty_hashtag_directory if qty_hashtag_directory is not None else -1
    qty_percent_directory = qty_percent_directory if qty_percent_directory is not None else -1
    directory_length = directory_length if directory_length is not None else -1
    qty_dot_file = qty_dot_file if qty_dot_file is not None else -1
    qty_underline_file = qty_underline_file if qty_underline_file is not None else -1
    qty_space_file = qty_space_file if qty_space_file is not None else -1
    qty_tilde_file = qty_tilde_file if qty_tilde_file is not None else -1
    qty_percent_file = qty_percent_file if qty_percent_file is not None else -1
    time_response = time_response if time_response is not None else -1
    asn_ip = asn_ip if asn_ip is not None else -1
    time_domain_activation = time_domain_activation if time_domain_activation is not None else -1
    time_domain_expiration = time_domain_expiration if time_domain_expiration is not None else -1
    ttl_hostname = ttl_hostname if ttl_hostname is not None else -1

    data = {
        'qty_slash_url': qty_slash_url,
        'length_url': length_url,
        'domain_length': domain_length,
        'qty_dot_directory': qty_dot_directory,
        'qty_hyphen_directory': qty_hyphen_directory,
        'qty_underline_directory': qty_underline_directory,
        'qty_slash_directory': qty_slash_directory,
        'qty_questionmark_directory': qty_questionmark_directory,
        'qty_equal_directory': qty_equal_directory,
        'qty_and_directory': qty_and_directory,
        'qty_exclamation_directory': qty_exclamation_directory,
        'qty_plus_directory': qty_plus_directory,
        'qty_hashtag_directory': qty_hashtag_directory,
        'qty_percent_directory': qty_percent_directory,
        'directory_length': directory_length,
        'qty_dot_file': qty_dot_file,
        'qty_underline_file': qty_underline_file,
        'qty_space_file': qty_space_file,
        'qty_tilde_file': qty_tilde_file,
        'qty_percent_file': qty_percent_file,
        'time_response': time_response,
        'asn_ip': asn_ip,
        'time_domain_activation': time_domain_activation,
        'time_domain_expiration': time_domain_expiration,
        'ttl_hostname': ttl_hostname
    }

    df = pd.DataFrame(data, index=[0])
    logger.info("Feature extraction completed")
    return df

