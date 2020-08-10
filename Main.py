from tkinter import *
from tkinter import ttk
from People import people
from Bank import bank
import tkinter.messagebox


##### create misc. items needed for project

months_list = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October', 'November', 'December']

year_list = []
year = 2010
for _ in range(0, 11):
    year_list.append(year)
    year += 1

trip = bank()

trip_members = []
###### create window one

window = Tk()
window.title('Trip Finance Program')
window.geometry('566x350+500+200')
window.resizable(False, False)
##### Make frame for trip name & date then put widgets inside

frame_one_left = ttk.LabelFrame(window, text="Trip Name & Date", width=243, height=150)
frame_one_left.grid_propagate(0)
frame_one_left.grid(row=0, column=0, padx=20, pady=10)

trip_name_entry_text = Label(frame_one_left, text="Trip Name:")
trip_name_entry_text.grid(row=0, column=0, padx=15, pady=5, sticky=W+S)

trip_name_entry = Entry(frame_one_left, width=34)
trip_name_entry.grid(row=1, column=0, padx=15, columnspan=2, sticky=W)

month_box = ttk.Combobox(frame_one_left, width=10, values=months_list)
month_box.grid(row=2, column=0, padx=15, pady=15, sticky=W)
month_box.current(0)

year_box = ttk.Combobox(frame_one_left, width=10, values=year_list)
year_box.grid(row=2, column=1, padx=25, pady=15, sticky=W)
year_box.current(10)

trip_name_warning = Label(frame_one_left, fg="red")
trip_name_warning.grid(row=0, column=1, padx=10, pady=5, sticky=W)


def add_name_date():

    if trip_name_entry.get() != "":
        trip_name_warning.configure(text='')
        trip.set_trip_name(trip_name_entry.get())
        trip.set_trip_date(month_box.get(), year_box.get())

        trip_name_entry.delete(0, END)
        month_box.current(0)
        year_box.current(10)

        current_trip_name.configure(text=trip.get_trip_name())
        current_trip_date.configure(text=(trip.get_trip_month()+" "+trip.get_trip_year()))
    else:
        trip_name_warning.configure(text="*enter valid name")


submit_button = ttk.Button(frame_one_left, width=10, text="Apply", command=lambda: add_name_date())
submit_button.grid(row=3, column=0, padx=20, columnspan=2, pady=0)


###### trip participants

frame_one_right = ttk.LabelFrame(window, text="Trip Participants", width=243, height=150)
frame_one_right.grid_propagate(0)
frame_one_right.grid(row=0, column=1, padx=20, pady=10)

name_text = Label(frame_one_right, text="Enter Name:")
name_text.grid(row=0, column=0, padx=15, pady=5, sticky=W+S)

name_entry = Entry(frame_one_right, width=34)
name_entry.grid(row=1, column=0, padx=15, columnspan=2, sticky=W)

name_warning = Label(frame_one_right, fg="red")
name_warning.grid(row=0, column=1, padx=15, pady=5, sticky=W)


def add_name():

    if name_entry.get() != "":
        name_warning.configure(text='')
        trip_members.append(people(name_entry.get()))

        temp_string = ""

        for People in trip_members:
            temp_string = temp_string+People.get_name()
            temp_string = temp_string+" "

        name_entry.delete(0, END)
        current_trip_participants.configure(text=temp_string)

    else:
        name_warning.configure(text="*enter valid name")


add_name_button = ttk.Button(frame_one_right, width=15, text="Add Participant", command=lambda: add_name())
add_name_button.place(x=70, y=100)



##### current trip

frame_one_current = ttk.LabelFrame(window, text="Trip Info", width=526, height=90)
frame_one_current.grid_propagate(0)
frame_one_current.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

trip_name = Label(frame_one_current, text="Trip Name:")
trip_name.grid(row=0, column=0, padx=5, sticky=W)

trip_date = Label(frame_one_current, text="Trip Date:")
trip_date.grid(row=1, column=0, padx=5, sticky=W)

