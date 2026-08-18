from toolkit.dns_lookup import dns_lookup

domain = input('Domain: ').casefold().strip()
record_type = input('Record Type: ').upper().strip()

supported_records = ['A', 'AAAA', 'MX', 'TXT']

if record_type not in supported_records:
    print('Unsupported record type.')
else:
    dns_lookup(domain, record_type)