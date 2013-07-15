# -*- coding: utf-8 -*-
# 
#       Copyright M.O. Atambo, University of Eldoret.

import sys
import requests

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
     a = Fetch('http://www.uoeld.ac.ke/')
     a.run_get()
