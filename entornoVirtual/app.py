import sys
sys.path.append(r'C:/Users/Link_/Desktop/LA_II/Proyecto/COELNETSSO/entornoVirtual/OpenAI')
import time
from fastapi import FastAPI
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from fastapi.staticfiles import StaticFiles
from Clasificacion_OpenAI import clasificacionTexto
import speech_recognition as sr
import threading


app = FastAPI()
app.mount("/static", StaticFiles(directory="entornoVirtual/static"), name="static")

@component
def App():
    
    input_value, set_input_value = use_state("")
    title_text, set_title_text = use_state("")
    similaridades, set_similaridades = use_state([0,0,0,0,0])
    categoria, set_categoria = use_state("Ninguno")

    def recognize_speech():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Di algo...")
            audio = r.record(source, duration = 7)

            try:
                text = r.recognize_google(audio, language='es-ES')
                print("Dijiste: {}".format(text))
                return text
            except sr.UnknownValueError:
                print("No se pudo entender el audio")
                return None
            except sr.RequestError as e:
                print("No se pudo completar la solicitud; {0}".format(e))
                return None
            
    def send_instruction():    
        set_title_text("Procesando datos, espere un momento...")

    def handle_change(event):
        new_value = event['target']['value']
        set_input_value(new_value)

    def handle_click(event):
        send_instruction()
        print(input_value)
        vector=clasificacionTexto(input_value)
        print(vector)
        set_similaridades(vector)
        max_similitud = vector.index(max(vector))
        cat = "No"
        if max_similitud == 0:
            cat = "Comida"
        elif max_similitud == 1:
            cat = "Musica"
        elif max_similitud == 2:
            cat = "Dispositivos Inteligentes"
        elif max_similitud == 3:
            cat = "Compras"
        elif max_similitud == 4:
            cat = "Recordatorios/Alarmas"
        set_categoria(cat)
        set_title_text("")

    def handle_click2(event):
        set_title_text("Habla ahora...")

        thread = threading.Thread(target=recognize_speech_thread)
        thread.start()
        
    def recognize_speech_thread():
        text = recognize_speech()
        if text:
            set_input_value(text)
        set_title_text("")

    return html.div(
        {"style": {"text-align": "left", "margin-top": "20px"}},
        html.style("""
            body {
                font-family: Arial, sans-serif; 
            }
            .background {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image: url('/static/ya.jpg'); 
                background-size: cover; 
                z-index: -1; 
                opacity: 0.9; 
            }
            h1, h2, button, label {
                color: white; 
            }
            input[type="text"] {
                width: 50%; 
                height: 50px;
                margin-bottom: 10px; 
                border-radius: 10px; 
            }
            button {
                width: 50%; 
                display: block; 
                background-color: darkblue; 
                height: 40px; 
                border-radius: 10px; 
                color: white; 
                border: none; 
                margin-bottom: 10px; 
            }
            .start-recording-button {
                margin-bottom: 10px; 
            }
            .send-instruction-button {
                margin-bottom: 10px; 
            }
            p {
                width: 50%; 
                border: 1px solid black;
                border-radius: 10px; 
                padding: 10px; 
                box-sizing: border-box; 
                background-color: white;
                margin-bottom: 10px; 
            }
            h2 {
                width: 50%; 
                text-align: left; 
                margin-bottom: 20px; 
            }
            .hidden {{
                display: none;
            }}
        """),
        html.div({"class": "background"}),  # Agrega un div para el fondo
        html.h1({"style": {"text-align": "center"}}, "AI Semantic Classifier"),
        html.h2({"style": {"text-align": "center"}}, title_text),  
        html.h2("Instrucción:"),
        html.input(
            {"type": "text",
             "placeholder": "Escribe aquí...",
             "value": input_value,
             "onChange": lambda event: handle_change(event),
            }
        ),
        html.button(
            {"onClick": lambda event: handle_click(event), "class": "send-instruction-button"},
            "Mandar Instrucción"
        ),
        html.button(
            {"onClick": lambda event: handle_click2(event), "class": "start-recording-button"},
            "Instrucción por voz"
        ),
        html.h2("Porcentaje de similitud con cada categoría:"),  # Agregar salida de texto
        
        html.p("Comida: " + str(round(similaridades[0],3))),
        html.p("Música: " + str(round(similaridades[1],3)) ),
        html.p("Dispositivos Inteligentes: " + str(round(similaridades[2],3))),
        html.p("Compras: " + str(round(similaridades[3],3))),
        html.p("Recordatorios: " + str(round(similaridades[4],3))),
        
        html.h2("Resultado:"),
        html.p("La instrucción tiene mayor similitud semántica con la categoria: " + categoria),
    )

configure(app, App)
