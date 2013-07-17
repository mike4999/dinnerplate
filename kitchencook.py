import os
import sys
import atexit

class Cook():
   def __init__(self):
       self.stdin = '/dev/null'
       self.stdout = '/home/asesma/mike/django/source/monitor/monitor/out'
       self.stderr = '/home/asesma/mike/django/source/monitor/monitor/err'
   def daemonize(self,pidfile):
       """
       do the UNIX double-fork magic, see Stevens' "Advanced
       Programming in the UNIX Environment" for details (ISBN 0201563177)
       http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
       """
       self.pidfile = pidfile
       try:
               pid = os.fork()
               if pid > 0:
                       # exit first parent
                       sys.exit(0)
       except OSError, e:
               sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
               sys.exit(1)
  
       # decouple from parent environment
       os.setsid()
       os.umask(0)
  
       # do second fork
       try:
               pid = os.fork()
               if pid > 0:
                       # exit from second parent
                       sys.exit(0)
       except OSError, e:
               sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
               sys.exit(1)
  
       # redirect standard file descriptors
       sys.stdout.flush()
       sys.stderr.flush()
       si = file(self.stdin, 'r')
       so = file(self.stdout, 'a+')
       se = file(self.stderr, 'a+', 0)
       os.dup2(si.fileno(), sys.stdin.fileno())
       os.dup2(so.fileno(), sys.stdout.fileno())
       os.dup2(se.fileno(), sys.stderr.fileno())
  
       # write pidfile
       atexit.register(self.delpid)
       pid = str(os.getpid())
       file(self.pidfile,'w+').write("%s\n" % pid)

   def delpid(self):
       os.remove(self.pidfile)

if __name__ == "__main__":
    a = Cook()
    a.daemonize('/dev/null')
