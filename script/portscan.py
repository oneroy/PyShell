import socket
import threading

def sockets(ip,port):
  try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c=s.connect_ex((ip,port))
    if c==0:
        print '%s:%s open'% (ip,port)
    else:
        pass
    s.close()
  except Exception,e:
        print e
        print 'error'

ip='10.0.3.54'
thr=[]
port=[21,22,23,25,80,135,449,8080,8090,3389,1433,3306,1521]
for i in port:
    t=threading.Thread(target=sockets,args=(ip,i))
    thr.append(t)
for i in thr:
    i.start()
for i in thr:
    i.join()
