import tkinter as tk
import query



# Create the main application window
root = tk.Tk()
root.title("Path of Exile Currency Tracker")



# Window Size
root.geometry("600x600")


# Create a Frame to contain the widgets
frame = tk.Frame(root)
frame.pack(side = 'left', anchor="nw")

# Currency queries from POE ninja API

button1 = tk.Button(frame, text="Softcore", padx=20, pady=10 , command=lambda: query.currencyquery("Softcore",text))
button2 = tk.Button(frame, text="Hardcore", padx=20, pady=10, command=lambda: query.currencyquery("Hardcore",text))

button1.pack(side="top", padx = 20, pady = 20, anchor="nw")
button2.pack(side="top", padx = 20, pady = 20, anchor="nw")

# Create a Text widget to display multi-line text
text = tk.Text(root,width=100, height=100, padx = 20, pady = 20)
text.pack(pady = 10, padx = 10, side="right")

# Insert function





# Run the application's event loop
root.mainloop()