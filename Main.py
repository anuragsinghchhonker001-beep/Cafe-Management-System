from tkinter import *
from tkinter import messagebox
import sqlite3

# Prices
coffee_price = 50
burger_price = 120
pizza_price = 250

# Save Order
def save_order(name, bill):
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders(customer_name,total_bill) VALUES (?,?)",
        (name, bill)
    )

    conn.commit()
    conn.close()

# Generate Bill
def generate_bill():

    name = customer_entry.get()

    if name == "":
        messagebox.showerror("Error", "Enter Customer Name")
        return

    coffee_qty = int(coffee.get() or 0)
    burger_qty = int(burger.get() or 0)
    pizza_qty = int(pizza.get() or 0)

    total = (
        coffee_qty * coffee_price +
        burger_qty * burger_price +
        pizza_qty * pizza_price
    )

    bill_text.delete(1.0, END)

    bill_text.insert(
        END,
        f"------ CAFE BILL ------\n\n"
    )

    bill_text.insert(
        END,
        f"Customer : {name}\n\n"
    )

    bill_text.insert(
        END,
        f"Coffee x {coffee_qty} = ₹{coffee_qty*coffee_price}\n"
    )

    bill_text.insert(
        END,
        f"Burger x {burger_qty} = ₹{burger_qty*burger_price}\n"
    )

    bill_text.insert(
        END,
        f"Pizza x {pizza_qty} = ₹{pizza_qty*pizza_price}\n"
    )

    bill_text.insert(
        END,
        f"\nTotal Bill = ₹{total}"
    )

    save_order(name, total)

root = Tk()
root.title("Cafe Management System")
root.geometry("700x500")

Label(
    root,
    text="CAFE MANAGEMENT SYSTEM",
    font=("Arial",18,"bold")
).pack(pady=10)

Label(root,text="Customer Name").pack()

customer_entry = Entry(root,width=30)
customer_entry.pack()

frame = Frame(root)
frame.pack(pady=20)

Label(frame,text="Coffee (₹50)").grid(row=0,column=0)
coffee = Entry(frame)
coffee.grid(row=0,column=1)

Label(frame,text="Burger (₹120)").grid(row=1,column=0)
burger = Entry(frame)
burger.grid(row=1,column=1)

Label(frame,text="Pizza (₹250)").grid(row=2,column=0)
pizza = Entry(frame)
pizza.grid(row=2,column=1)

Button(
    root,
    text="Generate Bill",
    command=generate_bill
).pack(pady=10)

bill_text = Text(root,height=15,width=50)
bill_text.pack()

root.mainloop()