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

def set_target(target_addr):
    global target
    target = target_addr

def server_loop():
    global target
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
    client_thread = threading.Thread(target=client_handler,args=(client_socket,))
    client_thread.start()

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
        "-l": set_listen,
        "-t": set_target
    }

    for opt, a in opts:
        print(opt, a)
        fn_item = menu.get(opt, lambda: "Invalid option")
        print(a != "")
        if(a == ""):
            fn_item()
        else:
            fn_item(a)

    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()
        client_sender(buffer)
    if listen:
        server_loop()
main()