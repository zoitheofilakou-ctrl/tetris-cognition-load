import socket

#  IP and port for the iMotions UDP connection
IP="127.0.0.1" # always 127.0.0.1 for local connection
UDP_PORT=8089
TCP_PORT=8087

# Function to send the event to iMotions(speed)
def sendudp(string_for_iMotions): 
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    sock.sendto(bytes(string_for_iMotions,"utf-8"),(IP,UDP_PORT))

def send_event(sample: str, value):
    """
    Scientific event for iMotions
    Format: M;1;SampleName;Value
    """
    message = f"M;1;{sample};{value}\r\n"
    sendudp(message)
    print("Sent to iMotions:", message.strip())