dns_records={'example.com':{'A':'93.184.216.34','AAAA':'2606:2800:220:1:248:1893:25c8:1946',
                            'MX':'mail.example.com', 'CNAME':None,'NS':'ns.example.com'},
             'mail.example.com':{'A':'93.184.216.36'},
             'mail.example.com':{'A':'93.184.216.37'}}
def query_dns(domain,record_type):
    records=dns_records.get(domain,{})
    return records.get(record_type)
def iterative_query(domain,record_type):
    result=query_dns(domain,record_type)
    if result:
        return result
    return "No record found"
def recursive_query(domain,record_type):
    result=query_dns(domain,record_type)
    if record_type=='CNAME' and result:
        return recursive_query(result,record_type)
    return result if result else "No record found"
def resolve_name(domain, record_type, query_type='recursive'):
    if query_type=='recursive':
        return recursive_query(domain,record_type)
    else:
        return iterative_query(domain,record_type)
print(resolve_name('example.com','A'))
print(resolve_name('example.com','MX','iterative'))
