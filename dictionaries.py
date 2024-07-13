#first_dt={"name":"nida","age":21,"degree":"cs","gender":"female"}
# for i in first_dt:
#   print(i,":",first_dt[i])
  
 # second way of creating dictionaries
sec_dt=dict(name="nida",age=21,degree="cs",gender="female")
#to add new element to the dictionary
sec_dt["email"]="nidandsalwakhan@gmail.com"

#to delete an element from the dictionary 
del sec_dt["gender"]    # first method
sec_dt.pop("email")  #second method
print(sec_dt)

try:
    print(sec_dt["name"])
except:
    print("error")    

# for i in sec_dt.keys():
#     print(i)
    
# for y in sec_dt.values():
#     print(y)    
for k in sec_dt.items():
    print(k)



 
