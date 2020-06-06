import sys
import socket
import getopt
import threading
import subprocess

listen = False
upload  = False
command = False

port = 0
target = ""
execute = ""
upload_destination = ""

def usage():
    print("net.py\n")
    print("Usage: net.py -t target_host -p port\n")
    print("-l --listen               - listen on [host]:[port] for\n")
    print("-e --execute=file_to_run  - execute the given file upon")
    print("                            receiving a connection\n")

def set_listen():
    global listen
    listen = True

def set_port(port_arg):
    global port
    port = int(port_arg)

def set_target(target_addr):
    global target
    target = target_addr

def main():
    global port
    global target
    global listen
    global execute
    global command
    global upload_destination

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",
            ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    menu = {
        "-p": set_port,
        "-l": set_listen,
        "-t": set_target
    }

    for opt, a in opts:
        fn_item = menu.get(opt, lambda: "Invalid option")
        if(a == ""):
            fn_item()
        else:
            fn_item(a)

    if(listen == True):
        print(netcat("ping"))

def netcat(text_to_send):
    global port
    global target

    print("netcat target", target, sep=" ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendall(text_to_send.encode())
    s.shutdown(socket.SHUT_WR)

    rec_data = []
    while 1:
      data = s.recv(1024)
      if not data:
         break
      rec_data.append(data)

    return str(rec_data)
main()