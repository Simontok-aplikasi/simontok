import random
import os, sys
nama = raw_input ("masukan nama : ")
password = raw_input  ("masukan password : ")
if nama == "deniganz" and password == "ganz":
  print "welcome"
elif nama == "user1" and password == "user1":
  print "welcome"
elif nama == "user2" and password == "user2":
  print "hay welcome"
else:
  print "sapa lu kamvhang org asing lu njerr!!!"
  sys.exit()

# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";
print ""
print ""
 
print O+"create by : mrds"
print P+"contant me : 081274083829"
print R+"permainan tebak simontok"
print R+"bissmilah dulu cuy:v"
print O+"============================="
print O+"  ///////        ///////"
print B+"    //  //   // //   // ///////"
print B+"   //  //   // /////// //   //"
print R+"  //  /////// //   // //   //"
print R+"============================="
print R+"    ////,   /////"
print P+"   //  //  //"
print P+"  //  //  /////"
print G+" /// //     //"
print G+"/////`  /////"
print G+"============================="
print ""
print P+"pilihan :"
print ""
print G+"1, zaskia gotik"
print B+"2, ariel tatum"
print W+"3, luna maya"

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv) 
def permainan():
    kamu = int(input("masukan pilihanmu: "))
    kom = random.choice(["zaskia", "ariel", "luna maya"])
    if kamu == 1:
        print G+"kamu    : zaskia gotik"
        print("komputer :", kom)
        if kom == "zaskia gotik":
           print G+"\tdraw"
        if kom == "ariel tatum":
           print B+"\tlu menang"
        if kom == "luna maya":
           print W+"\tlu kalah"
    if kamu == 2:
        print B+"kamu     : ariel tatum"
        print("komputer :", kom)
        if kom == "zaskia gotik":
           print G+"\tkamu kalah"
        if kom == "zaskia gotik":
           print R+"\tkamu kalah"
        if kom == "ariel tatum":
           print W+"\tdraw"
        if kom == "luna maya":
           print B+"\tlu menang"
    if kamu == 3:
        print B+"kamu     : luna maya"
        print("komputer :", kom)
        if kom == "zaskia gotik":
           print G+"\tlu menang"
        if kom == "ariel tatum":
           print W+"\tlu kalah"
        if kom == "luna maya":
           print B+"\tdraw"
    if kamu >=4:
      print R+"pilihanmu salah!!!"
      restart()
permainan()
restart()
try:
	permainan()
except keyboardinterrupt:
	os.system('clear')
	restart()
