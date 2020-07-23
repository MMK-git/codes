import xlrd
#from lxml import etree as ET
import shlex
import subprocess
import xml.etree.ElementTree as ET
import sys
class exceldata():

    '''
     global x
     x = input("ENTER THE NUMBER OF DEPLOYMENTS YOU WANT\n")
     def get(self,i):
         #global y
        n=[]
         #loc =input("enter excel file location")
        loc = ('/root/Documents/teste.xlsx')
        ls = xlrd.open_workbook(loc)
        sheet = ls.sheet_by_index(0)
        #for i in range(0,x):
        for j in range(0,4):
             m = sheet.cell_value(i,j)
             setattr(self,"a",m)
             n.append(m)
        return n
     '''
    global x
    global shee
    global loca
    global lsr
    x=input("ENTER THE NUMBER OF DEPLOYMENTS YOU WANT\n")
    loca = ('/root/Documents/teste.xlsx')
    lsr = xlrd.open_workbook(loca)
         #global sheet
    shee = lsr.sheet_by_index(0)
    def readex(self):
         a=[]
         global b
         b=[]
         c=[]
    #x=int(input("enter number"))
         loc = ('/root/Documents/teste.xlsx')
         ls = xlrd.open_workbook(loc)
         #global sheet
         sheet = ls.sheet_by_index(0)
    #cn=sheet.ncols
         cn =[]
         cn = sheet.col_values(0)
    #print(cn)
         #x=input("enter number\n")
         print("SELECT THE SERVERS YOU WANT TO USE FOR DEPLOYMENT")
         ha=0
         ro=[]
         for i in cn:
             print(ha,'.',i)
             ro.append(ha)
             ha=ha+1
        # print(ro)
         try:
             my_list = []

             for i in range(0, int(x)):
                 a=int(input())
                 if a in ro:
                     my_list.append(a)
                 else:
                #print("select from the above listed values")
                     sys.exit()
            #my_list.append(int(input()))
        #print(my_list)
# if the input is not-integer, just print the list
         except:
             print("please select integers listed above")
             sys.exit()
         #else:
             #print(my_list)
         for i in my_list:
             a=sheet.row_values(i)
             b.append(a)
         print(b)
         return b
                   
    def man(self,g,s,e,w):
         #print(k) 
         #v = input("enter file name for xml"+ str(k))
         a=input("ENTER OS BUILD PLAN\n")
         b=input("ENTER OS PATH PATH \n")
         root = ET.Element ('CONFIGS') 
         start = ET.SubElement (root, 'CONFIG') 
         iso = ET.SubElement (start, 'OS') 
         iso.text = a 
         iso_path = ET.SubElement (start, 'OS_PATH') 
         iso_path.text = b
         start2 = ET.SubElement (start, 'NODES') 
         start3 = ET.SubElement (start2, 'NODE')
         start4 = ET.SubElement(start3, 'ILO')
         ip = ET.SubElement(start4, 'ILO_IP')
         ip.text = g
         user = ET.SubElement(start4, 'ILO_USERNAME')
         user.text = s
         pwd = ET.SubElement(start4, 'ILO_PASSWORD')
         pwd.text = e
         host_name = ET.SubElement(start3, 'HOST_NAME')
         host_name.text = "rhel82"
         mac_address = ET.SubElement(start3, 'MACADDRESS')
         mac_address.text = w
         sys_pwd = ET.SubElement(start3, 'SYSTEM_PASSWORD')
         sys_pwd.text = "Compaq@123"
         sys_pwd = ET.SubElement(start3, 'TEAM')
         sys_pwd.text = "CSI-Other"
         sys_pwd = ET.SubElement(start3, 'BOOTMODE')
         sys_pwd.text = "UEFI"
         start5 = ET.SubElement(start3, 'SPP')
         install = ET.SubElement(start5, 'INSTALL')
         install.text = "no"
         sys_pwd = ET.SubElement(start5, 'ISO_PATH')
         sys_pwd.text ="http://172.20.57.150/deployment/SPP/SPP2020030.2020_0319.22.iso"
         iso_path = ET.SubElement(start5, 'FLASH_FIRMWARE')
         iso_path.text = "Yes"
         o = ET.tostring(root, encoding='utf8').decode('utf8')
         #print(o)
         filename = "%s.xml" % g
         f1 = open(filename, 'w')
         f1.write(o)
         print("xml is stored in" ,filename,"file")
         #setattr(self,"b",f1)
         f_list.append(filename)
         return f_list