trip_participants = Label(frame_one_current, text="Trip Participants:")
trip_participants.grid(row=2, column=0, padx=5, sticky=W)

current_trip_name = Label(frame_one_current)
current_trip_name.grid(row=0, column=1, padx=4, sticky=W)

current_trip_date = Label(frame_one_current)
current_trip_date.grid(row=1, column=1, padx=4, sticky=W)

current_trip_participants = Label(frame_one_current)
current_trip_participants.grid(row=2, column=1, padx=4, sticky=W)


#### main window info

def next_page_click():
    if current_trip_name['text'] == "" or current_trip_participants['text'] == "" or len(trip_members) < 2:
        first_page_warning.configure(text='*to move on enter a valid trip name and at least two participants')
    else:
        window.destroy()


next_page_button = ttk.Button(window, text="Next Page", width=10, command=lambda: next_page_click())
next_page_button.place(x=477, y=295)


def quit_click():
    if tkinter.messagebox.askyesno(title='Warning', icon="warning",
                                   message='all progress will be lost if you quit, continue?'):
        window.destroy(), sys.exit()


quit_button = ttk.Button(window, text="Quit", width=10, command=lambda: quit_click())
quit_button.place(x=20, y=295)

first_page_warning = Label(window, fg="red")
first_page_warning.place(x=200, y=270)

page_number = Label(window, text="Page 1 of 3")
page_number.place(x=500, y=330)


def doSomething():
    # check if saving
    # if not:
    window.destroy()
    sys.exit()


window.protocol('WM_DELETE_WINDOW', doSomething)


window.mainloop()



######################### WINDOW TWO ###################################


window_two = Tk()
window_two.title('Trip Finance Program')
window_two.geometry('566x350+500+200')
window_two.resizable(False, False)


###### every participant notebook for adding individual expenses

names = ttk.Notebook(window_two)
names.configure(width=526, height=125)
names.grid_propagate(0)


for people in trip_members:
    tab = ttk.Frame(names)
    names.add(tab, text=people.get_name())

    purchase_price_text = Label(tab, text="Purchase price ($):")
    purchase_price_text.grid(row=0, column=0, padx=15, pady=10, sticky=E)
    purchase_price_entry = Entry(tab)
    purchase_price_entry.grid(row=0, column=1, pady=10, columnspan=2)

    purchase_description_text = Label(tab, text="Purchase Descrip:")
    purchase_description_text.grid(row=1, column=0, padx=15, pady=5, sticky=E)
    purchase_description_entry = Entry(tab)
    purchase_description_entry.grid(row=1, column=1, pady=5, columnspan=2)

    purchases_text = Label(tab, text="Purchases:")
    purchases_text.grid(row=0, column=3, padx=20, sticky=E)

    purchases = Listbox(tab, width=25, height=6)
    purchases.grid(row=0, column=4, rowspan=3, sticky=W)

    def add_purchase(people, price, descrip, purchase_list, price_entry, description_entry):

        def is_number(price):
            try:
                float(price)
                return True
            except ValueError:
                return False

        if price == "" or descrip == "":
            incorrect_price_warning.configure(text='*invalid entry')
        elif is_number(price) is False:
            incorrect_price_warning.configure(text='*invalid price')
        else:
            incorrect_price_warning.configure(text='')

            people.add_purchase(price)
            people.add_description(descrip)
            people.add_purchase_descrip(round(float(price), 4), descrip)

            purchase_list.delete(0, END)

            for items in people.get_purchase_descrip():
                purchase_list.insert(0, items)

            price_entry.delete(0, END)
            description_entry.delete(0, END)

            people.set_total()
            trip.add_total_spent(price)
            trip.set_individual_debt(len(trip_members))
            current_trip_cost.configure(text=("$"+str(round(trip.get_total_spent(), 2))))
            current_cost_person.configure(text=("$"+str(round(trip.get_individual_debt(), 2))))


    add_purchase_button = ttk.Button(tab, text="Add Purchase",
                                     command=lambda people=people, purchase_description_entry=purchase_description_entry,
                                                    purchase_price_entry=purchase_price_entry, purchases=purchases:
                                     add_purchase(people, purchase_price_entry.get(), purchase_description_entry.get(),
                                                  purchases, purchase_price_entry, purchase_description_entry))
    add_purchase_button.grid(row=2, column=0, pady=12, columnspan=2, sticky=E)


