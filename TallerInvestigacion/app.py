from fastapi import FastAPI
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@component
def App():
    input_value, set_input_value = use_state("")

    def handle_change(event):
        new_value = event['target']['value']
        set_input_value(new_value)

    def handle_click(event):
        print(input_value)

    return html.div(
        {"style": {"text-align": "left", "margin-top": "20px"}},
        html.style("""
            body {
                font-family: Arial, sans-serif; /* Cambia el tipo de letra */
            }
            .background {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image: url('/static/ya.jpg'); 
                background-size: cover; 
                z-index: -1; /* Asegura que el fondo esté detrás de los otros elementos */
                opacity: 0.9; /* Ajusta la opacidad del fondo */
            }
            h1 {
                text-align: center; /* Centra el texto dentro del h1 */
            }
            h1, h2, button {
                color: white; /* Cambia el color del texto a blanco */
            }
            input[type="text"] {
                width: 50%; 
                height: 50px;
                margin-bottom: 10px; /* Añade espacio debajo del input */
                border-radius: 10px; /* Redondear los bordes del input */
            }
            button {
                width: 50%; /* Hacer el botón del mismo tamaño que el input */
                display: block; /* Hacer que el botón ocupe toda la anchura disponible */
                background-color: darkblue; /* Cambiar el color de fondo del botón */
                height: 40px; /* Ajustar la altura del botón */
                border-radius: 10px; /* Redondea los bordes del botón */
                color: white; /* Cambia el color del texto del botón a blanco */
                border: none; /* Quita el borde del botón */
                margin-bottom: 30px; /* Añade espacio debajo del botón */
            }
            p {
                width: 50%; /* Establece el mismo ancho que el input */
                border: 1px solid black; /* Agrega un borde negro */
                border-radius: 10px; /* Redondea los bordes del párrafo */
                padding: 10px; /* Añade un espacio alrededor del contenido del párrafo */
                box-sizing: border-box; /* Incluye el padding en el tamaño total del párrafo */
                background-color: white;
                margin-bottom: 10px; /* Añade espacio debajo del párrafo */
            }
            h2 {
                width: 50%; /* Establece el mismo ancho que el input */
                text-align: left; /* Alinea el texto a la izquierda */
                margin-bottom: 20px; /* Añade espacio debajo del h2 */
            }
        """),
        html.div({"class": "background"}),  # Agrega un div para el fondo
        html.h1("Mi aplicación"),  # Estilo centrado
        html.h2("Instrucción:"),
        html.input(
            {"type": "text",
             "placeholder": "Escribe aquí...",
             "value": input_value,
             "onChange": lambda event: handle_change(event),
            }
        ),
        html.button(
            {"onClick": lambda event: handle_click(event)},
            "Mandar Instrucción"
        ),
        html.h2("Porcentaje de similitud con cada categoría:"),  # Agregar salida de texto
        
        html.p("Comida: " + input_value),
        html.p("Música: " + input_value),
        html.p("Dispositivos Inteligentes: " + input_value),
        html.p("Compras: " + input_value),
        html.p("Recordatorios: " + input_value),
        
        html.h2("Resultado:"),
        html.p("La instrucción tiene mayos similitud semántica con la categoria: " + input_value),
    )

configure(app, App)
