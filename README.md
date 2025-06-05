
# 🛒 Groceries Management System (12th Grade Project)

Back in 12th grade, I created this simple CLI-based Groceries Management System using **Python** and **MySQL**. It wasn’t anything fancy, but it marked my very first step into the world of programming. 🌟

This basic inventory tool allows users to:
- Add grocery items
- Remove items
- Update quantity or price
- View the entire list in a tabular format

Although I had no knowledge of AI or frameworks back then, I built this entirely through trial and error. And surprisingly—it worked! 💻✨

> 💡 Fun Fact: This became a go-to project for my juniors in school who reused it for their own submissions. 😉

---

## 🔧 Features

- 📦 Add items with name, quantity, and price
- 🗑️ Remove items using ID
- 🔁 Modify item price and quantity
- 📋 Display all inventory items in a clean table
- 💾 Uses MySQL for persistent data storage

---

## 🧰 Tech Stack

- Python 3.x
- MySQL
- `mysql-connector-python` library

---

## 🗄️ MySQL Table Schema

Make sure to create this table before running the script:

```sql
CREATE TABLE ITEM_LIST (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Item VARCHAR(50),
  Quantity INT,
  Price INT
);
````

---

## ▶️ How to Run

1. Install required package:

   ```bash
   pip install mysql-connector-python
   ```

2. Set up your MySQL server and create the `grocerymanagement` database and `ITEM_LIST` table as per the schema above.

3. Update the connection details in the script:

   ```python
   SqlCon.connect(
     host="localhost",
     user="your_mysql_user",
     password="your_mysql_password",
     database="grocerymanagement",
     autocommit=True
   )
   ```

4. Run the Python script:

   ```bash
   python grocerymanagemt.py
   ```

---

## 📸 Demo

```
+-------------------------------------------------------+
|ID   |Item               |Quantity       |Price   |
+-------------------------------------------------------+
|1    |Milk               |2              |50      |
|2    |Rice               |5              |120     |
+-------------------------------------------------------+
```

---

## 📚 What I Learned

* Basics of SQL and database connections
* CRUD operations through Python
* Structuring command-line applications
* Trial-and-error debugging

---

