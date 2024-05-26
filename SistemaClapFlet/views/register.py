from flet import *
from flet_route import Params, Basket

import logica

#EL ESTATUS 1 ES HABILITADO
#EL ESTATUS 2 ES INHABILITADO

class register:
    def __init__(self):
        self.route = "/"
    
        #CONSULTAS
        self.llenarPreguntas = "SELECT pregunta FROM preguntas"
        #self.llenarUbicaciones = "SELECT ubicacion FROM ubicaciones"

    def view(self, page:Page, params:Params, basket:Basket):

        page.title = "CLAP"
        page.window_resizable = False
        page.window_maximizable = False

        #WIDGET
        self.usuario = TextField(label="Usuario", hint_text="Minimo 5 cacteres", max_length=10, border_color="#820000", border_radius=20, prefix_icon=icons.PERSON, width=280, height=60, on_change=lambda _: [self.quitarError(page, self.usuario), logica.validarEspacio(self.usuario, page)])
        self.contrasena = TextField(label="Contrasena", hint_text="Minimo 6 caracteres", max_length=12, border_color="#820000", border_radius=20, prefix_icon=icons.LOCK, width=280, height=60, on_change=lambda _: [self.quitarError(page, self.contrasena), logica.validarEspacio(self.contrasena, page)])
        self.confirmarContrasena = TextField(hint_text="Confirmar Contrasena", border_color="#820000", border_radius=20, prefix_icon=icons.LOCK, width=280, height=60, on_change=lambda _: [self.quitarError(page, self.confirmarContrasena), logica.validarEspacio(self.confirmarContrasena, page)])
        self.nombre = TextField(label="Nombre", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_color="#820000", border_radius=20, width=140, height=60, on_change=lambda _: [self.quitarError(page, self.nombre), logica.validarNombres(self.nombre, page)])
        self.apellido = TextField(label="Apellido", hint_text="Minimo 4 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_color="#820000", border_radius=20, width=140, height=60, on_change=lambda _: [self.quitarError(page, self.apellido), logica.validarNombres(self.apellido, page)])
        
        self.tipoCedula = Dropdown(label="Tipo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.tipoCedula), options=[
                dropdown.Option("V"), dropdown.Option("E")])
        self.tipoCedula.value = "V"
        self.cedula = TextField(label="Cedula", hint_text="Minimo 7 caracteres", border_color="#820000", border_radius=20, width=180, height=60, max_length=8, on_change=lambda _: [self.quitarError(page, self.cedula), logica.validarNumeros(self.cedula, page)])
        
        self.codigoTelefono = Dropdown(hint_text="Codigo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.codigoTelefono), options=[
                dropdown.Option("0412"), dropdown.Option("0414"), dropdown.Option("0416"), dropdown.Option("0424"), dropdown.Option("0238")])
        self.numeroTelefono = TextField(label="N telefono", hint_text="0000000", border_color="#820000", border_radius=20, width=180, height=60, max_length=7, on_change=lambda _: [self.quitarError(page, self.numeroTelefono), logica.validarNumeros(self.numeroTelefono, page)])
        self.correo = TextField(label="Direccion", hint_text="ej: clapcamoruco", border_color="#820000", border_radius=20, width=180, height=60, on_change=lambda _: [self.quitarError(page, self.correo), logica.validarCorreo(self.correo, page)])
        self.tipoCorreo = Dropdown(hint_text="Correo", color="black",border_color="#820000", border_radius=20, width=120, height=60, on_change=lambda _: self.quitarError(page, self.tipoCorreo), options=[
                dropdown.Option("@gmail.com"), dropdown.Option("@hotmail.com"), dropdown.Option("@outlook.com")])

        self.ubicacion = TextField(label="Ingresa tu ubicacion", hint_text="Ej : Camoruco v12", max_length=30, border_color="#820000", border_radius=20, capitalization=TextCapitalization.SENTENCES, width=280, height=60, on_change=lambda _: [self.quitarError(page, self.ubicacion), logica.validarAlfanumeros(self.ubicacion ,page)])
        #self.ubicacion = Dropdown(hint_text="Elegir Ubicacion", color="black",border_color="#820000", border_radius=20, width=280, height=60, on_change=lambda _: [self.quitarError(page, self.ubicacion), self.cargarVeredasCalle(page)])
        #self.veredaCalle = Dropdown(hint_text="Elegir Vereda/Calle", color="black",border_color="#820000", border_radius=20, width=280, height=60, visible=False, on_change=lambda _: self.quitarError(page, self.veredaCalle))
        self.pregunta = Dropdown(hint_text="Elegir Pregunta de Seguridad", color="black",border_color="#820000", border_radius=20, width=280, height=60, on_change=lambda _: self.quitarError(page, self.pregunta))
        self.respuesta = TextField(label="Respuesta", hint_text="Minimo 3 caracteres", max_length=20, capitalization=TextCapitalization.SENTENCES, border_color="#820000", border_radius=20, width=280, height=60, on_change=lambda _: [self.quitarError(page, self.respuesta), logica.validarNombres(self.respuesta, page)])
        self.nivelUser = Dropdown(hint_text="Cargo", color="black",border_color="#820000", border_radius=20, width=280, height=60, on_change=lambda _: self.quitarError(page, self.nivelUser), options=[
                dropdown.Option("Lider de Calle"), dropdown.Option("Lider Politico")])

        #LLENAR COMBO DE PREGUNTAS
        self.resultadoPreguntas = logica.consulta(self.llenarPreguntas)
        for guardarPreguntas in self.resultadoPreguntas:
            self.pregunta.options.append(dropdown.Option(guardarPreguntas[0]))

        #LLENAR COMBO DE UBICACION
        #self.resultadoUbicacion = logica.consulta(self.llenarUbicaciones)
        #for guardarUbicaciones in self.resultadoUbicacion:
            #self.ubicacion.options.append(dropdown.Option(guardarUbicaciones[0]))


        

        #CONTENEDORES
        self.contenedorLider = Container(
            height=725,
            width=500,
            border_radius=50,
            bgcolor="#820000",
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
                                Text("Datos Personales", style=TextThemeStyle.TITLE_LARGE),
                                Container(
                                    height=350,
                                    content=Column(
                                        spacing=20,
                                        height=350,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        width=480,
                                        scroll=ScrollMode.ALWAYS,
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    self.nombre,
                                                    self.apellido,
                                                ]
                                            ),
                                            Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                spacing=1,
                                                controls=[
                                                    self.tipoCedula,
                                                    self.cedula,
                                                ]
                                            ),
                                            self.nivelUser,
                                            #self.ubicacion,
                                            #self.veredaCalle,
                                            self.ubicacion,
                                            Text("Numero de telefono"),
                                            Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                spacing=1,
                                                controls=[
                                                    self.codigoTelefono,
                                                    self.numeroTelefono,
                                                ]
                                            ),
                                            Text("Correo electronico"),
                                            Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                spacing=1,
                                                controls=[
                                                    self.correo,
                                                    self.tipoCorreo,
                                                ]
                                            ),
                                        ]
                                    )    
                                ),
                                ElevatedButton("Siguiente", width=300, bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.camposVaciosPart1(page, self.contenedorLider, self.contenedorUsuario)),
                                ElevatedButton("Salir", bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.volverLogin(page))
                            ]
                        )
                    )
                ]
            )
        )

        self.contenedorUsuario = Container(
            height=725,
            width=500,
            border_radius=50,
            bgcolor="#820000",
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
                                Text("Usuario y Contraseña", style=TextThemeStyle.TITLE_LARGE),
                                self.usuario,
                                self.contrasena,
                                self.confirmarContrasena,
                                ElevatedButton("Siguiente", width=300, bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.camposVaciosPart2(page, self.contenedorUsuario, self.contenedorPregunta)),
                                ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.animar(self.contenedorUsuario, self.contenedorLider, page))
                                
                            ]
                        )
                    )
                ]
            )
        )

        self.contenedorPregunta = Container(
            height=725,
            width=500,
            border_radius=50,
            bgcolor="#820000",
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
                                Text("Pregunta de Seguridad", style=TextThemeStyle.TITLE_LARGE),
                                self.pregunta,
                                self.respuesta,
                                ElevatedButton("Siguiente", width=300, bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.camposVaciosPart3(page)),
                                ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _: self.animar(self.contenedorPregunta, self.contenedorUsuario, page))
                                
                            ]
                        )
                    )
                ]
            )
        )

        self.formulario = AnimatedSwitcher(
            self.contenedorLider,
            expand=True, 
            transition=AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=AnimationCurve.BOUNCE_OUT,
            switch_out_curve=AnimationCurve.BOUNCE_IN
        )

        return View(
            "/register",
            horizontal_alignment="center",
            vertical_alignment="center",
            bgcolor="transparent",
            padding=0,
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

    #def cargarVeredasCalle(self, pagee):
    #    pagee = pagee

    #    llenarVeredaCalle = "SELECT callesVeredas.direccion FROM callesVeredas JOIN ubicaciones ON ubicaciones_id = ubicaciones.id WHERE ubicaciones.ubicacion = ?"

    #    self.veredaCalle.visible = True
    #    self.veredaCalle.options.clear()

    #    resultadoVeredaCalle = logica.consulta(llenarVeredaCalle, [self.ubicacion.value])

    #    for guardarVeredaCalle in resultadoVeredaCalle:
    #        self.veredaCalle.options.append(dropdown.Option(guardarVeredaCalle[0]))

    #       pagee.update()


    def registrarUsuario(self, pageee, alert):
        pageee = pageee
        alert = alert

        nivelUsuario = 2
        arregloCedula = f"{self.tipoCedula.value}-{self.cedula.value}"
        arregloCorreo = f"{self.correo.value}{self.tipoCorreo.value}"
        arregloTelefono = f"{self.codigoTelefono.value}-{self.numeroTelefono.value}"
        
        #OBTENER ID PREGUNTA
        idPregunta = logica.consulta("SELECT id FROM preguntas WHERE pregunta = ?", [self.pregunta.value])

        #GUARDAR LA RESPUESTA
        logica.consulta("INSERT INTO respuestas VALUES (NULL, ?, ?)", [self.respuesta.value, idPregunta[0][0]])

        #OBTENER ID RESPUESTA
        idRespuesta = logica.consulta("SELECT respuestas.id FROM respuestas JOIN preguntas ON preguntas_id = preguntas.id WHERE preguntas.id = ? AND respuestas.respuesta = ?", [idPregunta[0][0], self.respuesta.value])

        #OBTENER ID CALLESVEREREDAS COMPLETO
        #idUbicacion = logica.consulta("SELECT callesVeredas.id FROM callesVeredas JOIN ubicaciones ON ubicaciones_id = ubicaciones.id WHERE ubicaciones.ubicacion = ? AND callesVeredas.direccion = ?", [self.ubicacion.value, self.veredaCalle.value])

        #GUARDAR DATOS DEL LIDER
        logica.consulta("INSERT INTO lideres VALUES (NULL, ?, ?, ?, ?, ?, ?)", [self.nombre.value, self.apellido.value, arregloCedula, arregloTelefono, arregloCorreo, self.ubicacion.value])

        #OBTENER ID LIDER
        idLider = logica.consulta("SELECT id FROM lideres WHERE cedula = ?", [arregloCedula])

        #SACAR DATO NIVEL USUARIO
        if self.nivelUser.value == "Lider Politico":
            nivelUsuario = 1

        #INSERTAR DATOS USUARIO
        logica.consulta("INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?, ?, 1)", [self.usuario.value, self.contrasena.value, idRespuesta[0][0], idLider[0][0], nivelUsuario])
        
        logica.enrutamiento(pageee, self.route)

        pageee.dialog = alert
        alert.open = True
        pageee.update()

    def camposVaciosPart1(self, pagee, contenedor11, contenedor22):
        pagee = pagee
        contenedor11 = contenedor11
        contenedor22 = contenedor22

        arregloCedula = f"{self.tipoCedula.value}-{self.cedula.value}"
        arregloCorreo = f"{self.correo.value}{self.tipoCorreo.value}"
        arregloTelefono = f"{self.codigoTelefono.value}-{self.numeroTelefono.value}"

        if (self.nombre.value == "") or (self.apellido.value == "") or (self.cedula.value == "") or (self.numeroTelefono.value == "") or (self.correo.value == "") or (self.ubicacion.value == "") or (self.nivelUser.value == None) or (self.tipoCorreo.value == None) or (self.codigoTelefono.value == None) or (len(self.nombre.value) in range(1, 3)) or (len(self.apellido.value) in range(1, 4)) or (len(self.cedula.value) in range(1, 7)) or (len(self.numeroTelefono.value) in range(1, 7)) or (len(self.ubicacion.value) in range(1, 3)):
            if self.nombre.value == "":
                self.nombre.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()
            
            if self.apellido.value == "":
                self.apellido.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.cedula.value == "":
                self.cedula.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.numeroTelefono.value == "":
                self.numeroTelefono.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.correo.value == "":
                self.correo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.ubicacion.value == "":
                self.ubicacion.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.nivelUser.value == None:
                self.nivelUser.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.tipoCorreo.value == None:
                self.tipoCorreo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.codigoTelefono.value == None:
                self.codigoTelefono.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if len(self.nombre.value) in range(1, 3):
                self.nombre.error_text = "Minimo de caracteres 3"
                pagee.update()

            if len(self.apellido.value) in range(1, 4):
                self.apellido.error_text = "Minimo de caracteres 4"
                pagee.update()
            
            if len(self.cedula.value) in range(1, 7):
                self.cedula.error_text = "Minimo de caracteres 7"
                pagee.update()
            
            if len(self.numeroTelefono.value) in range(1, 7):
                self.numeroTelefono.error_text = "Numero de telefono no valido"
                pagee.update()

            if len(self.ubicacion.value) in range(1, 3):
                self.ubicacion.error_text = "Minimo de caracteres 3"
                pagee.update()

        elif logica.consulta("SELECT id FROM lideres WHERE ubicacion =?", [self.ubicacion.value]):
            pagee.snack_bar = SnackBar(content=Text("Esta ubicacion ya esta en uso"))
            pagee.snack_bar.open = True
            pagee.update()

        elif logica.consulta("SELECT id FROM lideres WHERE cedula =?", [arregloCedula]):
            pagee.snack_bar = SnackBar(content=Text("Esta cedula ya esta ligada a un usuario"))
            pagee.snack_bar.open = True
            pagee.update()

        elif logica.consulta("SELECT id FROM lideres WHERE telefono =?", [arregloTelefono]):
            pagee.snack_bar = SnackBar(content=Text("Este numero de telefono ya esta asignado a un usuario"))
            pagee.snack_bar.open = True
            pagee.update()

        elif logica.consulta("SELECT id FROM lideres WHERE correo =?", [arregloCorreo]):
            pagee.snack_bar = SnackBar(content=Text("Este correo ya esta en uso"))
            pagee.snack_bar.open = True
            pagee.update()

        else:
            self.animar(contenedor11, contenedor22, pagee)
            

    def camposVaciosPart2(self, pagee, contenedor11, contenedor22):
        contenedor11 = contenedor11
        contenedor22 = contenedor22
        pagee = pagee

        queryy = "SELECT id FROM usuarios WHERE usuario =?"

        if (self.usuario.value == "") or (self.contrasena.value == "") or (self.confirmarContrasena.value == "") or (len(self.usuario.value) in range(1, 5)) or (len(self.contrasena.value) in range(1, 6)):

            if self.usuario.value == "":
                self.usuario.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()
            
            if self.contrasena.value == "":
                self.contrasena.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.confirmarContrasena.value == "":
                self.confirmarContrasena.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()
            
            if len(self.usuario.value) in range(1, 5):
                self.usuario.error_text = "Minimo de caracteres 5"
                pagee.update()

            if len(self.contrasena.value) in range(1, 6):
                self.contrasena.error_text = "Minimo de caracteres 6"
                pagee.update()
        
        elif logica.consulta(queryy, [self.usuario.value]):
            pagee.snack_bar = SnackBar(content=Text("Nombre de Usuario ya existente"))
            pagee.snack_bar.open = True
            pagee.update()

        elif self.contrasena.value == self.confirmarContrasena.value:
            self.animar(contenedor11, contenedor22, pagee)

        else:    
            pagee.snack_bar = SnackBar(content=Text("La contraseña no coinciden"))
            pagee.snack_bar.open = True
            pagee.update()

    def camposVaciosPart3(self, pagee):
        pagee = pagee

        self.textGuardar = AlertDialog(title=Text("Usuario registrado correctamente"))

        if (self.pregunta.value == None) or (self.respuesta.value == "") or (len(self.respuesta.value) in range (1, 3)):          
            if self.respuesta.value == "":
                self.respuesta.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.pregunta.value == None:
                self.pregunta.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if len(self.respuesta.value) in range (1, 3):
                self.respuesta.error_text = "Minimo de caracteres 3"
                pagee.update()

            else:
                return

        else:

            self.registrarUsuario(pagee, self.textGuardar)

    def quitarError(self, pagee, textfield):
        pagee = pagee
        textfield = textfield

        textfield.error_text = None
        pagee.update()

    def volverLogin(self, pagee):
        pagee = pagee

        pagee.go(self.route)