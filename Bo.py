
welocom= "\033[1;34m***welocom***"
print (welocom)
print ("\033[0;31m...tools...")
print ("\033[0;32m[1]bomb\n [2]ing bot")
tool=int(input ("\033[1;33menter tool number:") )
if (tool==int(2)):
  print (''' 
 \033[1;32m _____               ____        _   
 |_   _|             |  _ \      | |  
   | |  _ __   __ _  | |_) | ___ | |_ 
   | | | '_ \ / _` | |  _ < / _ \| __|
  _| |_| | | | (_| | | |_) | (_) | |_ 
 |_____|_| |_|\__, | |____/ \___/ \__|
               __/ |                  
              |___/                   
  ''')
  print("runig:-run")
  word=input("Enerer you word: " )
  endtxt= (word[-3:])
  if("ing" == endtxt):
    print("\033[1;33m" +word[:-3])
  else:
    print("\033[1;33m" +word)
    print("\003[1;32m×××tanks×××")
if (tool==int(1)):
  print ('''\033[0;32m______                 _     
  | ___ \               | |    
  | |_/ / ___  _ __ ___ | |__  
  | ___ \/ _ \| '_ ` _ \| '_ \ 
  | |_/ / (_) | | | | | | |_) |
  \____/ \___/|_| |_| |_|_.__/ 
  ''')
  print("eg:-  input 5\nbum..\nbum...\nbum....\nbom.....")
  x=int(input("Enter your types:") )
  for z in range(k):
    print(f"\003[0;33m bum",k,(k) * ".")

else:
    print("\033[1;31m try again")
