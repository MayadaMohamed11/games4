def showbored():
    print (arr7[0],'','|','',arr7[1],'|','',arr7[2],'|',arr7[3])
    print (arr7[4],'','|','',arr7[5],'|','',arr7[6],'|',arr7[7])
    print (arr7[8],'','|',arr7[9],'|',arr7[10],'|',arr7[11])
    print (arr7[12],'|',arr7[13],'|',arr7[14],'|',arr7[15])
arr7=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
counter=0
def fun1 ():
     for j in range (2):
       num=int(input('player 1 = '))
       while (num>16 or num<1):
                  print("Not Valid")
                  num=int(input("Player 1: "))
       arr5.append(num)
       if (num==1 or num==2 or num==3 or num==4 or num==5 or num==6 or num==7 or num==8 or num==9 or num==10 or num==11 or num==12 or num==13 or num==14 or num==15 or num==16):
          if(arr7[num-1]!='x'):
              for i in range (16):
                if(num==arr7[i]):
                       arr7[i]='x'

          else:
              del arr5[j]
              while(arr7[num-1]=='x'):
                     print('sory enter anthor number')
                     num=int(input("Player 1: "))
              arr5.append(num)
              arr7[num-1]='x'
def fun4():
       for j in range (2):
         num=int(input('player 2 = '))
         while (num>16 or num<1):
                  print("Not Valid")
          
                  num=int(input("Player 2: "))          
         arr5.append(num)
         if (num==1 or num==2 or num==3 or num==4 or num==5 or num==6 or num==7 or num==8 or num==9 or num==10 or num==11 or num==12 or num==13 or num==14 or num==15 or num==16):
                if(arr7[num-1]!='x'):
                   for i in range (16):
                     if(num==arr7[i]):
                            arr7[i]='x'

                else:
                    del arr5[j]
                    while(arr7[num-1]=='x'):
                       print('sory enter anthor number')
                       num=int(input("Player 2: "))
                    arr5.append(num)
                    arr7[num-1]='x'                   
def fun2 ():
    counter=0
    if ((arr5[1]-arr5[0]==1 and arr5[0]%4!=0) or arr5[1]-arr5[0]==4 or (arr5[0]-arr5[1]==1 and arr5[1]%4!=0) or arr5[0]-arr5[1]==4):
                     del arr5[0]
                     del arr5[0]
                     for i in range (0,3):
                         if(arr7[i]!='x' and arr7[i+1]!='x'):
                             counter+=1
                         if(arr7[i+4]!='x' and arr7[i+5]!='x'):
                             counter+=1
                         if(arr7[i+8]!='x' and arr7[i+9]!='x'):
                             counter+=1
                         if(arr7[i+12]!='x' and arr7[i+13]!='x'):
                                counter+=1
                     for i in range (0,3):
                         if (arr7[i]!='x' and arr7[i+4]!='x'):
                            counter+=1
                         if (arr7[i+4]!='x' and arr7[i+8]!='x'):
                             counter+=1
                         if (arr7[i+8]!='x' and arr7[i+12]!='x'):
                            counter+=1
                     if (counter!=0):
                         counter=0
                     elif (counter==0):
                         print("player1 is winner")
                         print(' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','end game')
                         break

    else:  
        print("enter anthor numbers")
        arr7[arr5[0]-1]=arr5[0]
        arr7[arr5[1]-1]=arr5[1]
        del arr5[0]
        del arr5[0]
        fun1()
        fun2()
def fun3 ():
    counter=0
    if (arr5[1]-arr5[0]==1 and arr5[0]%4!=0 or arr5[1]-arr5[0]==4 or arr5[0]-arr5[1]==1 and arr5[1]%4!=0 or arr5[0]-arr5[1]==4):
                     del arr5[0]
                     del arr5[0]
                     for i in range (0,3):
                         if(arr7[i]!='x' and arr7[i+1]!='x'):
                             counter+=1
                         if(arr7[i+4]!='x' and arr7[i+5]!='x'):
                             counter+=1
                         if(arr7[i+8]!='x' and arr7[i+9]!='x'):
                             counter+=1
                         if(arr7[i+12]!='x' and arr7[i+13]!='x'):
                              counter+=1
                     for i in range (0,3):
                         if (arr7[i]!='x' and arr7[i+4]!='x'):
                            counter+=1
                         if (arr7[i+4]!='x' and arr7[i+8]!='x'):
                             counter+=1
                         if (arr7[i+8]!='x' and arr7[i+12]!='x'):
                            counter+=1
                     if(arr7[0]=='x' and arr7[1]=='x' and arr7[2]=='x' and arr7[3]=='x' and arr7[4]=='x' and arr7[5]=='x' and arr7[6]=='x' and arr7[7]=='x' and
                                   arr7[8]=='x' and arr7[9]=='x' and arr7[10]=='x' and arr7[11]=='x' and arr7[12]=='x' and arr7[13]=='x' and arr7[14]=='x' and arr7[15]=='x'):
                                   print("both of them winner")
                                   print(' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','end game')
                                           
                     elif (counter==0):
                              print("player2 is winner")
                              print(' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','end game')
                     if (counter!=0):
                        counter=0
    else:
        print("enter anthor numbers")
        arr7[arr5[0]-1]=arr5[0]
        arr7[arr5[1]-1]=arr5[1]
        del arr5[0]
        del arr5[0]
        fun4()
        fun3()
arr5=[]
showbored()
for i in range (4):
    fun1()
    fun2()
    showbored()
    fun4()
    fun3()
    showbored()
                    

    
    
                
        

    


    
    
                
  
                 
