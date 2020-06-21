# gui-user-input
This is a library for GUI user input

## Usage:
```python
import user_input as ui
result = ui.start_gui()
#or
result = ui.start_gui(button_text=["Confirm", "Cancel"], error_text="The field cannot be empty", title="This is a title")
```
Where result is a an empty string or a string with characters depending on the user input

![User Input Demo](user_input_demo.gif)