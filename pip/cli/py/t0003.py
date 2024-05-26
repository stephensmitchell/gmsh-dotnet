import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Button, Form
# Define event handler function
def button_click(sender, event):
    print("Button clicked!")
# Create a Form
form = Form()
form.Text = "Event Handling Example"
# Create a Button
button = Button()
button.Text = "Click me!"
button.Click += button_click
# Add Button to Form
form.Controls.Add(button)
# Show the Form
form.ShowDialog()
