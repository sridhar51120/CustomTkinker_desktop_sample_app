from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from Components.Dashboard_Frames.Dashboard import tab_dashboard
from Components.Dashboard_Frames.Products import tab_products
import customtkinter

app = CTk()
app.geometry("856x645")
app.resizable(0, 0)
set_appearance_mode("light")

# Create a tab frame to hold different tabs
tab_frame = CTkTabview(master=app)
tab_frame.pack(fill="both", expand=True)

# Create tabs and associate them with corresponding content
tab_frame.add("Dashboard")
tab_frame.add("Products")
tab_frame.add("Billing")  # Add corresponding function for billing
tab_frame.add("Selling")  # Add corresponding function for selling
tab_frame.add("Profile")  # Add corresponding function for profile

# Add content to tabs
tab_frame.add_frame(dashboard_tab, lambda: tab_dashboard(tab_frame))
tab_frame.add_frame(products_tab, lambda: tab_products(tab_frame))
# Add content for other tabs as needed

# Start with the Dashboard tab selected
tab_frame.select_tab(dashboard_tab)
app.mainloop()
