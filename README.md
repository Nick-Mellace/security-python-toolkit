# Security Python Toolkit

A Python toolkit for automating common email security investigations.

## Why this project exists

Security engineers often spend valuable time performing repetitive investigative tasks such as DNS lookups, SPF validation, and DMARC analysis.

This toolkit aims to automate those workflows while serving as a hands-on learning project for Python, APIs, cloud security, and software engineering.

## Current Features

- MX Lookup
    - Query domain
    - Return all MX records with preference values
    - Confirm whether domain exists and has MX records
    - Distinguish between Null MX and domains with no published MX records

## Usage

`python main.py`
Domain:  

Basic error handling is built in for non-existent domains, domains without published MX records, and Null MX records.

## Example Outputs

```
Domain: dsa.org
20 dsa-org.mx2-us.mailanyone.net.
30 dsa-org.mx3-us.mailanyone.net.
10 dsa-org.mx1-us.mailanyone.net.

Domain: FraserWeisz4Evr.com
FraserWeisz4Evr.com does not exist.

Domain: example.com
example.com publishes a Null MX record and does not accept mail.
```

## Project Structure

`main.py` - Main program, collect input to pass to toolkit
`toolkit/dns_lookup.py` - Perform MX lookup and interpret DNS response

## Planned Features

- Advanced DNS lookup
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