dict = {"Mohan": 82, "Rohan": 78 ,"Soham":90 ,"Nandan":86}
print(dict)
name = (str(input("Enter one name : ")))
name = name.capitalize()
if dict.get(name) == None:
     print(f"Student {name} doesnt exist")
else :

    print(f"{name} scored : {dict[name]}%")


