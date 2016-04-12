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

ip='10.0.3.'
thr=[]
port=135
for i in range(254):
    ip_d=ip+str(i)
    t=threading.Thread(target=sockets,args=(ip_d,port))
    thr.append(t)
for i in thr:
    i.start()
for i in thr:
    i.join()
