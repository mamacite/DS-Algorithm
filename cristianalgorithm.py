import time
import random

def christian_algorithm():
    # Simulated "Server" time
    server_time = time.time() + 500  # Server is ahead
    
    print(f"Client sending request...")
    start_time = time.time()
    
    # Simulate network delay (RTT)
    time.sleep(random.uniform(0.1, 0.5)) 
    
    exit_time = time.time()
    rtt = exit_time - start_time
    
    # Calculate synchronized time
    # Formula: T_client = T_server + (RTT / 2)
    synchronized_time = server_time + (rtt / 2)
    
    print(f"Server Time: {server_time}")
    print(f"Round Trip Time (RTT): {round(rtt, 4)} seconds")
    print(f"Synchronized Client Time: {synchronized_time}")

christian_algorithm()