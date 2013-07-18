# -*- coding: utf-8 -*-
# 
#       Copyright M.O. Atambo, University of Eldoret.

import sys
import requests
import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='local html file with control content',default= 'http://www.uoeld.ac.ke/')

except Exception as e:
    print "Failed: %s"%e

class Fetch():
      def __init__(self,args):
          self.url = args
          self.testing = 1
      
      def run_get(self): 
          self.reply = requests.get(self.url)
          if self.reply.status_code != requests.codes.ok:
              print "server down or not answering requests"
              sys.exit()
  
if __name__ == "__main__":
    args = parser.parse_args()
    a = Fetch(args.url)
    a.run_get()
    print (a.reply.text)
