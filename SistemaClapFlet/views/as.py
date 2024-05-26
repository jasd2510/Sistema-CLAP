def view(self, page:Page, params:Params, basket:Basket):

        self.bitacoraLista = []

        self.iDLiderCalle = logica.datoUser[0][0]
        self.nombreLiderCalle = logica.datoUser[0][1]
        self.ApellidoLiderCalle = logica.datoUser[0][2]
        self.UbicacionLiderCalle = logica.datoUser[0][3]
        self.idUsuario = logica.datoUser[0][4]
        self.fechaEntradaUser = logica.datoUser[0][5]

        self.check = Checkbox(on_change=lambda _:self.estatusUsuario(page))

        self.entryEmpresa = TextField(label="Empresa", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryEmpresa), logica.validarNombres(self.entryEmpresa, page)])
        self.entryTamano = TextField(label="Tamaño", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryTamano), logica.validarNombres(self.entryTamano, page)])
        self.entryPico = TextField(label="Pico", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryPico), logica.validarNombres(self.entryPico, page)])

        self.entryComunidad = TextField(label="Comunidad", hint_text="Minimo 4 caracteres", max_length=30, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryComunidad), logica.validarNombres(self.entryComunidad, page)])
        self.entryVereda = TextField(label="Vereda\Calle", hint_text="", max_length=30, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryVereda), logica.validarNombres(self.entryVereda, page)])
        self.cantidadVerdas = TextField(label="Cantidad de Vereda\Calle", hint_text="", max_length=2, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.cantidadVerdas), logica.validarNumeros(self.entryComunidad, page)])
        self.cantidadVerdas.value = "1"

        page.title = "CLAP"
        page.window_maximizable = False
        page.window_resizable = False
        page.window_height = "800"
        page.window_width = "1000"
        page.window_center()

        self.titulo = Text("Lideres de Calle", style=TextThemeStyle.TITLE_LARGE, color="white")
        self.textoSlider = Text(f"{self.nombreLiderCalle}", weight=FontWeight.W_500, color="WHITE")

        #self.barraBusqueda = TextField(hint_text="Buscar Jefe de Familia", width=280, height=40)

        self.nombreLi = Text("")
        self.apellidoLi = Text("")
        self.cedulaLi = Text("")
        self.ubicacionLi = Text("")
        self.telefonoLi = Text("")
        self.correoLi = Text("")
        #self.nombreP = Text("")
        #self.apellidoP = Text("")
        #self.cedulaP = Text("")
        #self.ubicacionP = Text("")
        self.preguntaP = Text("")
        self.respuestaP = Text("")
        self.usuarioP = Text("")
        self.contrasenaP = Text("", visible=False)
        #self.telefonoP = Text("")
        #self.correoP = Text("")
        
        self.codigoTelefono = Dropdown(hint_text="Codigo", visible=False, color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.codigoTelefono), options=[
                dropdown.Option("0412"), dropdown.Option("0414"), dropdown.Option("0416"), dropdown.Option("0424"), dropdown.Option("0238")])
        self.numeroTelefono = TextField(label="N telefono", visible=False, hint_text="0000000", border_color="#820000", border_radius=20, width=180, height=60, max_length=7, on_change=lambda _: [self.quitarError(page, self.numeroTelefono), logica.validarNumeros(self.numeroTelefono, page)])
        self.correoCambiar = TextField(label="Direccion", visible=False, hint_text="ej: clapcamoruco", max_length=50, border_color="#820000", border_radius=20, width=180, height=60, on_change=lambda _: self.quitarError(page, self.correo))
        self.tipoCorreo = Dropdown(hint_text="Correo", visible=False, color="black",border_color="#820000", border_radius=20, width=120, height=60, on_change=lambda _: self.quitarError(page, self.tipoCorreo), options=[
                dropdown.Option("@gmail.com"), dropdown.Option("@hotmail.com"), dropdown.Option("@outlook.com")])


        self.nombre = Text("")
        self.apellido = Text("")
        self.cedula = Text("")
        self.ubicacion = Text("")
        self.pregunta = Text("")
        self.respuesta = Text("")
        self.usuario = Text("")
        self.contrasena = Text("", visible=False)
        self.telefono = Text("")
        self.correo = Text("")
        self.estatus = Text("")

        self.volverCargarTusDatos(page)

        self.btnCandado = IconButton(icon=icons.LOCK_OUTLINE, on_click=lambda _:self.revelarPass(page))
        self.btnCandadoP = IconButton(icon=icons.LOCK_OUTLINE, on_click=lambda _:self.revelarPassP(page))

        #self.btnLapizTelefono = IconButton(icon=icons.EDIT, on_click=lambda _:self.cambiarTelefono(page))
        #self.btnLapizCorreo = IconButton(icon=icons.EDIT, on_click=lambda _:self.cambiarCorreo(page))

        #self.btnCancelTelefono = IconButton(icon=icons.CANCEL, on_click=lambda _:self.cancelarTelefono(page), visible=False)
        #self.btnCancelCorreo = IconButton(icon=icons.CANCEL, on_click=lambda _:self.cancelarCorreo(page), visible=False)

        #self.btnActualizarTelefono = ElevatedButton("Actualizar", visible=False, on_click=lambda _: self.validarTelefono(page))
        #self.btnActualizarCorreo = ElevatedButton("Actualizar", visible=False, on_click=lambda _: self.validarCorreo(page))

        self.tablaSeleccionarHistorial = DataTable(
            bgcolor="#C5283D",
            columns=[
                #DataColumn(Text("id")),
                DataColumn(Text("Jornada", color="WHITE")),
                DataColumn(Text("Fecha", color="WHITE")),
            ],
            rows=[

            ]
        )

        self.tablaLlenarHistorial = DataTable(
            bgcolor="#C5283D",
            columns=[
                #DataColumn(Text("id")),
                DataColumn(Text("Ci", color="WHITE")),
                DataColumn(Text("Nombre", color="WHITE")),
                DataColumn(Text("Apellido", color="WHITE")),
                DataColumn(Text("Empresa", color="WHITE")),
                DataColumn(Text("Tamano", color="WHITE")),
                DataColumn(Text("Pico", color="WHITE")),
                DataColumn(Text("Agregado", color="WHITE"))
            ],
            rows=[

            ]
        )

        self.columnaCards = Row(
            wrap=True,
        )
        
        self.listaBitacora = ListView(width=400, height=550, spacing=20)

        self.volverGenerarCartas(page)

        #APP BAR
        self.appbar = Container(
            bgcolor="#C5283D",
            border_radius=border_radius.all(15),
            height=100,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(padding=padding.only(left=10) ,content=self.logo),
                    self.titulo,
                    PopupMenuButton(items=[PopupMenuItem(text="Cerrar seccion", on_click=lambda _: self.salir(page))])
                ]
            )
        )

        #SLIDER
        self.slider = Container(
            height=635,
            width=150,
            bgcolor="#C5283D",
            border_radius=border_radius.all(15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=10,
                height=630,
                width=150,
                expand=True,
                controls=[
                    Stack(
                        controls=[
                            Column(
                                height=630,
                                controls=[
                                    self.indicator
                                ]
                            ),

                            Column(
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    Container(
                                        padding=padding.only(top=25),
                                        content=Column(
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                            controls=[
                                                CircleAvatar(
                                                    content=Icon(icons.PEOPLE),
                                                    width=80,
                                                    height=80,
                                                ),
                                                Text("Bienvenido", weight=FontWeight.W_500, color="WHITE"),
                                                self.textoSlider,
                                            ]
                                        )
                                    ),

                                    Container(
                                        
                                        margin=margin.only(top=50),
                                        padding=padding.only(left=35),
                                        offset=Offset(x=None, y=None),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Lideres de Calle")],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.HOME),
                                                Text("Inicio")
                                            ]
                                        )
                                    ),

                                    Container(
                                        margin=margin.only(top=20),
                                        padding=padding.only(left=35),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorBombonas, self.contenedorBombonas, page), self.cambiar_pagina(6.8), self.cambiarTitulo(page, "Gestion de Bombonas")],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.EVENT_NOTE),
                                                Text("Bombonas")
                                            ]
                                        )
                                    ),

                                    Container(
                                        margin=margin.only(top=20),
                                        padding=padding.only(left=35),
                                        offset=Offset(x=None, y=None),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorPerfil, self.contenedorPerfil, page), self.cambiar_pagina(8.2), self.cambiarTitulo(page, "Tu Perfil"), self.regresarPassFalse(page)],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.PEOPLE),
                                                Text("Tu Perfil")
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            )
        )


        #CONTENEDORES PRINCIPALES
        self.contenedorInicio = Container(
            height=635,
            width=815,
            padding=15,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            border_radius=border_radius.all(15),
            alignment=alignment.center,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Row(
                        height=50,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            #self.barraBusqueda,
                            Text(""),
                            ElevatedButton("Actualizar Precios", bgcolor="Yellow", color="Black", on_click=lambda _: self.menuPrecios(page))
                        ]
                    ),
                    self.columnaCards
                ]    
            )
        )

        self.contenedorPerfil = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            padding=padding.only(top=10),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                spacing=20,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        bgcolor="white",
                        height=500,
                        width=800,
                        padding=padding.only(top=40),
                        border_radius=border_radius.all(40),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                Column(
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Nombre:"),
                                                self.nombreLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Nombre", on_click=lambda _: self.editNombreLi(page, self.nombreLi.value))
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Apellido:"),
                                                self.apellidoLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Apellido", on_click=lambda _: self.editApellidoLi(page, self.apellidoLi.value))
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Cedula:"),
                                                self.cedulaLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Cedula", on_click=lambda _: self.editCedulaLi(page, self.cedulaLi.value[0],self.cedulaLi.value[2:]))
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Telefono:"),
                                                self.telefonoLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Telefono", on_click=lambda _: self.editTelefonoLi(page, self.telefonoLi))
                                                #self.codigoTelefono,
                                                #self.numeroTelefono,
                                                #self.btnLapizTelefono,
                                                #self.btnCancelTelefono 
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Correo:"),
                                                self.correoLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Correo", on_click=lambda _: self.editCorreoLi(page, self.correoLi))
                                                #self.correoCambiar,
                                                #self.tipoCorreo,
                                                #self.btnLapizCorreo,
                                                #self.btnCancelCorreo
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Ubicacion:"),
                                                self.ubicacionLi,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Pregunta:"),
                                                self.preguntaP,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Respuesta:"),
                                                self.respuestaP,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Usuario:"),
                                                self.usuarioP,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Contraseña:"),
                                                self.contrasenaP,
                                                self.btnCandadoP
                                            ]
                                        ),
                                    ]
                                ),
                                Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Lideres de Calle"), self.regresarPassFalseP(page)]),
                                                ElevatedButton("Ver tu bitacora", on_click=lambda _: [self.animar(self.formularioBitacora, self.formularioBitacora, page), self.cambiarTitulo(page, "Historial de Inicios de sesion"), self.volverGenerarBitacora(page, self.cedulaLi)])
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.contenedorHistorial = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            padding=15,
            border=border.all(2, "#C5283D"),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        bgcolor="white",
                        height=550,
                        border_radius=border_radius.all(7),  
                        content=Column(
                            expand=True,
                            height=550,
                            scroll=ScrollMode.ALWAYS,
                            controls=[
                                self.tablaSeleccionarHistorial,
                            ]
                        )
                    ),

                    Row(
                        controls=[
                            ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Mi Comunidad")])
                        ]
                    ),
                ]
            )
        )

        self.formularioLiderCalle = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            padding=padding.only(top=10),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                spacing=20,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        bgcolor="white",
                        height=500,
                        width=350,
                        padding=padding.only(top=40),
                        border_radius=border_radius.all(40),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Column(
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Nombre:"),
                                                self.nombre,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Apellido:"),
                                                self.apellido,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Cedula:"),
                                                self.cedula,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Ubicacion:"),
                                                self.ubicacion,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Telefono:"),
                                                self.telefono,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Correo:"),
                                                self.correo,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Pregunta:"),
                                                self.pregunta,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Respuesta:"),
                                                self.respuesta,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Usuario:"),
                                                self.usuario,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Contraseña:"),
                                                self.contrasena,
                                                self.btnCandado
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Estatus:"),
                                                self.estatus,
                                                self.check
                                            ]
                                        ),
                                    ]
                                ),
                                Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiarTitulo(page, "Lideres de Calle"), self.regresarPassFalse(page)]),
                                                ElevatedButton("Ver Jornadas", bgcolor="Green", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorHistorial, self.contenedorHistorial, page), self.cambiarTitulo(page, "Administrador de jornadas"), self.volverGenerarArchivos(page)])
                                            ]
                                        ),
                                        ElevatedButton("Ver bitacora", on_click=lambda _: [self.animar(self.formularioBitacora, self.formularioBitacora, page), self.cambiarTitulo(page, "Historial de Inicios de sesion"), self.volverGenerarBitacora(page, self.cedula)])
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.formularioBitacora = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            padding=padding.only(top=10),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                spacing=20,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.listaBitacora,
                    ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiarTitulo(page, "Lideres de Calle"), self.cambiar_pagina(5.5), self.regresarViewFalse(page)]),
                ]
            )
        )

        self.contenedorBombonas = Container(
            height=635,
            width=815,
            padding=15,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            border_radius=border_radius.all(15),
            alignment=alignment.center,
            content=Column(
                spacing=30,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    ElevatedButton("Agregar nueva Empresa", on_click=lambda _: self.nuevaEmpresa(page)),
                    #ElevatedButton("Agregar nuevo Tamaño", on_click=lambda _: self.nuevoTamano(page)),
                    ElevatedButton("Agregar nuevo Pico", on_click=lambda _: self.nuevoPico(page))            
                ]
            )
        )

        #SALTOS DE VISTAS
        #Contenedor del medio
        self.formulario = AnimatedSwitcher(
            self.contenedorInicio,
            expand=True, 
            transition=AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=AnimationCurve.BOUNCE_OUT,
            switch_out_curve=AnimationCurve.BOUNCE_IN
        )

        return View(
            "/liderPolitico",
            padding=5,
            controls=[
                self.appbar,

                Container(
                    padding=0,
                    margin=0,
                    content=Row(
                        alignment=CrossAxisAlignment.START,
                        controls=[
                            self.slider,
                            self.formulario
                        ]
                    )
                )
            ]
        )
