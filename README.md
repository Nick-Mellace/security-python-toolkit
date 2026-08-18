# Security Python Toolkit

A Python toolkit for automating common email security investigations.

## Why this project exists

Security engineers often spend valuable time performing repetitive investigative tasks such as DNS lookups, SPF validation, and DMARC analysis.

This toolkit aims to automate those workflows while serving as a hands-on learning project for Python, APIs, cloud security, and software engineering.

## Current Features

- General DNS Lookup
    - Query A, AAAA, MX, and TXT records
    - Return MX records with preference values
    - Confirm whether a domain exists and has requested DNS records
    - Distinguish between Null MX and domains with no published MX records
    - Identify and return published SPF records
    - Report when no SPF record is found

## Usage

Run `python main.py`, enter a domain, and select a supported DNS record type: A, AAAA, MX, or TXT.

TXT lookups inspect published records for SPF (`v=spf1`) and return the SPF policy when found. Basic error handling is included for non-existent domains, missing DNS records, Null MX, unsupported record types, and domains without a published SPF record.

## Example Outputs

### MX Lookup

Domain: mimecast.com  
Record Type: MX  
10 service-alpha-inbound-a.mimecast.com.  
10 service-alpha-inbound-b.mimecast.com.

## TXT Lookup

Domain: mimecast.com
Record Type: TXT
v=spf1 redirect=aojpw1q8._spf._d.mim.ec

Domain: justtxt.joshdata.me
Record Type: TXT
No SPF record found.

### A Lookup

Domain: gmail.com  
Record Type: A  
142.251.41.133

### AAAA Lookup

Domain: google.com  
Record Type: AAAA  
2607:f8b0:4009:800::200e

### Null MX

Domain: example.com  
Record Type: MX  
example.com publishes a Null MX record and does not accept mail.

### Unsupported Record Type

Domain: mimecast.com  
Record Type: BANANAS  
Unsupported record type.

## Project Structure

`main.py` - Command-line entry point and user input validation  
`toolkit/dns_lookup.py` - DNS lookup and SPF detection utility

## Planned Features

- Advanced SPF parsing and validation
- WHOIS lookup
- DMARC parser
- REST API
- Microsoft Graph integration

## Learning Goals

- Hands-on, real-world Python application
- Professional development in cybersecurity
- Learn to use AI effectively as a learning tool
- Creative expression through coding - it's fun!