list1=[]
list2=[]
global f_list
f_list=[]
ob=exceldata()
import re
#print(type(x))
#xe=re.compile('^(?=.*[0-9]$)(?=.*[a-zA-Z])')
#if xe.match(username):
 #   print("getitvmisr")
xe=re.compile('(([a-z]+)([0-9]+))')
pe=re.compile('(([0-9]+)([a-z]+))')
#print(type(x))
de=re.compile('[^a-zA-Z0-9]')
#if(pe.match(username)or xe.match(username))and (xe.match(username)or pe.match(username)):
 #                                                                      print("getitvmis")
if x.isalpha():
    #print("YOU HAVE ONLY "+ str(shee.nrows)+ "SERVERS")
    #ob=exceldata()
    #sys.exit()
    #ob.readex()
    print("ACCEPTS ONLY INTEGERS")
    sys.exit()

elif x.isdigit() and int(x) > shee.nrows:
    print("YOU HAVE ONLY "+ str(shee.nrows) + " SERVERS")
    sys.exit()
elif (pe.match(x)or xe.match(x))and (xe.match(x)or pe.match(x)):

    print("ACCEPTS ONLY INTEGERS")
    sys.exit()
    #ob=exceldata()
    #ob.readex()
elif de.match(x):
    print("special characters not allowed")
    sys.exit()
elif int(x) <= shee.nrows and x.isdigit() and int(x)>0:

     #print("ACCEPTS ONLY INTEGERS")
     #sys.exit()
    ob=exceldata()
    ob.readex()
elif int(x)== 0:
    print("DEPLOYMENTS SHOULD BE ATLEAST ONE")
    sys.exit()
else:
    print("negative integers not accepted")
    sys.exit()
'''if x.isdigit():

    #ob=exceldata()
    ob.readex()
else:
    print("ACCEPTS ONLY INTEGERS")
    sys.exit()'''
#print(x)
'''
if x.isdigit():
    for i in range(0,int(x)):
         obj=exceldata()
         list1.append(obj.get(i))
else:
    print("enter numerical values")
    sys.exit()
    obj1=exceldata()
    x=input()
    if x.isdigit():
        for i in range(0,int(x)):
             obj=exceldata()

         #list1.append(obj.get(i))

             list1.append(obj.get(i))
             
print(list1)'''
#print(list1[0][0])
#for m in range(0,int(y))
for k in range(0,int(x)):
     #ob=exceldata()
     ob.man(b[k][0], b[k][1],b[k][2],b[k][3])

#print(f_list)
from subprocess import Popen, PIPE
p = ['-f /root/' + dire for dire in f_list]
def mmk(n):
     return n  +  " " '-cy'
res=map(mmk,p)
files_list=list(res)
print(files_list)
q=open("console_output.txt","w")
e=open("errorout.txt","w")
from subprocess import Popen, PIPE
import subprocess
import os
cmds_list = [['cpt', file_name] for file_name in files_list]
procs = [Popen(cmd,bufsize=0,stdout=q, stderr=e) for cmd in cmds_list]
for proc in procs:
    #proc.communicate()
    stdout, stderr = proc.communicate()
    #stdout = procs.stdout.read()
    #print(stdout)
    proc.wait()
os.system("rm /root/errorout.txt")
print("DEPLOYMENT DONE")
