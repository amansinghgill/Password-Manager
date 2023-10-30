from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")  # Make sure the logo.png file is in the same directory as this script
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='E')  # Aligned to the right (east)
email_label = Label(text="Username:")
email_label.grid(row=2, column=0, sticky='E')  # Aligned to the right (east)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky='E')  # Aligned to the right (east)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')  # Aligned to both sides (east and west)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')  # Aligned to both sides (east and west)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW')  # Aligned to both sides (east and west)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky='EW')  # Aligned to both sides (east and west)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')  # Aligned to both sides (east and west)

# Ensuring that the columns expand proportionally when the window is resized
window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=1)

window.mainloop()