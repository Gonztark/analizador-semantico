import tkinter
from tkinter import filedialog
import customtkinter
from lexico import analizar_lexico, reset_lines
from sintactico import analizar_sintactico
from semantico import analizar_semantica

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Analizador Léxico y Sintáctico")
        self.geometry("1300x650") 

        # Cuadro de texto para la entrada del usuario
        self.texto_entrada = customtkinter.CTkTextbox(self, width=380, height=300)
        self.texto_entrada.grid(row=0, column=0, padx=20, pady=20)
        self.texto_entrada.insert("1.0", "Introduce el código aquí o carga un archivo")
        self.texto_entrada.bind("<FocusIn>", self.on_focus_in)

        # Mostrar resultado léxico
        self.texto_resultado_lexico = customtkinter.CTkTextbox(self, width=380, height=250, state="disabled")
        self.texto_resultado_lexico.grid(row=0, column=1, padx=20, pady=(20,0))

        # Mostrar resultado sintáctico
        self.texto_resultado_sintactico = customtkinter.CTkTextbox(self, width=380, height=250, state="disabled")
        self.texto_resultado_sintactico.grid(row=1, column=1, padx=20, pady=(0,0))

        # Mostrar resultado semantico
        self.texto_resultado_semantico = customtkinter.CTkTextbox(self, width=380, height=250, state="disabled")
        self.texto_resultado_semantico.place(x=850, y=200)

        # botones
        self.boton_analizar_lexico = customtkinter.CTkButton(self, text="Analizar Léxico", command=self.analizar_lexico)
        self.boton_analizar_lexico.grid(row=2, column=1, pady=20, sticky="w")

        self.boton_analizar_sintactico = customtkinter.CTkButton(self, text="Analizar Sintáctico", command=self.analizar_sintactico)
        self.boton_analizar_sintactico.grid(row=2, column=1, pady=20, sticky="e")

        self.boton_analizar_semantico = customtkinter.CTkButton(self, text="Analizar Semántica", command=self.analizar_semantico)
        self.boton_analizar_semantico.place(x=980, y=480)

        self.boton_cargar = customtkinter.CTkButton(self, text="Cargar Archivo", command=self.cargar_archivo)
        self.boton_cargar.place(x=140, y=350)

    def on_focus_in(self, event):
        default_text = "Introduce el código aquí o carga un archivo"
        if self.texto_entrada.get("1.0", "end-1c") == default_text:
            self.texto_entrada.delete("1.0", "end")

    def analizar_lexico(self):
        texto_usuario = self.texto_entrada.get("1.0", "end-1c")
        resultado = analizar_lexico(texto_usuario)
        self.texto_resultado_lexico.configure(state="normal")
        self.texto_resultado_lexico.delete("1.0", "end")
        self.texto_resultado_lexico.insert("1.0", resultado)
        self.texto_resultado_lexico.configure(state="disabled")

    def analizar_sintactico(self):
        texto_usuario = self.texto_entrada.get("1.0", "end-1c")
        resultado = analizar_sintactico(texto_usuario)
        reset_lines()
        if not resultado.strip():
            resultado = "No hay errores de sintaxis."
        self.texto_resultado_sintactico.configure(state="normal")
        self.texto_resultado_sintactico.delete("1.0", "end")
        self.texto_resultado_sintactico.insert("1.0", resultado)
        self.texto_resultado_sintactico.configure(state="disabled")

    def analizar_semantico(self):
        texto_usuario = self.texto_entrada.get("1.0", "end-1c")
        resultado = analizar_semantica(texto_usuario)
        self.texto_resultado_semantico.configure(state="normal")
        self.texto_resultado_semantico.delete("1.0", "end")
        self.texto_resultado_semantico.insert("1.0", resultado)
        self.texto_resultado_semantico.configure(state="disabled")
        

    def cargar_archivo(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                self.texto_entrada.configure(state="normal")
                self.texto_entrada.delete("1.0", "end")
                self.texto_entrada.insert("1.0", contenido)
                self.texto_entrada.configure(state="normal")

if __name__ == "__main__":
    app = App()
    app.mainloop()
