from tkinter import Tk, Text, filedialog, Button, IntVar, Menu, Menubutton, Canvas, Scrollbar, BOTH, VERTICAL, HORIZONTAL
import markdown as md

root = Tk()
text = Text(root)
text.grid()

# Definir canvas como una variable global
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.grid(row=0, column=1, rowspan=2,columnspan=2)

# Agregar barras de desplazamiento
vertical_scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
vertical_scrollbar.grid(row=0, column=3, sticky="ns")  # Cambio en la posición de la barra de desplazamiento vertical
canvas.config(yscrollcommand=vertical_scrollbar.set)

horizontal_scrollbar = Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
horizontal_scrollbar.grid(row=1, column=1, columnspan=2, sticky="ew")  # Cambio en la posición de la barra de desplazamiento horizontal
canvas.config(xscrollcommand=horizontal_scrollbar.set)

# Definir canvas para el "Context Hub"
canvas_context_hub = Canvas(root, width=200, height=300, bg='lightgray')
canvas_context_hub.grid(row=0, column=3, sticky="n")

# Función para obtener el texto seleccionado en el editor de texto
def get_selected_text():
    selected_text = text.get("sel.first", "sel.last")
    return selected_text

# Función para mostrar el texto seleccionado en el "Context Hub"
def show_selected_text():
    selected_text = get_selected_text()
    canvas_context_hub.delete("all")  # Limpiar cualquier contenido previo
    canvas_context_hub.create_text(100, 150, text=selected_text, font=("Arial", 12), justify="center")

# Botón para mostrar el texto seleccionado en el "Context Hub"
show_context_button = Button(root, text="Show Selected Text", command=show_selected_text)
show_context_button.grid(row=1, column=3, sticky="s")

# Función para generar contexto con el texto seleccionado
def generate_context():
    selected_text = get_selected_text()
    # Aquí puedes realizar alguna acción con el texto seleccionado, como procesarlo para generar contexto
    pass

# Botón para generar contexto con el texto seleccionado
generate_context_button = Button(root, text="Generate Context", command=generate_context)
generate_context_button.grid(row=2, column=3, sticky="n")



def saveas():
    global text

    t = text.get("1.0", "end-1c")

    savelocation = filedialog.asksaveasfilename()

    file1 = open(savelocation, "w+")

    file1.write(t)

    file1.close()

def OpenFile():
    global text

    # Obtener la ubicación del archivo seleccionado por el usuario
    file_path = filedialog.askopenfilename()

    # Verificar si se seleccionó un archivo
    if file_path:
        # Intentar abrir el archivo seleccionado en modo lectura
        try:
            with open(file_path, 'r') as file:
                # Leer el contenido del archivo
                file_content = file.read()

                # Limpiar el contenido actual del widget Text
                text.delete('1.0', 'end')

                # Insertar el contenido del archivo en el widget Text
                text.insert('1.0', file_content)
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir al abrir el archivo
            print("Error al abrir el archivo:", e)
            
button=Button(root, text="Open", command=OpenFile) 
button.grid()
button=Button(root, text="Save", command=saveas) 
button.grid()

def FontHelvetica():

    global text

    text.config(font="Helvetica")
def FontCourier():

    global text

    text.config(font="Courier")

font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()

font.menu.add_checkbutton(label="Courier", variable=Courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,command=FontHelvetica) 

# Función para ejecutar Markdown en el canvas
def execute_markdown():
    global text, canvas
    markdown_text = text.get("1.0", "end-1c")
    html_text = md.markdown(markdown_text)
    canvas.delete("all")  # Limpiar cualquier contenido previo
    canvas.create_text(200, 150, text=html_text, font=("Arial", 12), justify="center")
    return html_text  # Devuelve el texto en formato HTML

# Botón para ejecutar Markdown y mostrar el render en HTML
execute_button = Button(root, text="Execute Markdown", command=execute_markdown)
execute_button.grid(row=2, column=1, sticky="e")

def complete_text(text):
    html = md.markdown(text,output_format="html")
    template = f'''
    <!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My File</title></head><body>{html}</body></html>
    '''
    return template

# Función para guardar el HTML renderizado
def Save_html():
    global text, canvas
    html_text = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    t = complete_text(html_text)
    file1.write(t)
    file1.close()

# Botón para guardar el HTML renderizado
html_button = Button(root, text="Save Rendered HTML", command=Save_html)
html_button.grid(row=2, column=2, sticky="e")

root.mainloop()
