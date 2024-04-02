Name="Neelima"
password="135"
user_name=input("enter the name:")
pass_word=input("enter the password:")
s='''
1.credit
2.debit
3.mini statement
4.exit
'''
Amount=1000
if Name==user_name and password==pass_word:
   while True:
      print(s)
      option=int(input("enter the Option:"))
      if option==1:
         credit_amount=float(input("enter the credit amount:"))  
         print("amount after credit:",Amount+credit_amount)
      elif option==2:
         debited_amount=float(input("enter the debit"))
         print("amount after debited:",Amount-debited_amount)
      elif option==3:
         print("###mini statemt###:",Amount)
      elif option==4:
         break
else:
     print("Incorrect")
           


