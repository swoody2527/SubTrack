
from tkinter import *
from tkinter import ttk
import tkinter
import subtrack as st

def main_menu():
    root = Tk()
    root.title("SubTrack")
    root.geometry("800x400")
    root.resizable(0,0)
    ttk.Label(
        root,
        text="SubTrack",
        font=("Helvetica", 22)).place(x=340, y=20)
    ttk.Button(root, text="View Current Subscriptions", padding="20 20 20 20", command=view).grid(
        row=1,
        column=1,
        padx=(125,10),
        pady=100)
    ttk.Button(root, text="Add Subscription", padding="20 20 20 20", command=add).grid(
        row=1,
        column=2,
        padx=10,
        pady=100)
    ttk.Button(root, text="Delete Subscription", padding="20 20 20 20", command=delete).grid(
        row=1,
        column=3,
        padx=10,
        pady=100)
    ttk.Button(root, text="Exit", command=lambda: root.quit())
    root.mainloop()


def view():
    st.check_over()
    subs = st.get_subs()
    subs = [list(row) for row in subs]
    root = Tk()
    root.title("SubTrack: View Subscriptions")
    root.resizable(0,0)
    if subs == []:
        root.geometry("400x50")
        ttk.Label(root, font=("Helvetica", 16), text="No active subscriptions currently exist").grid(column=0, row=0)
    else:
        root.update()
        root.geometry("625x400")
        headers = ["Name", "Price", "Start Date", "Renewal", "Next Charge"]
        for i in range(5):
            Label(root, text=headers[i], font=("Helvetica", 16)).grid(row=0, column=i)
        height = len(subs)
        for i in range(height):
            for j in range(5):
                b = ttk.Entry(root, text="")
                if j == 2 or j == 4:
                    format_date = st.format_view_dates(subs[i][j])
                    b.insert(0,format_date)
                else:
                    b.insert(0,subs[i][j])
                b.config(state=DISABLED)
                b.grid(row=i+1, column=j)
        return root

def add():
    root = Tk()
    root.title("SubTrack: Add a Subscription")
    headers = ["Name", "Price", "Start Date(dd/mm/yyyy)", "Renewal(months)"]
    ttk.Label(root, text="Add a Subscription", font=("Helvetica", 16)).grid(row=0, column=1, columnspan=2)
    for i in range(4):
        Label(root, text=headers[i], font=("Helvetica", 12)).grid(row=1, column=i)
    name = ttk.Entry(root, text="")
    name.grid(row=2, column=0, padx=5)
    price = ttk.Entry(root)
    price.grid(row=2, column=1, padx=5)
    start_date = ttk.Entry(root)
    start_date.grid(row=2, column=2, padx=5)
    renewal = ttk.Entry(root)
    renewal.grid(row=2, column=3, padx=5)
    enter_btn =ttk.Button(root, text="Add Subscription", padding="10 10 10 10", command=lambda: [st.insert(st.Sub(name.get(), price.get(), st.dateobj(start_date.get()), renewal.get())), root.destroy(), st.check_over()])
    enter_btn.grid(pady=10 ,row=3, column=1, columnspan=2)


def delete():
    subs = st.get_subs()
    if subs == []:
        root = view()
    else:
        root = view()
        root.title("SubTrack: Delete A Subscription")
        ttk.Label(root, text="Subscription Name").grid(column=0, row=len(subs)+1, pady=(10,0))
        del_entry = ttk.Entry(root)
        del_entry.grid(column=0, row=len(subs)+2)
        ttk.Button(root, text="Delete Subscription", command=lambda: del4_gui(del_entry.get(), subs)).grid(column=1, row=len(subs)+2,)

def del4_gui(del_name, subs):
    check_root = Tk()
    check_root.title("Confirm Deletion")
    if del_name in (item[0] for item in subs):
        check_label = ttk.Label(check_root, text=f"Are you sure you want to delete {del_name} from subscriptions?")
        check_label.grid(row=0,column=0, columnspan=2)
        print(del_name)
        ttk.Button(check_root, text="Yes", command=lambda: [st.delete2(del_name), check_root.destroy()]).grid(column=0, row=1)
        ttk.Button(check_root, text="No", command=lambda: check_root.destroy()).grid(column=1, row=1)
    else:
        error_msg = ttk.Label(check_root,font=("Helvetica", 16), text=f"No subscripton for {del_name} exists").grid(column=1, row=2)

if __name__=="__main__":
    st.check_over()
    main_menu()