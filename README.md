# Security Python Toolkit

A Python toolkit for automating common email security investigations.

## Why this project exists

Security engineers often spend valuable time performing repetitive investigative tasks such as DNS lookups, SPF validation, and DMARC analysis.

This toolkit aims to automate those workflows while serving as a hands-on learning project for Python, APIs, cloud security, and software engineering.

## Current Features

- General DNS Lookup
    - Query A, AAAA, MX, and TXT records
    - Return all published records for the requested record type
    - Validate supported DNS record types
    - Confirm whether a domain exists
    - Distinguish between Null MX and domains with no published MX records

## Usage

Run `python main.py`, enter a domain, and select a supported DNS record type.

Currently supported record types:

- A
- AAAA
- MX
- TXT

Basic error handling is included for non-existent domains, unsupported record types, DNS queries with no published records, and Null MX records.

## Example Outputs

### MX Lookup

Domain: mimecast.com  
Record Type: MX  
10 service-alpha-inbound-a.mimecast.com.  
10 service-alpha-inbound-b.mimecast.com.

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
`toolkit/dns_lookup.py` - DNS lookup and response handling

## Planned Features

- SPF validation
- WHOIS lookup
- DMARC parser
- REST API
- Microsoft Graph integration

## Learning Goals

- Hands-on, real-world Python application
- Professional development in cybersecurity
- Learn to use AI effectively as a learning tool
- Creative expression through coding - it's fun!