import mysql.connector as SqlCon        #importing mysql.connector module to connect mysql with python


connection = SqlCon.connect(host="localhost",user="root",password = "Dharshan18@Mysql",database = "grocerymanagement",autocommit=True)  #It connects with mysql using required components
cursor = connection.cursor()  #cursor is for interact the user with mysql tables

def Display():          #to display all the contents in the table
	cursor.execute("select * from ITEM_LIST")     #    to collect the data and have in the cursor from table
	data = cursor.fetchall()      #by cursor fetching all data's and printing it
	print("\n+-------------------------------------------------------+\n|ID\t|Item\t\t\t|Quantity\t|Price\t|\n+------------------------------+")
	for i in data:  #to display the data as per in table by fetching it
		print(f"|{i[0]}\t|{i[1]}\t|{i[2]}\t\t|{i[3]}")
		print("+-------------------------------------------------------+")

def Update(info): #to add any new value to the table by getting "info" as argument
		cursor.execute("select * from ITEM_LIST") #to collect the data and have in the cursor from table
		data = cursor.fetchall() #by cursor fetching all data's and printing it
		
		cursor.execute(f"insert into ITEM_LIST values(NULL,'{info[1]}',{info[2]},{info[2]})") #sql command to insert the given values by the user

def Remove(ID): #to remove or del the element from table by getting "ID" as argument
		cursor.execute(f"delete from ITEM_LIST where ID = {ID}") #sql command to del the data entered by the user


def ModifyPrice(ID,Price):#to update the price in table by getting "ID" and "Price" as argument
		cursor.execute(f"Update ITEM_LIST set Price = {Price} where ID = {ID}")	#sql command to update the price in table

def ModifyQuantity(ID,Quantity):#to update the quantity in table by getting "ID" and "Price" as argument
		cursor.execute(f"Update ITEM_LIST set Quantity = {Quantity} where ID = {ID}") #sql command to update the quality in table



while True: #to loop the below all components
	
	Display() #this function call will display the structure of the table
	Do = input("\n1>Add\n2>Remove Item\n3>Modify Price\n4>Modify Quantity\n5>Exit\n>>>")#just input statement to get input from the user
	
	if Do == "1": #if user's choice is 1,it will add the content to the table
		Item = input("Item Name: ")
		Quantity = int(input("Item Quantity: "))
		Price = int(input("Item Price: "))
		Update((Item,Quantity,Price)) #this function call will pass all the values entered by user to add in table


	elif Do == "2": #if user's choice is 3,it will remove the data from table
		ID = int(input("Item ID: "))
		Remove(ID)#this function call will pass all the value entered by user to remove data in table
	
	elif Do =="3":#if user's choice is 4,it will update the price of the table
		ID = int(input("Enter ID: "))
		Price = int(input("Enter Price: "))
		ModifyPrice(ID,Price)#this function call will pass all the values entered by user to update the price of the table

	elif Do == "4":#if user's choice is 5,it will update the quantity of the table
		ID = int(input("Enter ID: "))
		Quantity = int(input("Enter Quantity: "))
		ModifyQuantity(ID,Quantity)#this function call will pass all the values entered by user to update the quantity of the table
		ModifyQuantity(ID,Quantity)#this function call will pass all the values entered by user to update the quantity of the table
	elif Do == "5":#if user's choice is 6,it will quit from process
		break  #it will end the loop
	else:
		break
