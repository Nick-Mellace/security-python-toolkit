import dns.resolver

def dns_lookup(domain, record_type):
    try: 
        records = dns.resolver.resolve(domain, record_type)   
        found_spf = False
        for record in records:                               
            if record_type == 'MX':                         
                if str(record.exchange) == '.' and record.preference == 0:  # Handling for Null MX
                    print(f'{domain} publishes a Null MX record and does not accept mail.')
                else:                          
                    print(record)
            elif record_type == 'TXT':                      
                combined_bytes = b''.join(record.strings)   # Reassemble TXT chunks before decoding
                results = combined_bytes.decode()              
                if results.startswith('v=spf1'):                  
                    found_spf = True  
                    print(results)                          
            else:                 
                print(record)
        if record_type == 'TXT' and not found_spf:
            print('No SPF record found.')    
    except dns.resolver.NXDOMAIN:   
        print(f'{domain} does not exist.')
    except dns.resolver.NoAnswer:     
        print(f'{domain} is a valid domain, but does not have any published {record_type} records.')
        