names.grid(row=0, column=0, padx=20, pady=10)


##### current trip info

current_trip_info = ttk.LabelFrame(window_two, text="Current Trip Info", width=526, height=90)
current_trip_info.grid_propagate(0)
current_trip_info.grid(row=1, column=0, padx=20, pady=10)

trip_name = Label(current_trip_info, text="Trip Name:")
trip_name.grid(row=0, column=0, padx=5, sticky=W)

trip_date = Label(current_trip_info, text="Trip Date:")
trip_date.grid(row=1, column=0, padx=5, sticky=W)

trip_participants = Label(current_trip_info, text="Trip Participants:")
trip_participants.grid(row=2, column=0, padx=5, sticky=W)

current_trip_name = Label(current_trip_info, text=trip.get_trip_name())
current_trip_name.grid(row=0, column=1, padx=4, sticky=W)

current_trip_date = Label(current_trip_info, text=(trip.get_trip_month()+" "+trip.get_trip_year()))
current_trip_date.grid(row=1, column=1, padx=4, sticky=W)

names_string = ""
for people in trip_members:
    names_string = names_string + people.get_name() + " "

current_trip_participants = Label(current_trip_info, text=names_string)
current_trip_participants.grid(row=2, column=1, padx=4, sticky=W)

trip_total = Label(current_trip_info, text="Total Trip Cost:")
trip_total.grid(row=0, column=2, padx=15, sticky=W)

cost_per_person = Label(current_trip_info, text="Cost Per Participant:")
cost_per_person.grid(row=1, column=2, padx=15, sticky=W)

current_trip_cost = Label(current_trip_info, text=("$"+str(trip.get_total_spent())), fg="green3")
current_trip_cost.grid(row=0, column=3, padx=4, sticky=W)

current_cost_person = Label(current_trip_info, text=("$"+str(trip.get_individual_debt())), fg="green3")
current_cost_person.grid(row=1, column=3, padx=4, sticky=W)


##### current page info and buttons

incorrect_price_warning = Label(window_two, fg="red")
incorrect_price_warning.place(x=58, y=62)


def next_page_click():
    if tkinter.messagebox.askyesno(title='Warning', icon="warning",
                                   message='Before continuing make sure all purchases have been entered, continue?'):
        window_two.destroy()


next_page_button = ttk.Button(window_two, text="Finish", width=10, command=lambda: next_page_click())
next_page_button.place(x=477, y=295)


def quit_click():
    if tkinter.messagebox.askyesno(title='Warning', icon="warning",
                                   message='all progress will be lost if you quit, continue?'):
        window_two.destroy(), sys.exit()


quit_button = ttk.Button(window_two, text="Quit", width=10, command=lambda: quit_click())
quit_button.place(x=20, y=295)

page_number = Label(window_two, text="Page 2 of 3")
page_number.place(x=500, y=330)


def doSomething():
    # check if saving
    # if not:
    window_two.destroy()
    sys.exit()


window_two.protocol('WM_DELETE_WINDOW', doSomething)

window_two.mainloop()

###############calculate all payments

for people in trip_members:
    people.set_debt(float(trip.get_individual_debt()))

for people in trip_members:
    people.set_debt_temp()

