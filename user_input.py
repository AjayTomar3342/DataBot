from tkinter.filedialog import askopenfilename
from process_user_input import process_user_input, graph_plotting
from data_quality_check import data_quality_check
from sentiment_analyzer import sentiment_analyzer
from docx2pdf import convert
from docx import Document
from fpdf import FPDF
from tkinter import font, messagebox

import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog
import pandas as pd
import openpyxl as op

# Tooltip Class
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tooltip_window is not None:  
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip_window, text=self.text, background="black", borderwidth=2, relief="solid",  padx=5, pady=5)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window is not None:
            self.tooltip_window.destroy()
            self.tooltip_window = None


# Create the main tkinter window
root = tk.Tk()
root.title("DataBot")
root.geometry("400x400")


# Center the window on the screen
window_width = 400
window_height = 400

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry with the calculated coordinates
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.configure(bg="#D3D3D3")  # Light background color

# Define a custom font
custom_font = font.Font(family="Helvetica", size=12)

# Create a frame for upload buttons
upload_frame = tk.Frame(root, bg="#D3D3D3")
upload_frame.pack(pady=20) 

# Function to send back the resulting docx file to end-user
def send_docx_to_end_user(docx):
    # Open a file dialog to let the user choose where to save the docx file
    file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])

    if file_path:
        docx.save(file_path)  # Save the docx to the chosen path
        print(f"Docx file saved to: {file_path}")
    else:
        print("Save operation cancelled")


# Function to give user the UI to upload Excel file
def upload_file():
    # Open file dialog to select the Excel file
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx; *.xlsm; *.xls")])


    if file_path:  # If the user selected a file
        try:
            # Load the Excel file using pandas
            df = pd.read_excel(file_path)

            # Show the first few rows of the dataframe as an example
            print("File loaded successfully!")

            # Save the file physically
            df.to_csv('User Files/input_df.csv')

            # Message to user if file upload was successfull
            messagebox.showerror("Success", f"File Uploaded Successfully")


        except Exception as e:
            print(f"Error loading file: {e}")
    else:
        print("No file selected.")

        # Message to user if file upload was not successfully
        messagebox.showerror("Error", f"File Uploaded Failed. Try Again.")


# Function to give user the UI to submit analysis instructions
def get_user_instructions():

    # Open dialog box to allow user to input instructions
    instruction = simpledialog.askstring("How may I help you?", "Enter your thoughts:"
    , initialvalue="Please create a dotplot for Column Age and Column Id", parent=root)

    if instruction:  # If the user submitted an instruction
        try:

            print("Instruction Received!")
            # Submit user instruction to be analyzed for creating plots
            plot_info = process_user_input(instruction)
            print("Instruction: ", instruction)
            # Plot the required graphs
            figure, error_message =  graph_plotting(plot_info)
            print("Error Message", error_message)
            # Check if there was a column name error
            if error_message == "Column Name Error":
                messagebox.showerror("Error", f"Column Name not found. Please make sure you used the "
                                              f"correct column name and there are no spaces within the column name")

        except Exception as e:
            print(f"Instruction Format Unclear : {e}")
    else:
        print("No instruction submitted.")


# Function to handle Data Quality Check request
def data_quality_check_button():
    # Open file dialog to select the Excel file
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx; *.xlsm; *.xls")])

    if file_path:  # If the user selected a file
        try:
            # Load the Excel file using pandas
            data_quality_check_df = pd.read_excel(file_path)

            # Show the first few rows of the dataframe as an example
            print("File loaded successfully!")

            # Save the file physically
            data_quality_check_df.to_csv('User Files/data_quality_check_df.csv')

            # Message to user if file upload was successfull
            messagebox.showerror("Success", f"File Uploaded Successfully")

            result = data_quality_check()

            # Send back the file to end-user
            send_docx_to_end_user(result)

        except Exception as e:
            print(f"Error loading file: {e}")
    else:

        # Message to user if file upload was not successfull
        messagebox.showerror("Error", f"File Uploaded Failed. Try Again.")

        print("No file selected.")

    # # Read the resulting docx file
    # doc = Document('Result Files/Data Quality Report.docx')




# Function to give user the UI to submit sentiment analysis text
def get_sentiment_analysis_text():

    # Open dialog box to allow user to input text
    instruction = simpledialog.askstring("Input text to be analyzed:", "Enter required text:"
    , initialvalue="Simply Write", parent=root)

    if instruction:  # If the user submitted an instruction
        try:
            print("Input Text Received!")

            # Message to user if file upload was successfull
            messagebox.showerror("Success", f"Text Uploaded Successful")

            sentiment_analyzer(instruction)


        except Exception as e:
            print(f"Input Text Format Unclear : {e}")
    else:
        # Message to user if text upload was not successfull
        messagebox.showerror("Error", f"Text Upload Failed. Try Again.")

        print("No input text submitted.")

    # Read the resulting docx file
    doc = Document('Result Files/Sentiment Analysis Report.docx')

    # Send back the file to end-user
    send_docx_to_end_user(doc)



# Create an upload button for uploading Excel file
upload_button1 = tk.Button(upload_frame, text="Upload Excel File", command=upload_file, font=custom_font,
                           bg="#4CAF50", fg="black")
upload_button1.pack(pady=10, padx=20)
ToolTip(upload_button1, "Upload the excel file which you want to use for the creation of graphical plots")


# Create a button to allow user to input their instructions
button1 = tk.Button(upload_frame, text="Submit Instructions", command=get_user_instructions, font=custom_font,
                    bg="#2196F3", fg="black")
button1.pack(pady=10, padx=20)
ToolTip(button1, "Submit the instructions based on which graphical plots have to be made")


# Create a button for data quality check
upload_button2 = tk.Button(upload_frame, text="Upload for Data Quality Check", command=data_quality_check_button,
                           font=custom_font, bg="#FF9800", fg="black")
upload_button2.pack(pady=10, padx=20)
ToolTip(upload_button2, "Upload the excel file whose data quality has to be analyzed")


# Create a button for sentiment analysis
button2 = tk.Button(upload_frame, text="Submit Text for Sentiment Analysis", command=get_sentiment_analysis_text,
                    font=custom_font, bg="#9C27B0", fg="black")
button2.pack(pady=10, padx=20)
ToolTip(button2, "Submit text for sentiment analysis.")


# Start the tkinter event loop
root.mainloop()
