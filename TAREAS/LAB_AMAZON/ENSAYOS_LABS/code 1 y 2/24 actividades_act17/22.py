import time
dns_cache={}
def update_cache(domain,record_type,value,ttl):
    expiration=time.time()+ttl
    if domain not in dns_cache:
        dns_cache[domain]={}
    dns_cache[domain][record_type]=(value,expiration)
    print(f"Cache updated:{domain}[{record_type}]->{value} (TTL: {ttl}s)")
def query_dns(domain,record_type):
    if domain in dns_cache and record_type in dns_cache[domain]:
        value,expiration=dns_cache[domain][record_type]
        if expiration> time.time():
            print(f"Cache hit:{domain}[{record_type}]->{value}")
            return value
        else:
            print(f"Cache expired for {domain}[{record_type}]")
    external_value="192.168.1.1"
    update_cache(domain,record_type,external_value,30)
    return external_value
def clean_expired_entries():
    current_time=time.time()
    for domain in list(dns_cache.keys()):
        for record_type in list(dns_cache[domain].keys()):
            _,expiration=dns_cache[domain][record_type]
            if expiration <=current_time:
                del dns_cache[domain][record_type]
                if not dns_cache[domain]:
                    del dns_cache[domain]
                    print(f"Expired ache entry removed:{domain}[{record_type}]")
update_cache('example.com','A','93.184.216.34',10)
query_dns('example.com' ,'A')
time.sleep(5)
query_dns('example.com','A')
time.sleep(6)
query_dns('example.com','A')
clean_expired_entries()
