from tkinter import *
from tkinter import messagebox

class TicketSales(object):
    def __init__(self, window):
        self.window = window
        self.window.title("TicketSales")
        self.window.geometry("500x500")
        self.window.config()

        # enter mobile number label and entry placement
        self.cell_entry_label = Label(self.window, text="Enter Mobile Number:")
        self.cell_entry = Entry(self.window)
        self.cell_entry_label.place(x=10, y=10)
        self.cell_entry.place(x=220, y=10)

        # placing category of ticket label and dropbox
        self.ticket_label = Label(self.window, text="Select Ticket Category:")
        self.options = ["Movie", "Theatre", "Soccer"]
        self.variable = StringVar(self.window)
        self.variable.set("Select Ticket...")
        self.ticket_op = OptionMenu(window, self.variable, *self.options)
        self.ticket_label.place(x=10, y=50)
        self.ticket_op.place(x=220, y=45)

        #  placing the ticket amount box
        self.ticket_no_label = Label(self.window, text="Amount of tickets:",)
        self.ticket_spinbox = Spinbox(self.window, width=10, from_=1, to=99)
        self.ticket_no_label.place(x=10, y=90)
        self.ticket_spinbox.place(x=220, y=90)

        # placing and defining calculation and clear button
        self.calc_button = Button(self.window, text='Calculate', command=self.calc_prepayment)
        self.clear_button = Button(self.window, text='Clear',  command=self.clear)
        self.calc_button.place(x=40, y=200)
        self.clear_button.place(x=250, y=200)

        # the calculated answer Ta Da :)
        self.amount_pay = Label(self.window, text="")
        self.reserve = Label(self.window, text="")
        self.cell_label = Label(self.window, text="")
        self.amount_pay.place(x=50, y=300)
        self.reserve.place(x=50, y=350)
        self.cell_label.place(x=50, y=400)

    # defining commands for calculations and errors
    def calc_prepayment(self):
        ticket_no = int(self.ticket_spinbox.get())
        vat = 0.14
        try:
            int(self.cell_entry.get())
            if len(self.cell_entry.get()) < 10 or len(self.cell_entry.get()) > 10:
                raise ValueError

            elif self.variable.get() == "Please select ticket":
                raise ValueError

            elif int(self.ticket_spinbox.get()) == 0:
                raise ValueError

            elif self.variable.get() == "Soccer":
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            elif self.variable.get() == "Movie":
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            elif self.variable.get() == "Theater":
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            reserve_text = "Reservation for {} for : {} ".format(self.variable.get(), ticket_no)
            cell_text = "Reservation Made By: {}".format(self.cell_entry.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:
            messagebox.showerror(message="Oops! Error!!")

    def clear(self):
        self.cell_entry.delete(0, END)
        self.cell_entry.focus()
        self.variable.set("Select Ticket")
        self.ticket_spinbox.delete(0, END)
        self.ticket_spinbox.insert(0, 0)
        self.amount_pay.config(text="")
        self.reserve.config(text="")
        self.cell_label.config(text="")

root = Tk()
TicketSales(root)
root.mainloop()