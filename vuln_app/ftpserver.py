from twisted.internet import protocol, reactor, error
from twisted.python import log
from datetime import datetime
import sys

class CLogger:
  __log_file_path = "/var/log/pyftp/ftp.log"
  # __log_file_path = "./ftp.log"
  __time_last_write = datetime.now()

  def print(self, msg: str):
    curr_time = datetime.now()
    if(abs(self.__time_last_write.minute - curr_time.minute) > 1):
      with open(self.__log_file_path, 'r+') as f:
        f.truncate(0)

    self.__time_last_write = curr_time
    fout = open(self.__log_file_path, 'a')
    fout.write(f"[{curr_time}] " + msg + ";\n")
    fout.close()
    


class FTPProtocol(protocol.Protocol):
  __username = ""
  __password = ""
  __logger = CLogger()
  def connectionMade(self):
    self.transport.write(b"220 Welcome to the FTP server\r\n")

  def dataReceived(self, data):
    if data.startswith(b"USER "):
      self.__username = data[5:].decode().strip()
      self.__logger.print(f"User {self.__username} connected")
      self.transport.write(b"331 Please specify the password.\r\n")
    elif data.startswith(b"PASS "):
      self.__password = data[5:].decode().strip()
      self.__logger.print(f"Password: {self.__password}")
      self.transport.write(b"230 Login not successful.\r\n")
      self.connectionLost(error.ConnectError)
      

  def connectionLost(self, reason):
    self.__logger.print(f"User disconnected")
    self.transport.loseConnection()
    

class FTPFactory(protocol.Factory):
  def buildProtocol(self, addr):
    return FTPProtocol()
  
  # def doStart(self):
  #   return self.startFactory()
  
  # def doStop(self):
  #   return self.stopFactory()



def main():
  if len(sys.argv) < 2:
    print(f"[!] Enter the port : python3 {sys.argv[0]} <port>")
    return
  
  # log.startLogging(sys.stdout)
  reactor.listenTCP(int(sys.argv[1]), FTPFactory())
  reactor.run()


if __name__ == '__main__':
  main()