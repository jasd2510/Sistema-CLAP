from flet import *
from flet_route import Params, Basket

import logica

class recuperar:
    def __init__(self):
        #RUTA
        self.route = "/"

    def view(self, page:Page, params:Params, basket:Basket):
        #TEXTFLIEDS
        self.tipoCedula = Dropdown(label="Tipo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.tipoCedula), options=[
                dropdown.Option("V"), dropdown.Option("E")])
        self.tipoCedula.value = "V"
        self.cedula = TextField(label="Cedula", hint_text="Minimo 7 caracteres", border_color="#820000", border_radius=20, width=180, height=60, max_length=8, on_change=lambda _: [self.quitarError(page, self.cedula), logica.validarNumeros(self.cedula, page)])
        self.pregunta = Text("", style=TextThemeStyle.TITLE_MEDIUM)
        self.respuesta = TextField(hint_text="Escriba su respuesta", capitalization=TextCapitalization.SENTENCES, label="Respuesta", border_radius=30, border_color="#820000", width=280, height=60, on_change=lambda _:[self.quitarError(page, self.respuesta), logica.validarNombres(self.respuesta, page)])
        self.contrasena = TextField(hint_text="Minimo 6 caracteres", label="Contraseña", border_radius=30, border_color="#820000", prefix_icon=icons.LOCK, width=280, height=60, max_length=12, on_change=lambda _:[self.quitarError(page, self.contrasena), logica.validarEspacio(self.contrasena, page)])
        self.confimarContrasena = TextField(hint_text="Confirmar contraseña", label="Confirmar", border_radius=30, border_color="#820000", prefix_icon=icons.LOCK, width=280, height=60, on_change=lambda _:[self.quitarError(page, self.confimarContrasena), logica.validarEspacio(self.confimarContrasena, page)])

        page.title = "CLAP"
        page.window_resizable = False
        page.window_maximizable = False
        #CONTENEDORES
        self.containerCedula = Container(
            height=725,
            width=500,
            content=Column(
                controls=[
                    Container(
                        height=150,
                        alignment=alignment.center,
                        content=Row(
                            alignment=MainAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="blue"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                Container(width=70, height=8, bgcolor="white"),
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="white"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                Container(width=80, height=8, bgcolor="white"),
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="white"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                            ]
                        )
                    ),

                    Container(
                        bgcolor="white",
                        height=550,
                        width=500,
                        border_radius=border_radius.only(topLeft=50),
                        padding=padding.all(30),
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.SPACE_AROUND,
                            spacing=20,
                            controls=[
                                Text("Identificación", style=TextThemeStyle.TITLE_LARGE),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=1,
                                    controls=[
                                        self.tipoCedula,
                                        self.cedula,
                                    ]
                                ),
                                ElevatedButton("Siguiente", width=300, bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.validarCedula(page, self.containerCedula, self.containerRespuesta)),
                                ElevatedButton("Atras", bgcolor="#cb3234", color="#ffffff", on_click=lambda _: logica.enrutamiento(page, self.route))
                            ]
                        )
                    )
                ]
            )
        )

        self.containerRespuesta = Container(
            height=725,
            width=500,
            content=Column(
                controls=[
                    Container(
                        height=150,
                        alignment=alignment.center,
                        content=Row(
                            alignment=MainAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="white"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                Container(width=70, height=8, bgcolor="white"),
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="blue"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                Container(width=80, height=8, bgcolor="white"),
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="white"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                            ]
                        )
                    ),

                    Container(
                        bgcolor="white",
                        height=550,
                        width=500,
                        border_radius=border_radius.only(topLeft=50),
                        padding=padding.all(30),
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.SPACE_AROUND,
                            spacing=20,
                            controls=[
                                Text("Pregunta de seguridad", style=TextThemeStyle.TITLE_LARGE),
                                self.pregunta,
                                self.respuesta,
                                ElevatedButton("Siguiente", width=300, bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.validarRespuesta(page, self.cedula, self.containerRespuesta, self.containerContrasena)),
                                ElevatedButton("Atras", bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.animar(self.containerRespuesta, self.containerCedula, page))
                            ]
                        )
                    )
                ]
            )
        )

        self.containerContrasena = Container(
            height=725,
            width=500,
            content=Column(
                controls=[
                    Container(
                        height=150,
                        alignment=alignment.center,
                        content=Row(
                            alignment=MainAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="white"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                Container(width=70, height=8, bgcolor="white"),
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="white"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                Container(width=80, height=8, bgcolor="white"),
                                Stack(
                                    controls=[
                                        Container(
                                            width=50, 
                                            height=50, 
                                            bgcolor="white", 
                                            border_radius=border_radius.all(50),
                                            content=Column(
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius=border_radius.all(50),
                                                        bgcolor="blue"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                            ]
                        )
                    ),

                    Container(
                        bgcolor="white",
                        height=550,
                        width=500,
                        border_radius=border_radius.only(topLeft=50),
                        padding=padding.all(30),
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.SPACE_AROUND,
                            spacing=20,
                            controls=[
                                Text("Asignar Nueva Contraseña", style=TextThemeStyle.TITLE_LARGE),
                                self.contrasena,
                                self.confimarContrasena,
                                ElevatedButton("Guardar", width=300, bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.validarContrasena(page, self.contrasena, self.confimarContrasena, self.cedula)),
                                ElevatedButton("Atras", bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.animar(self.containerContrasena, self.containerRespuesta, page))
                            ]
                        )
                    )
                ]
            )
        )

        self.formulario = AnimatedSwitcher(
            self.containerCedula,
            expand=True, 
            transition=AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=AnimationCurve.BOUNCE_OUT,
            switch_out_curve=AnimationCurve.BOUNCE_IN
        )


        return View(
            "/recuperar",
            horizontal_alignment="center",
            vertical_alignment="center",
            padding=0,
            bgcolor="#820000",
            controls=[
                self.formulario
            ]
        )

    def animar(self, contenedor1, contenedor2, pageee):
        contenedor1 = contenedor1
        contenedor2 = contenedor2
        pageee = pageee

        self.formulario.content = contenedor2 if self.formulario.content == contenedor1 else contenedor1
        pageee.update()

    def salir(self, pagee):
        pagee = pagee

        logica.enrutamiento(pagee, self.route)

        self.cedula.value = ""
        self.pregunta.value = ""
        self.respuesta.value = ""
        self.contrasena.value = ""
        self.confimarContrasena.value = ""
        self.cedula.error_text = None

    def quitarError(self, pagee, textfield):
        pagee = pagee
        textfield = textfield

        textfield.error_text = None
        pagee.update()

    def validarContrasena(self, pagee, contrasena, confirmar, cedula):
        pagee = pagee
        contrasena = contrasena
        confirmar = confirmar
        cedula = cedula

        textGuardar = AlertDialog(title=Text("Contraseña cambiada correctamente"))

        arregloCedulaaa = f"{self.tipoCedula.value}-{self.cedula.value}"

        if (contrasena.value == "") or (confirmar.value == "") or (len(contrasena.value) in range (1,6)):
            if contrasena.value == "":
                self.contrasena.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if confirmar.value == "":
                self.confimarContrasena.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if len(contrasena.value) in range (1,6):
                self.contrasena.error_text = "Minimo de caracteres 6"
                pagee.update()
            
            else:
                return

        elif contrasena.value == confirmar.value:
            idUsuario = logica.consulta("SELECT usuarios.id FROM usuarios JOIN lideres ON lideres_id = lideres.id WHERE lideres.cedula = ?", [arregloCedulaaa])
            
            logica.consulta("UPDATE usuarios SET contrasena =? WHERE usuarios.id =?", [contrasena.value, idUsuario[0][0]])
            logica.enrutamiento(pagee, self.route)

            pagee.dialog = textGuardar
            textGuardar.open = True
            pagee.update()

            self.cedula.value = ""
            self.pregunta.value = ""
            self.respuesta.value = ""
            self.contrasena.value = ""
            self.confimarContrasena.value = ""
            self.cedula.error_text = None

        else:
            pagee.snack_bar = SnackBar(content=Text("Las contraseñas no coinciden"))
            pagee.snack_bar.open = True
            pagee.update()

    def validarRespuesta(self, pagee, ci, contenedor11, contenedor22):
        pagee = pagee
        ci = ci
        contenedor11 = contenedor11
        contenedor22 = contenedor22

        arregloCedulaa = f"{self.tipoCedula.value}-{self.cedula.value}"

        queryConsulta = "SELECT respuestas.respuesta FROM usuarios JOIN lideres ON lideres_id = lideres.id JOIN respuestas ON respuesta_id = respuestas.id JOIN preguntas ON preguntas_id = preguntas.id WHERE lideres.cedula = ?"
        resultadoRespuesta = logica.consulta(queryConsulta, [arregloCedulaa])

        if self.respuesta.value == "":
            self.respuesta.error_text = "Campo vacio, por favor rellenelo para continuar"
            pagee.update()

        elif resultadoRespuesta[0][0] == self.respuesta.value:
            self.animar(contenedor11, contenedor22, pagee)

        else:
            pagee.snack_bar = SnackBar(content=Text("Su respuesta es incorrecta"))
            pagee.snack_bar.open = True
            pagee.update()

    def mostrarPregunta(self, page, resultadoo, ci):
        page = page
        resultadoo = resultadoo
        ci = ci

        self.pregunta.value = f"{resultadoo[0][0]}"

        page.update()

    def validarCedula(self, pagee, contenedor11, contenedor22):
        pagee = pagee
        contenedor11 = contenedor11
        contenedor22 = contenedor22
        arregloCedula = f"{self.tipoCedula.value}-{self.cedula.value}"
        
        queryConsulta = "SELECT preguntas.pregunta FROM usuarios JOIN lideres ON lideres_id = lideres.id JOIN respuestas ON respuesta_id = respuestas.id JOIN preguntas ON preguntas_id = preguntas.id WHERE lideres.cedula = ?"
        resultado = logica.consulta(queryConsulta, [arregloCedula])

        if (self.cedula.value == "") or (len(self.cedula.value) in range (1,7)):
            if self.cedula.value == "":
                self.cedula.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()
            
            if len(cedula.value) in range (1,7):
                self.cedula.error_text = "Minimo de caracteres 7"
                pagee.update()

        elif logica.consulta(queryConsulta, [arregloCedula]):
            self.mostrarPregunta(pagee, resultado, arregloCedula)
            self.animar(contenedor11, contenedor22, pagee)

        else:
            pagee.snack_bar = SnackBar(content=Text("La cedula no coincide con ningun usuario registrado"))
            pagee.snack_bar.open = True
            pagee.update()