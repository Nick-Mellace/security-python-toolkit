import dns.resolver

def mx_lookup(domain):
    try: 
        records = dns.resolver.resolve(domain, 'MX')    # Pull MX records and assign to variable
        for record in records:
            if str(record.exchange) == '.' and record.preference == 0:  # Handling for Null MX
                print(f'{domain} publishes a Null MX record and does not accept mail.')
            else:                          
                print(record)                  
    except dns.resolver.NXDOMAIN:   
        print(f'{domain} does not exist.')
    except dns.resolver.NoAnswer:     
        print(f'{domain} is a valid domain, but does not have any published MX records.')