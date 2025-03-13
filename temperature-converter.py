from nicegui import ui

ui.colors(
      primary='#5ea6e0',
      secondary='#fffff',
      accent='#5ea6e0',
      positive='#58cc73',
      negative='#c10015',
      info='#9d00ff',
      warning='#ffe499'
)


def convert():
    try: 
        temp = float(input_field.value)
        temp_2 = float(slider.value)  
        result_label.classes(remove="text-negative", add="text-positive")
        result_label.classes("text-lg font-semibold text-positive mt-4")

        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
            result_label.set_text(f"{temp_2}°C = {temp_2 * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
            result_label.set_text(f"{temp_2}°F = {(temp_2 - 32) * 5/9:.2f}°C")

        # text-positive: applies the color associated with "positive" to the text

    except ValueError:
        result_label.set_text("Please enter a valid number.")

        result_label.classes(remove="text-positive", add="text-negative")
        result_label.classes("text-lg font-semibold text-negative mt-4")

        # text-negative: applies the color associated with "negative" to the text


with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
    # w-100: Set element width to be fixed at 100
    # p-6: the p controls an elements padding on all sides, the 6 means a padding of 6
    # shadow-xl: creates an xl drop shadow
    # mx-auto: automatically sets the margins for an element
    # mt-10: sets a top margin to of 10
    # rounded-xl: controls the border radius of an element. the xl means a xl border radius

    ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")

    # text-2xl: controls the font size of an element. in this case it makes the font 2xl
    # font-bold: sets the font weight to be bold
    # text-accent:
    # mb-4: sets a bottom margin of 4

    with ui.row().classes("mx-auto"):
        with ui.card():
            input_field = ui.input("Enter Temperature").props('type="number"').classes("w-50 mb-4 p-2 text-lg border rounded")
        with ui.card():
            ui.label("Enter Temperature")

            ## creates a slider for temperature change
            slider = ui.slider(min=-100, max=100, step = 0.01, value = 0)
            ui.label().bind_text_from(slider, 'value')      
            
            ## toggling the slider on and off 
            ui.button('Enable slider', on_click=slider.enable)
            ui.button('Disable slider', on_click=slider.disable)


        # w-full: sets width at 100%
        # border: sets a border of 1px around an element
        # rounded: sets a border radius

        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")

        # text-white: makes the text white
        # py-2: sets a vertical padding of 2 to an element
        # px-4: sets a horizontal padding of 4 to an element

        result_label = ui.label("").classes("text-lg mt-4")

ui.run()