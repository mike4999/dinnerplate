#!/opt/monitor/monitor/bin/python
# -*- coding: utf-8 -*-
# 
#       Copyright M.O. Atambo, University of Eldoret.
from bs4 import BeautifulSoup
import sys
import argparse
import time
import os
import sys
root , pyfilename = os.path.split(os.path.abspath(__file__))
os.chdir(root)

try:
    from hotpot  import Fetch
    from kitchencook import Cook
except Exception as e:
    print "cant import module: %s exiting"%e
    sys.exit()


try:
    import defaults
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', help='url to page thats monitored', default =defaults.myurl)
    parser.add_argument('--control', help='local html file with control content',default= defaults.myokfile)
    parser.add_argument('--notify', help='email to receive notification',default=defaults.myemail)
    parser.add_argument('--daemonize', help='to daemonize or not to daemonize',default=False)
    args = parser.parse_args()

except Exception as e:
    print "cant import module: %s"%e
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', help='url to page thats monitored')
    parser.add_argument('--control', help='local html file with control content')
    parser.add_argument('--notify', help='email to receive notification')
    args = parser.parse_args()

class Soup_chef(Cook):
      def __init__(self,htmldoc,control):
          self.url = htmldoc
          self.control = control
          self.testing= 1
          self.test_params = {}
          self.control_params = {}
    
      def pour_soup (self):
          if args.daemonize:
                  self.daemonize('/var/spool/dinnerplate/pid/dinerplated.pid')
          self.suspect = BeautifulSoup( self.url )
          try:
              okfile = open( self.control,"r")
              self.control = BeautifulSoup(okfile) 
          except Exception as e:
              print e, "there's what happend"
              sys.exit()
   
      def taste_soup(self):
	  self.test_params['links'] = self.suspect.find_all('link')
	  self.test_params['title'] = self.suspect.find_all('title')
	  self.test_params['script'] = self.suspect.find_all('script')
	  self.test_params['li'] = self.suspect.find_all('li')
	  self.test_params['div'] = self.suspect.find_all('div')
	  self.test_params['span'] = self.suspect.find_all('span')
          self.control_params['links'] = self.control.find_all('link')
          self.control_params['title'] = self.control.find_all('title')
          self.control_params['script'] = self.control.find_all('script')
          self.control_params['li'] = self.control.find_all('li')
          self.control_params['div'] = self.control.find_all('div')
          self.control_params['span'] = self.control.find_all('span')
      
      def drink_soup(self):
          self.taste = {}
          for i in self.test_params.keys():
              len_test = len(self.test_params[i] )
              len_control = len(self.control_params[i])
          
              if len_test != len_control:
                  test_problems = self.test_params[i]
                  control_problems = self.control_params[i]

                  for j in range(len(test_problems)):
                      if test_problems[j] not in  control_problems:
                         self.taste['removed %s :'%j] = " here lies the culprit %s thats been added"%test_problems[j]

                  for j in range(len(control_problems)):
                      if control_problems[j] not in  test_problems:
                         self.taste['added %s :'%j] = " here lies the culprit %s thats been removed"%control_problems[j]
                  """
                  we need to send an email here
                  """
              else:
                  self.taste ['ok %s :'%i] = "number of %s is %s and %s in test and contol respectively"%(i,len_test,len_control) 
            
      def complement_chef(self):
           self.dirty_plate = {}
           if self.taste.values():
              for i in  self.taste.keys():
                  if ("removed" in i) or ("added" in i ):
                      self.dirty_plate[i] = self.taste[i]
           if self.dirty_plate:
               self.waiter={}
               print self.dirty_plate
               import socket
               host  = socket.gethostname()
               self.waiter['Subject'] = 'Automated mail warning, Your waiter, with complements'
               self.waiter['From'] = host
               self.waiter['To'] = args.notify
            
               try: 
                   import smtplib
                   from email.mime.text import MIMEText
                   s = smtplib.SMTP('localhost')
                   s.sendmail(self.waiter['From'], args.notify,str( self.dirty_plate))
           
               except Exception as e:
                   print "we're unable to send emails coz of: %s"%e
                   


if __name__ == "__main__" :
    while True:
        req = Fetch (args.test) 
        req.run_get()
        a = Soup_chef(req.reply.text,args.control)
        a.pour_soup()
        a.taste_soup()
        a.drink_soup()
        a.complement_chef()
        time.sleep(120)
