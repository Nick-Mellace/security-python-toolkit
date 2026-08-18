import dns.resolver

def dns_lookup(domain, record_type):
    try: 
        records = dns.resolver.resolve(domain, record_type)   # Pull requested records and assign to variable
        for record in records:                                  # Iterate through record values
            if record_type == 'MX':
                if str(record.exchange) == '.' and record.preference == 0:  # Handling for Null MX
                    print(f'{domain} publishes a Null MX record and does not accept mail.')
                else:                          
                    print(record)
            else:
                print(record)                  
    except dns.resolver.NXDOMAIN:   
        print(f'{domain} does not exist.')
    except dns.resolver.NoAnswer:     
        print(f'{domain} is a valid domain, but does not have any published {record_type} records.')