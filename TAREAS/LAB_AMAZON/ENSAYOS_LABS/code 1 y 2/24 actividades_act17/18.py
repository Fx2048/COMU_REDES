import time
def simulate_dos_attack(request_rate_threshold,duration,service_capacity):
    start_time=time.time()-0.001
    current_time=start_time
    request_count=0
    while current_time -start_time<duration:
        request_count+=1
        if current_time-start_time!=0 and request_count/(current_time-start_time)>request_rate_threshold:
            overload_start_time=current_time
            return overload_start_time
        time.sleep(0.001)
        current_time=time.time()
    return None
request_rate_threshold= 100
duration=10
service_capacity=500
overload_start_time=simulate_dos_attack(request_rate_threshold,duration,service_capacity)
if overload_start_time:
    print(f"El servicio está sobrecargado a partiri de {overload_start_time}")
    
else:
    print("el serivico no esta sobrecargado para el ataque simulataneo")
    
    