for people in trip_members:
    if people.get_debt() < 0:
        for items in trip_members:
            if items.get_name() != people.get_name():
                if (people.get_debt() * -1) >= items.get_debt() > 0:
                    people.add_payment(items.get_debt())
                    people.add_pay_who(items.get_name())
                    people.update_temp_debt(items.get_debt())
                    items.pay_temp_debt(items.get_debt())
                elif (people.get_debt() * -1) <= items.get_debt():
                    people.add_payment(people.get_temp_debt()*-1)
                    people.add_pay_who(items.get_name())
                    items.pay_temp_debt(people.get_temp_debt())
                    people.update_temp_debt(people.get_temp_debt())

for people in trip_members:
    people.round_payments()
    people.round_purchases()

############ create window three

window_three = Tk()
window_three.title('Trip Finance Program')


######### trip info

current_trip_info = ttk.LabelFrame(window_three, text="Current Trip Info", width=526, height=90)
current_trip_info.grid_propagate(0)
current_trip_info.grid(row=0, column=0, padx=20, pady=10)

trip_name = Label(current_trip_info, text="Trip Name:")
trip_name.grid(row=0, column=0, padx=5, sticky=W)

trip_date = Label(current_trip_info, text="Trip Date:")
trip_date.grid(row=1, column=0, padx=5, sticky=W)

trip_participants = Label(current_trip_info, text="Trip Participants:")
trip_participants.grid(row=2, column=0, padx=5, sticky=W)

current_trip_name = Label(current_trip_info, text=trip.get_trip_name())
current_trip_name.grid(row=0, column=1, padx=4, sticky=W)

current_trip_date = Label(current_trip_info, text=(trip.get_trip_month()+" "+trip.get_trip_year()))
current_trip_date.grid(row=1, column=1, padx=4, sticky=W)

names_string = ""
for people in trip_members:
    names_string = names_string + people.get_name() + " "

current_trip_participants = Label(current_trip_info, text=names_string)
current_trip_participants.grid(row=2, column=1, padx=4, sticky=W)

trip_total = Label(current_trip_info, text="Total Trip Cost:")
trip_total.grid(row=0, column=2, padx=15, sticky=W)

cost_per_person = Label(current_trip_info, text="Cost Per Participant:")
cost_per_person.grid(row=1, column=2, padx=15, sticky=W)

current_trip_cost = Label(current_trip_info, text=("$"+str(round(trip.get_total_spent(), 2))), fg="green3")
current_trip_cost.grid(row=0, column=3, padx=4, sticky=W)

current_cost_person = Label(current_trip_info, text=("$"+str(round(trip.get_individual_debt(), 2))), fg="green3")
current_cost_person.grid(row=1, column=3, padx=4, sticky=W)


############### financial details info

participant_trip_info = ttk.LabelFrame(window_three, text="Individual Trip Details")


column = 0

for people in trip_members:
    row = 0

    name = Label(participant_trip_info, text=(people.get_name()))
    name.grid(row=row, column=column, pady=5, padx=5, sticky=W)

    purchase_label = Label(participant_trip_info, text="Purchases:")
    purchase_label.grid(row=row+1, column=column, pady=5, padx=5, sticky=W)

    if len(people.get_purchase()) > 0:
        temp_row = 2
        for items in people.get_purchase_descrip():
            purchases = Label(participant_trip_info, text=items)
            purchases.grid(row=temp_row, column=column, pady=5, padx=5, sticky=W)
            temp_row += 1

    payments_label = Label(participant_trip_info, text="You Owe:")
    payments_label.grid(row=row+1, column=column+1, pady=5, padx=10, columnspan=2, sticky=W)

    if len(people.get_pay()) > 0:
        temp_row = 2
        for x in range(0, len(people.get_pay())):

            pay_who = Label(participant_trip_info, text=people.get_pay_who()[x])
            pay_who.grid(row=temp_row, column=column+1, pady=5, padx=5, sticky=W)

            payment = Label(participant_trip_info, text=("$"+str(people.get_pay()[x])), fg="green3")
            payment.grid(row=temp_row, column=column+2, pady=5, padx=5, sticky=W)

            temp_row += 1

    column = column + 3

participant_trip_info.grid(row=1, column=0, padx=20, pady=10)

window_three.mainloop()



