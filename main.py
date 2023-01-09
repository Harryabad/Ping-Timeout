import datetime
import socket
from pythonping import ping
import time
import speedtest
import atexit

try:
    # Get an IP address using socket 
    url = (socket.gethostbyname('google.com'))

    # 'Request timed out' is our catch for a failed ping
    substring = "Request timed out"

    # Create a new txt to store our failed ping data
    f = open("Ping Timeouts.txt", "w")

    # Not needed but if there are 30 instances of RTOs, program will close
    count = 0

    wifi = speedtest.Speedtest()

    def speedtest():
        
        f.write(f"Speedtest at {datetime.datetime.now()}\n")
        f.write(f"Wifi Download speed: {(int(wifi.download())//1000000)} Mbps\n")
        f.write(f"Wifi Upload speed: {(int(wifi.upload())//1000000)} Mbps\n\n")
        print("Speedtest Complete \n")

    speedtest()

    while True:

        # Send a ping, split data, store as string
        ping_data = str(ping(url, out=True)).split("\n")

        if substring in ping_data[0] or substring in ping_data[1] or substring in ping_data[2] or substring in ping_data[3]:
            f.write(f"Update at {datetime.datetime.now()} \n")
            f.write(f"{ping_data[0]}")
            f.write(f"{ping_data[1]}")
            f.write(f"{ping_data[2]}")
            f.write(f"{ping_data[3]}")
            f.write("\n")
            
            count += 1
            if count >30:
                break

        time.sleep(.7500)
        
    f.close()


except KeyboardInterrupt:
    speedtest()
    print(f"Program Executed at {datetime.datetime.now()}")
    f.close()