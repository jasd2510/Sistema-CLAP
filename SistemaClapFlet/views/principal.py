from flet import *
from flet_route import Params, Basket
from datetime import datetime
from time import sleep

import os
import pathlib
import shutil

import logica
import reporte

class principal:
    def __init__(self):
        self.logo = Image(src=f"{logica.rutaactual}\img\clap.png", height=80)        
        #self.logo = Image(src="SistemaClapFlet\img\clap.png", height=80)
        self.indicator = Container(bgcolor='WHITE', width=140, height=40, border_radius=border_radius.only(topLeft=15, bottomLeft=15), offset=transform.Offset(0.075,5.5), animate_offset=animation.Animation(500, AnimationCurve.DECELERATE))

    def view(self, page:Page, params:Params, basket:Basket):

        self.CedulaParametro = ""
        self.cartas = []
        self.bitacoraLista = []

        #DATOS DEL JEFE DE FAMILIA
        self.nombreJ = Text("")
        self.apellidoJ = Text("")
        self.cedulaJ = Text("")
        self.ubicacionJ = Text("")
        self.calleVeredaJ = Text("")
        self.telefonoJ = Text("")
        self.correoJ = Text("")

        #DATOS DEL LIDER DE CALLE
        self.nombreLi = Text("")
        self.apellidoLi = Text("")
        self.cedulaLi = Text("")
        self.ubicacionLi = Text("")
        self.telefonoLi = Text("")
        self.correoLi = Text("")

        self.iDLiderCalle = logica.datoUser[0][0]
        self.nombreLiderCalle = logica.datoUser[0][1]
        self.ApellidoLiderCalle = logica.datoUser[0][2]
        self.UbicacionLiderCalle = logica.datoUser[0][3]
        self.idUsuario = logica.datoUser[0][4]
        self.fechaEntradaUser = logica.datoUser[0][5]

        self.textoSlider = Text(f"{self.nombreLiderCalle}", weight=FontWeight.W_500, color="WHITE")


        page.title = "CLAP"
        page.window_resizable = False
        page.window_height = "800"
        page.window_width = "1000"
        page.window_center()
        page.window_maximizable = False

        #page.window_prevent_close = True
        #page.on_window_event = lambda _:self.window_event(page)

        self.titulo = Text("Mi Comunidad", style=TextThemeStyle.TITLE_LARGE, color="white")
        self.tituloCilindroPropietario = Text("", style=TextThemeStyle.TITLE_LARGE)
        self.tituloCilindroSeleccionado = Text("", style=TextThemeStyle.TITLE_LARGE)
        self.tituloAgregarJefes = Text("No tienes a ningun Jefe de Familia resgistrado, pusla agregar para añadir a los jefes familiares", style=TextThemeStyle.TITLE_LARGE)

        #self.barraBusqueda = TextField(hint_text="Buscar Jefe de Familia", width=280, height=40)

        #TEXTFIELDS REGISTRO
        self.nombre = TextField(label="Nombre", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.nombre), logica.validarNombres(self.nombre, page)])
        self.apellido = TextField(label="Apellido", hint_text="Minimo 4 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.apellido), logica.validarNombres(self.apellido, page)])
        self.tipoCedula = Dropdown(label="Tipo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.tipoCedula), options=[
                dropdown.Option("V"), dropdown.Option("E")])
        self.tipoCedula.value = "V"
        self.cedula = TextField(label="Cedula", hint_text="Minimo 7 caracteres", border_color="#820000", border_radius=20, width=180, height=60, max_length=8, on_change=lambda _: [self.quitarError(page, self.cedula), logica.validarNumeros(self.cedula, page)])
        self.cantidadCi = Dropdown(label="Cantidad de cilindros", border_radius=30, border_color="#820000", width=300, height=60, value=0, on_change=lambda _: [self.volverGenerarCilindros(page), self.quitarError(page, self.cantidadCi)], options=[
                dropdown.Option("1"), dropdown.Option("2"), dropdown.Option("3"),
                dropdown.Option("4"), dropdown.Option("5"), dropdown.Option("6"),
                dropdown.Option("7"), dropdown.Option("8"), dropdown.Option("9"),
            ]
        )

        self.codigoTelefono = Dropdown(hint_text="Codigo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.codigoTelefono), options=[
                dropdown.Option("0412"), dropdown.Option("0414"), dropdown.Option("0416"), dropdown.Option("0424"), dropdown.Option("0238")])
        self.numeroTelefono = TextField(label="N telefono", hint_text="0000000", border_color="#820000", border_radius=20, width=180, height=60, max_length=7, on_change=lambda _: [self.quitarError(page, self.numeroTelefono), logica.validarNumeros(self.numeroTelefono, page)])
        self.correo = TextField(label="Direccion", hint_text="ej: clapcamoruco", border_color="#820000", border_radius=20, width=180, height=60, on_change=lambda _:[self.quitarError(page, self.correo), logica.validarCorreo(self.correo, page)])
        self.tipoCorreo = Dropdown(hint_text="Correo", color="black",border_color="#820000", border_radius=20, width=120, height=60, on_change=lambda _: self.quitarError(page, self.tipoCorreo), options=[
                dropdown.Option("@gmail.com"), dropdown.Option("@hotmail.com"), dropdown.Option("@outlook.com")])

        self.columnaContenedor = Row(
            vertical_alignment=MainAxisAlignment.CENTER,
            alignment=alignment.center,
            wrap=True,
        )

        self.columnaCards = Row(
            wrap=True,
        )

        self.tablaCilindros = DataTable(
            bgcolor="#C5283D",
            columns=[
                DataColumn(Text("id", color="WHITE")),
                DataColumn(Text("Empresa", color="WHITE")),
                DataColumn(Text("Tamano", color="WHITE")),
                DataColumn(Text("Pico", color="WHITE")),
                DataColumn(Text("Fecha Registrado", color="WHITE")),
                DataColumn(Text("Accion", color="WHITE"))
            ],
            rows=[

            ]
        )

        self.tablaPedido = DataTable(
            bgcolor="#C5283D",
            columns=[
                DataColumn(Text("id", color="WHITE")),
                DataColumn(Text("Empresa", color="WHITE")),
                DataColumn(Text("Tamano", color="WHITE")),
                DataColumn(Text("Pico", color="WHITE")),
                DataColumn(Text("Accion", color="WHITE"))
            ],
            rows=[

            ]
        )

        self.tablaJornadaPrincipal = DataTable(
            bgcolor="#C5283D",
            column_spacing=30,
            columns=[
                #DataColumn(Text("id")),
                DataColumn(Text("Ci", color="WHITE")),
                DataColumn(Text("Nombre", color="WHITE")),
                DataColumn(Text("Apellido", color="WHITE")),
                DataColumn(Text("Empresa", color="WHITE")),
                DataColumn(Text("Tamano", color="WHITE")),
                DataColumn(Text("Pico", color="WHITE")),
                DataColumn(Text("Agregado", color="WHITE")),
                DataColumn(Text("Accion", color="WHITE"))
            ],
            rows=[

            ]
        )

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
                    PopupMenuButton(items=[PopupMenuItem(text="Cerrar sesion", on_click=lambda _: self.salir(page))])
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
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Mi Comunidad")],
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
                                        on_click=lambda e: [self.animar(self.contenedorReporte, self.contenedorReporte, page), self.cambiar_pagina(6.8), self.volverGenerarJornada(page), self.cambiarTitulo(page, "Administrador de Jornada")],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.EDIT_NOTE),
                                                Text("Reporte")
                                            ]
                                        )
                                    ),

                                    Container(
                                        margin=margin.only(top=20),
                                        padding=padding.only(left=35),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorHistorial, self.contenedorHistorial, page), self.cambiar_pagina(8.2), self.volverGenerarArchivos(page), self.cambiarTitulo(page, "Historial de jornadas")],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.EVENT_NOTE),
                                                Text("Historial")
                                            ]
                                        )
                                    ),
                                    Container(
                                        margin=margin.only(top=20),
                                        padding=padding.only(left=35),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorPerfilLider, self.contenedorPerfilLider, page), self.cargarDatosLider(page), self.cambiar_pagina(9.5), self.cambiarTitulo(page, "Mis datos")],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.PEOPLE),
                                                Text("Perfil")
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
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Row(
                        height=50,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            #self.barraBusqueda,
                            Text(""),
                            ElevatedButton("Agregar", bgcolor="GREEN", color="WHITE",on_click= lambda _: [self.animar(self.formularioJefe, self.formularioJefe, page), self.cambiarTitulo(page, "Datos Personales del Jefe de Familia")])
                        ]
                    ),

                    Container(
                        height=550,
                        border_radius=border_radius.all(7),  
                        content=Column(
                            expand=True,
                            height=550,
                            scroll=ScrollMode.ALWAYS,
                            controls=[
                                self.columnaCards,
                                self.tituloAgregarJefes
                            ]
                        )
                    )
                ]
            )
        )

        self.contenedorReporte = Container(
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
                                self.tablaJornadaPrincipal,
                            ]
                        )
                    ),

                    Row(
                        controls=[
                            ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Mi Comunidad")]),
                            ElevatedButton("Generar Reporte",bgcolor="GREEN", color="WHITE", on_click=lambda _:self.confirmarReporte(page))
                        ]
                    ),
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

        #CONTENEDOR CON LOS DATOS PERSONALES DEL JEFE DE FAMILIA DONDE SE PUEDE EDITAR
        self.contenedorPerfilJefe = Container(
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
                        padding=padding.only(top=60),
                        border_radius=border_radius.all(40),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Nombre:"),
                                        self.nombreJ,
                                        IconButton(icon=icons.EDIT, tooltip="Editar Nombre", on_click=lambda _: self.editNombre(page, self.nombreJ.value))
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Apellido:"),
                                        self.apellidoJ,
                                        IconButton(icon=icons.EDIT, tooltip="Editar Apellido", on_click=lambda _: self.editApellido(page, self.apellidoJ.value))
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Cedula:"),
                                        self.cedulaJ,
                                        IconButton(icon=icons.EDIT, tooltip="Editar Cedula", on_click=lambda _: self.editCedula(page, self.cedulaJ.value[0],self.cedulaJ.value[2:]))
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Ubicacion:"),
                                        self.ubicacionJ,
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Telefono:"),
                                        self.telefonoJ,
                                        IconButton(icon=icons.EDIT, tooltip="Editar Telefono", on_click=lambda _: self.editTelefono(page, self.telefonoJ))
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Correo:"),
                                        self.correoJ,
                                        IconButton(icon=icons.EDIT, tooltip="Editar Correo", on_click=lambda _: self.editCorreo(page, self.correoJ))
                                    ]
                                ),
                                ElevatedButton("Regresar a inicio", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Mi Comunidad")]),
                            ]
                        )
                    )
                ]
            )
        )

        #CONTENEDOR CON LOS DATOS PERSONALES DEL LIDER DE CALLE DONDE SE PUEDE EDITAR
        self.contenedorPerfilLider = Container(
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
                        padding=padding.only(top=60),
                        border_radius=border_radius.all(40),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=10,
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
                                        Text("Ubicacion:"),
                                        self.ubicacionLi,
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Telefono:"),
                                        self.telefonoLi,
                                        IconButton(icon=icons.EDIT, tooltip="Editar Telefono", on_click=lambda _: self.editTelefonoLi(page, self.telefonoLi))
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        Text("Correo:"),
                                        self.correoLi,
                                        IconButton(icon=icons.EDIT, tooltip="Editar Correo", on_click=lambda _: self.editCorreoLi(page, self.correoLi))
                                    ]
                                ),
                                ElevatedButton("Regresar a inicio", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Mi Comunidad")]),
                            ]
                        )
                    )
                ]
            )
        )

        #FORMULARIO REGISTRO JEFE
        self.formularioJefe = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            padding=padding.only(top=30),
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
                            spacing=10,
                            controls=[
                                Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        self.nombre,
                                        self.apellido,
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            controls=[
                                                self.tipoCedula,
                                                self.cedula,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            controls=[
                                                self.codigoTelefono,
                                                self.numeroTelefono
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            controls=[
                                                self.correo,
                                                self.tipoCorreo
                                            ]
                                        ),
                                        self.cantidadCi,
                                    ]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.regresarInicio(page), self.cambiarTitulo(page, "Mi Comunidad")]),
                                        ElevatedButton("Seguir",bgcolor="GREEN", color="WHITE", on_click=lambda _: self.generarFormularioCilindros(page))
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.formularioCilindro = Container(
            height=635,
            width=815,
            expand=True,
            padding=10,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            border_radius=border_radius.all(15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.columnaContenedor,
                    ElevatedButton("Guardar", bgcolor="GREEN", color="#ffffff",  on_click=lambda _:self.abrirAlertConfirmarCilindros(page)),
                    ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[self.regresarFormularioJefe(page), self.cambiarTitulo(page, "Datos Personales del Jefe de Familia")])
                ]
            )
        )

        #VISTA DE CILINDROS DE JEFES DE FAMILIA
        self.contenedorJefeFamilia = Container(
            height=635,
            width=815,
            padding=3,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            border_radius=border_radius.all(15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Row(
                        vertical_alignment=MainAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:self.animar(self.contenedorInicio, self.contenedorInicio, page)),
                            self.tituloCilindroPropietario,
                            Row(
                                vertical_alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    ElevatedButton("Ver informacion", on_click=lambda _: [self.cargarDatosJefe(page), self.animar(self.contenedorPerfilJefe, self.contenedorPerfilJefe, page)]),
                                    ElevatedButton("Anadir Cilindro", bgcolor="GREEN", color="#ffffff", on_click=lambda _: self.abrirAnadirCilindro(page))
                                ]
                            ),
                            #ElevatedButton("Anadir Cilindro", bgcolor="GREEN", color="#ffffff", on_click=lambda _: self.abrirAnadirCilindro(page))
                        ]
                    ),
                    Container(
                        height=260,
                        bgcolor="WHITE",
                        content=Column(
                            scroll=ScrollMode.ALWAYS,
                            expand=True,
                            controls=[
                               self.tablaCilindros 
                            ]
                        )
                    ),
                    self.tituloCilindroSeleccionado,
                    Container(
                        height=260,
                        bgcolor="WHITE",
                        content=Column(
                            scroll=ScrollMode.ALWAYS,
                            expand=True,
                            controls=[
                               self.tablaPedido
                            ]
                        )
                    ),
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
            "/principal",
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

#MOVERSE
    def animar(self, contenedor1, contenedor2, pageee):
        contenedor1 = contenedor1
        contenedor2 = contenedor2
        pageee = pageee

        self.formulario.content = contenedor2 if self.formulario.content == contenedor1 else contenedor1
        pageee.update()

    def cambiar_pagina(self, ye):
        ye = ye

        self.indicator.offset.y = ye
        self.indicator.update()

    def quitarError(self, pageee, textfield):
        pageee = pageee
        textfield = textfield

        textfield.error_text = None
        pageee.update()

    def regresarInicio(self, pagee):
        pagee = pagee

        self.nombre.value = ""
        self.apellido.value = ""
        self.cedula.value = ""
        self.cantidadCi.value = 0
        self.numeroTelefono.value = ""
        self.codigoTelefono.value = None
        self.correo.value = ""
        self.tipoCorreo.value = None
        self.tipoCedula.value = "V"

        self.animar(self.contenedorInicio, self.contenedorInicio, pagee)

    def regresarFormularioJefe(self, pagee):
        pagee = pagee

        self.empresa.value = None
        self.pico.value = None
        self.tamano.value = None
        self.cantidadCi.value = 0
        
        datosCilindros.clear()
        itemsCilindros.clear()

        self.animar(self.formularioJefe, self.formularioJefe, pagee)

        pagee.update()

#GENERAR CARTAS DE LOS LIDERES DE CALLE Y VER INFORMACION
    def volverGenerarCartas(self, pageeee):
        pageeee = pageeee

        if logica.consulta("SELECT jefesf.id FROM jefesf JOIN lideres ON lideres_id = lideres.id WHERE lideres.id = ?", [self.iDLiderCalle]):
            self.columnaCards.controls.clear()
            self.tituloAgregarJefes.visible = False
            self.columnaCards.controls = self.generarCards(pageeee)
            pageeee.update()
        else:
            pass

    def generarCards(self, pagee):
        pagee = pagee

        querySelectJefe = "SELECT id, nombre, apellido, ci FROM jefesf WHERE lideres_id =?"
        resultado = logica.consulta(querySelectJefe, [self.iDLiderCalle])

        for ids, nom, ape, ci in resultado:
            self.cartas.append(
                Container(
                    bgcolor="RED",
                    height=150,
                    width=250,
                    padding=padding.all(7),
                    border_radius=border_radius.all(20),
                    on_click=lambda _, ids=ids: self.generarJefe(ids, pagee),
                    content=Column(
                        controls=[
                            Text(f"{nom} {ape}", style=TextThemeStyle.TITLE_LARGE, color="WHITE"),
                            Text(f"{ci}", style=TextThemeStyle.TITLE_MEDIUM, color="WHITE"),
                        ]
                    )
                )
            )
            pagee.update()

        return self.cartas

    def regresarAlInicioCompletado(self, pageeee):
        pageeee = pageeee

        self.nombre.value = ""
        self.apellido.value = ""
        self.cedula.value = ""
        self.cantidadCi.value = None
        self.numeroTelefono.value = ""
        self.codigoTelefono.value = None
        self.correo.value = ""
        self.tipoCorreo.value = None
        self.tipoCedula.value = "V"

        itemsCilindros.clear()
        datosCilindros.clear()

        self.empresa.value = None
        self.pico.value = None
        self.tamano.value = None
        self.cantidadCi.value = 0

        listaId.clear()

        self.cartas.clear()
        self.volverGenerarCartas(pageeee)

        self.animar(self.contenedorInicio, self.contenedorInicio, pageeee)

    def seleccionarJefe(self, jefe, pageeeee):
        jefe = jefe
        pageeeee = pageeeee

        cells = []

        global cedulaIdentidad
        cedulaIdentidad = jefe


        queryy = "SELECT cilindros.id, empresas.empresa, tamanos.tamano, picos.pico, cilindros.fechaAsignada FROM cilindros JOIN empresas ON empresas_id = empresas.id JOIN tamanos ON tamanos_id = tamanos.id JOIN picos ON picos_id = picos.id JOIN jefesf ON jefesf_id = jefesf.id WHERE jefesf.id = ? AND cilindros.estatus = 1"
        resultado = logica.consulta(queryy, [jefe])

        for idss, empresa, tamano, pico, fecaRegistrada in resultado:
            cells.append(DataRow(
                color="WHITE",
                cells=[
                    DataCell(Text(f"{idss}")),
                    DataCell(Text(f"{empresa}")),
                    DataCell(Text(f"{tamano}")),
                    DataCell(Text(f"{pico}")),
                    DataCell(Text(f"{fecaRegistrada[:-13]}")),
                    DataCell(Row(controls=[IconButton(icon=icons.EDIT, tooltip="Editar Cilindro", on_click=lambda _, idss=idss: self.abrirEditarCilindro(pageeeee, idss)), IconButton(icon=icons.DELETE, tooltip="Eliminar Cilindro", on_click=lambda _, idss=idss: self.abrirEliminarCilindro(pageeeee, idss))]))
                ],
                on_select_changed=lambda _, idss=idss: self.seleccionarJornada(idss, pageeeee)
            ),
            )

            pageeeee.update()

        return cells

#VALIDAR Y GUARDAR INFROMACION DE LOS FORMULARIOS DE JEFES DE FAMILIA Y CILINDROS
    def generarFormularioCilindros(self, pagee):
        pagee = pagee

        arregloCedula = f"{self.tipoCedula.value}-{self.cedula.value}"

        queryy = "SELECT jefesf.nombre, jefesf.apellido FROM jefesf WHERE jefesf.ci = ?"
        resultado = logica.consulta(queryy, [arregloCedula])

        arregloCorreo = f"{self.correo.value}{self.tipoCorreo.value}"
        arregloTelefono = f"{self.codigoTelefono.value}-{self.numeroTelefono.value}"

        if (self.nombre.value == "") or (self.apellido.value == "") or (self.cedula.value == "") or (self.numeroTelefono.value == "") or (self.correo.value == "") or (self.tipoCorreo.value == None) or (self.codigoTelefono.value == None) or (self.cantidadCi.value == 0) or (len(self.nombre.value) in range(1, 3)) or (len(self.apellido.value) in range(1, 4)) or (len(self.cedula.value) in range(1, 7)) or (len(self.numeroTelefono.value) in range(1, 7)):
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

            if self.tipoCorreo.value == None:
                self.tipoCorreo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.codigoTelefono.value == None:
                self.codigoTelefono.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if self.cantidadCi.value == 0:
                self.cantidadCi.error_text = "Campo vacio, por favor seleccione para continuar"
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

        elif logica.consulta(queryy, [arregloCedula]):
            pagee.snack_bar = SnackBar(content=Text(f"Esta cedula ya esta registrada, a nombre de {resultado[0][0]} {resultado[0][1]}"))
            pagee.snack_bar.open = True
            pagee.update()

        elif logica.consulta("SELECT id FROM jefesf WHERE telefono =?", [arregloTelefono]):
            pagee.snack_bar = SnackBar(content=Text("Este numero de telefono ya esta asignado a un usuario"))
            pagee.snack_bar.open = True
            pagee.update()

        elif logica.consulta("SELECT id FROM jefesf WHERE correo =?", [arregloCorreo]):
            pagee.snack_bar = SnackBar(content=Text("Este correo ya esta en uso"))
            pagee.snack_bar.open = True
            pagee.update()

        else:
            self.cambiarTitulo(pagee, f"Datos de Cilindros de {self.nombre.value} {self.apellido.value}")
            self.animar(self.formularioCilindro, self.formularioCilindro, pagee)

    def volverGenerarCilindros(self, pageee):
        pageee = pageee

        self.columnaContenedor.controls = self.itemsCilindros(int(self.cantidadCi.value), pageee)

        pageee.update()

    def itemsCilindros(self, count, pagee):
        pagee = pagee

        global itemsCilindros
        global datosCilindros

        itemsCilindros = []
        datosCilindros = []
        # Necesito hacer una variable global que contenga otra lista donde se guardaran los valores de cada dropdow

        count = count + 1

        for formularioIndividual in range(1, count):

            self.empresa = Dropdown(hint_text="Seleccionar empresa", height=60, width=130)
            self.tamano = Dropdown(hint_text="Seleccionar tamaño", height=60, width=130)
            self.pico = Dropdown(hint_text="Seleccionar pico", height=60, width=130)

            
            for emp in logica.consulta("SELECT empresa FROM empresas"):
                self.empresa.options.append(dropdown.Option(emp[0]))

            
            for tam in logica.consulta("SELECT tamano FROM tamanos"):
                self.tamano.options.append(dropdown.Option(tam[0]))


            for pic in logica.consulta("SELECT pico FROM picos"):
                self.pico.options.append(dropdown.Option(pic[0]))

            self.empresa.value = "Radelco"
            self.tamano.value = "Pequeña"
            self.pico.value = "Presion"

            itemsCilindros.append(
                Container(
                    height=250,
                    border_radius=border_radius.all(15),
                    width=150,
                    bgcolor="WHITE",
                    border=border.all(2, "#C5283D"),
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            Text(f"Cilindro {str(formularioIndividual)}", weight=FontWeight.W_500,),
                            Text("Empresa:", size=10, weight=FontWeight.W_900),
                            self.empresa,
                            Text("Tamaño:", size=10, weight=FontWeight.W_900),
                            self.tamano,
                            Text("Pico:", size=10, weight=FontWeight.W_900),
                            self.pico
                        ]
                    )
                )
            )

            datosCilindros.append([self.empresa, self.tamano, self.pico])

            pagee.update()
        
        return itemsCilindros

    def abrirAlertConfirmarCilindros(self, pageee):
        pageee = pageee
        
        self.textoConfirmar = Text(f"Estas seguro que desea registrar al lider de familia {self.nombre.value} {self.apellido.value}?")
        self.btnConfirmarCilin = TextButton("Confirmar", on_click=lambda _:[self.guardarJefe(pageee)])
        self.btnCancelarCilin = TextButton("Cancelar", on_click=lambda _:[self.cerrarAlertJornada(pageee, self.alertConfirmarCilindros)])

        self.alertConfirmarCilindros = AlertDialog(content=self.textoConfirmar,
            actions=[self.btnConfirmarCilin, self.btnCancelarCilin]
        )

        pageee.dialog = self.alertConfirmarCilindros
        self.alertConfirmarCilindros.open = True

        pageee.update()

    def guardarJefe(self, pagee):
        pagee = pagee
        
        global listaId
        listaId = []

        arregloCedulaa = f"{self.tipoCedula.value}-{self.cedula.value}"
        arregloCorreo = f"{self.correo.value}{self.tipoCorreo.value}"
        arregloTelefono = f"{self.codigoTelefono.value}-{self.numeroTelefono.value}"

        self.alertConfirmarCilindros.actions.clear()
        self.textoConfirmar.value = "Guardando datos, por favor espere"
        pagee.update()

        #INSERTAR LOS DATOS DEL LIDER DE FAMILIA
        logica.consulta("INSERT INTO jefesf VALUES (NULL, ?, ?, ?, ?, ?, ?, 1)", [arregloCedulaa, self.nombre.value, self.apellido.value, arregloTelefono, arregloCorreo, self.iDLiderCalle])

        #OBTENER EL ID DEL LIDER DE FAMILIA
        idJefeFamiliar = logica.consulta("SELECT id FROM jefesf WHERE ci = ?", [arregloCedulaa])

        #CONSULTA PARA SELECCIONAR LOS IDS
        queryEmpresa = "SELECT id FROM empresas WHERE empresa =?"
        queryTamano = "SELECT id FROM tamanos WHERE tamano =?"
        queryPico = "SELECT id FROM picos WHERE pico =?"

        #CICLO PARA OBTENER LOS IDS
        for empresa, tamano, pico in datosCilindros:
            resultadoIdEmpresa = logica.consulta(queryEmpresa, [empresa.value])
            resultadoIdEmpresa = resultadoIdEmpresa[0][0]

            resultadoIdTamano = logica.consulta(queryTamano, [tamano.value])
            resultadoIdTamano = resultadoIdTamano[0][0]

            resultadoIdPico = logica.consulta(queryPico, [pico.value])
            resultadoIdPico = resultadoIdPico[0][0]

            listaId.append([resultadoIdEmpresa, resultadoIdPico, resultadoIdTamano])

        #GUARDAMOS LOS CILINDROS EN LA BASE DE DATOS
        queryGuardarCilindros = "INSERT INTO cilindros VALUES (NULL, ?, ?, ?, ?, ?, 1)"

        for empresaId, picoId, tamanoId in listaId:
            fecha = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            fecha = str(fecha)

            logica.consulta(queryGuardarCilindros, [str(empresaId), str(picoId), str(tamanoId), idJefeFamiliar[0][0], str(fecha)])
            sleep(0.1)

        self.cerrarAlertJornada(pagee, self.alertConfirmarCilindros)
        self.cambiarTitulo(pagee, "Mi Comunidad")
        self.regresarAlInicioCompletado(pagee)


    #ESTA FUNCION HACE UNA CONSULTA A LA TABLA PEDIDOS SI RETORNA ALGO SE ACTIVA LA OTRA DATATABLE
    def generarJefe(self,jefee, pageee):
        jefee = jefee
        pageee = pageee

        nombreLiderFamilia = logica.consulta("SELECT nombre FROM jefesf WHERE id =?", [jefee])

        query = "SELECT pedidos.id, cilindros.id, empresas.empresa, tamanos.tamano, picos.pico FROM pedidos JOIN cilindros ON cilindros_id = cilindros.id JOIN jefesf ON jefesf_id = jefesf.id JOIN empresas ON empresas_id = empresas.id JOIN tamanos ON tamanos_id = tamanos.id JOIN picos ON picos_id = picos.id WHERE jefesf.id = ? AND pedidos.archivos_id IS NULL"
        resultadoQuery = logica.consulta(query, [jefee])

        self.tablaCilindros.rows.clear()
        self.tituloCilindroPropietario.value = f"Cilindros de {nombreLiderFamilia[0][0]}"
        self.tablaCilindros.rows = self.seleccionarJefe(jefee, pageee)

        if resultadoQuery:
            self.tituloCilindroSeleccionado.value = "Cilindros Seleccionados"
            self.tablaPedido.visible = True
            self.tablaPedido.rows = self.seleccionarPedido(resultadoQuery, pageee)
            self.quitarCilindrosRepetidos(pageee, jefee)
            pageee.update()
            
        else:
            self.tituloCilindroSeleccionado.value = ""
            self.tablaPedido.visible = False
            pageee.update()

        self.animar(self.contenedorJefeFamilia, self.contenedorJefeFamilia, pageee)

        pageee.update()

    def quitarCilindrosRepetidos(self, pagee, ci):
        pagee = pagee
        ci = ci

        queryy = "SELECT cilindros.id FROM pedidos JOIN cilindros ON cilindros_id = cilindros.id JOIN jefesf ON jefesf_id = jefesf.id WHERE jefesf.id =? AND pedidos.archivos_id IS NULL"
        resultadoC = logica.consulta(queryy, [ci])

        numFilas = self.tablaCilindros.rows[:]

        for i in numFilas:
            numFila = numFilas.index(i)

            valor = self.tablaCilindros.rows[numFila].cells[0].content.value

            for e in resultadoC:
                
                if valor == f"{e[0]}":
                    self.tablaCilindros.rows[numFila].visible = False
                    pagee.update()
                    break

    def seleccionarPedido(self, resultadoo, page):
        resultadoo = resultadoo
        page = page

        listPedido = []

        for idPedido, ids, empr, tamn, pic in resultadoo:
            listPedido.append(DataRow(
                color="WHITE",
                cells=[
                    DataCell(Text(f"{ids}")),
                    DataCell(Text(f"{empr}")),
                    DataCell(Text(f"{tamn}")),
                    DataCell(Text(f"{pic}")),
                    DataCell(Row(controls=[IconButton(icon=icons.CANCEL, tooltip="Quitar", on_click=lambda _, idPedido=idPedido: self.eliminarJornadaJefe(idPedido, page))]))
                ],
            ),
            )

            page.update()

        return listPedido

#CRUD DE CILINDROS
    def abrirEliminarCilindro(self, pagee, ids):
        pagee = pagee
        ids = ids

        self.alertElminar = AlertDialog(modal=True, content=Text("Seguro que deseas eleminar el cilindro?"), actions=[TextButton("Si", on_click=lambda _: self.EliminarCilindro(ids, pagee)), TextButton("No", on_click=lambda _:self.cerrAlertEleminar(pagee))])

        pagee.dialog = self.alertElminar
        self.alertElminar.open = True

        pagee.update()

    def EliminarCilindro(self, ide, pageeee):
        ide = ide
        pageee = pageeee

        queryElminar = "UPDATE cilindros SET estatus = 2 WHERE id =?"

        logica.consulta(queryElminar, [ide])

        self.cerrAlertEleminar(pageeee)

        self.generarJefe(cedulaIdentidad, pageeee)

        pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El cilindro se elimino correctamente"))
        pageee.snack_bar.open = True

        pageeee.update()

    def abrirAnadirCilindro(self, pagee):
        pagee = pagee

        self.empresaAnadir = Dropdown(hint_text="Seleccionar empresa", height=60, width=240, on_change=lambda _: self.quitarError(pagee, self.empresaAnadir))
        self.tamanoAnadir = Dropdown(hint_text="Seleccionar tamaño", height=60, width=240, on_change=lambda _: self.quitarError(pagee, self.tamanoAnadir))
        self.picoAnadir = Dropdown(hint_text="Seleccionar pico", height=60, width=240, on_change=lambda _: self.quitarError(pagee, self.picoAnadir))
            
        for emp in logica.consulta("SELECT empresa FROM empresas"):
            self.empresaAnadir.options.append(dropdown.Option(emp[0]))
            
        for tam in logica.consulta("SELECT tamano FROM tamanos"):
            self.tamanoAnadir.options.append(dropdown.Option(tam[0]))

        for pic in logica.consulta("SELECT pico FROM picos"):
            self.picoAnadir.options.append(dropdown.Option(pic[0]))

        self.alertAnadir = AlertDialog(
            content=Container(
                height=300,
                width=150,
                bgcolor="white",
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    spacing=10,
                    controls=[
                        self.empresaAnadir,
                        self.tamanoAnadir,
                        self.picoAnadir
                    ]
                )
            ),
            actions=[
                Row(
                    controls=[
                        ElevatedButton("Agregar", on_click=lambda _:self.anadirCilindro(pagee, self.empresaAnadir, self.tamanoAnadir, self.picoAnadir)),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrAlertAnadir(pagee))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertAnadir
        self.alertAnadir.open = True

        pagee.update()

    def anadirCilindro(self, pageee, empresa, tamano, pico):
        pageee = pageee
        empresa = empresa
        tamano = tamano
        pico = pico

        if (empresa.value == None) or (tamano.value == None) or (pico.value == None):
            
            if empresa.value == None:
                empresa.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if tamano.value == None:
                tamano.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if pico.value == None:
                pico.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            
            else:
                return

        else:
            queryEmpresa = "SELECT id FROM empresas WHERE empresa =?"
            queryTamano = "SELECT id FROM tamanos WHERE tamano =?"
            queryPico = "SELECT id FROM picos WHERE pico =?"

            resultadoIdEmpresa = logica.consulta(queryEmpresa, [empresa.value])
            resultadoIdEmpresa = resultadoIdEmpresa[0][0]

            resultadoIdTamano = logica.consulta(queryTamano, [tamano.value])
            resultadoIdTamano = resultadoIdTamano[0][0]

            resultadoIdPico = logica.consulta(queryPico, [pico.value])
            resultadoIdPico = resultadoIdPico[0][0]

            fecha = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            fecha = str(fecha)

            resultadoIdJefe = logica.consulta("SELECT id FROM jefesf WHERE id = ?", [cedulaIdentidad])

            logica.consulta("INSERT INTO cilindros VALUES (NULL, ?, ?, ?, ?, ?, 1)", [resultadoIdEmpresa, resultadoIdPico, resultadoIdTamano, resultadoIdJefe[0][0], fecha])

            self.cerrAlertAnadir(pageee)

            self.generarJefe(cedulaIdentidad, pageee)

            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("Se agrego el cilindro correctamente"))
            pageee.snack_bar.open = True

            pageee.update()

    def abrirEditarCilindro(self, pagee, ids):
        pagee = pagee
        ids = ids

        self.empresaEdit = Dropdown(hint_text="Seleccionar empresa", height=60, width=240)
        self.tamanoEdit = Dropdown(hint_text="Seleccionar tamaño", height=60, width=240)
        self.picoEdit = Dropdown(hint_text="Seleccionar pico", height=60, width=240)

        for emp in logica.consulta("SELECT empresa FROM empresas"):
            self.empresaEdit.options.append(dropdown.Option(emp[0]))
            
        for tam in logica.consulta("SELECT tamano FROM tamanos"):
            self.tamanoEdit.options.append(dropdown.Option(tam[0]))

        for pic in logica.consulta("SELECT pico FROM picos"):
            self.picoEdit.options.append(dropdown.Option(pic[0]))

        querySelect = "SELECT empresas.empresa, tamanos.tamano, picos.pico FROM cilindros JOIN empresas ON empresas_id = empresas.id JOIN tamanos ON tamanos_id = tamanos.id JOIN picos ON picos_id = picos.id WHERE Cilindros.id = ?"
        resultadoGeneral = logica.consulta(querySelect, [ids])

        empresaV = resultadoGeneral[0][0]
        tamanoV = resultadoGeneral[0][1]
        picoV = resultadoGeneral[0][2]

        #SELECCIONAR EMPRESA
        if empresaV == empresaV:
            self.empresaEdit.value = empresaV
            pagee.update()

        #SELECCIONAR TAMANO
        if tamanoV == tamanoV:
            self.tamanoEdit.value = tamanoV
            pagee.update()

        #SELECCIONAR PICO
        if picoV == picoV:
            self.picoEdit.value = picoV
            pagee.update()

        self.alertEditar = AlertDialog(
            content=Container(
                height=250,
                width=150,
                bgcolor="white",
                content=Column(
                    spacing=10,
                    controls=[
                        self.empresaEdit,
                        self.tamanoEdit,
                        self.picoEdit
                    ]
                )
            ),
            actions=[
                Row(
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.editarCilindro(pagee, self.empresaEdit, self.tamanoEdit, self.picoEdit, ids)),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrAlertEditar(pagee))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditar
        self.alertEditar.open = True

        pagee.update()

    def editarCilindro(self, pagee, emp, tamn, pic, idsss):
        pagee = pagee
        emp = emp
        tamn = tamn
        pic = pic
        idsss = idsss

        queryEmpresa = "SELECT id FROM empresas WHERE empresa =?"
        queryTamano = "SELECT id FROM tamanos WHERE tamano =?"
        queryPico = "SELECT id FROM picos WHERE pico =?"

        resultadoIdEmpresa = logica.consulta(queryEmpresa, [emp.value])
        resultadoIdEmpresa = resultadoIdEmpresa[0][0]

        resultadoIdTamano = logica.consulta(queryTamano, [tamn.value])
        resultadoIdTamano = resultadoIdTamano[0][0]

        resultadoIdPico = logica.consulta(queryPico, [pic.value])
        resultadoIdPico = resultadoIdPico[0][0]

        query = "UPDATE cilindros SET empresas_id =?, picos_id =?, tamanos_id =? WHERE id = ?"
        logica.consulta(query, [resultadoIdEmpresa, resultadoIdPico, resultadoIdTamano, idsss])

        self.cerrAlertEditar(pagee)

        self.generarJefe(cedulaIdentidad, pagee)

        pagee.snack_bar = SnackBar(content=Text(f"se edito el cilindro n{idsss}"), bgcolor="#4CBD49")
        pagee.snack_bar.open = True

        pagee.update()

    def cerrAlertEleminar(self, pageeee):
        pageeee = pageeee

        self.alertElminar.open = False

        pageeee.update()
    
    def cerrAlertAnadir(self, pageeee):
        pageeee = pageeee

        self.alertAnadir.open = False

        pageeee.update()

    def cerrAlertEditar(self, pageeee):
        pageeee = pageeee

        self.alertEditar.open = False

        pageeee.update()

    def seleccionarJornada(self, idsss, pagee):
        idsss = idsss
        pagee = pagee

        fecha = datetime.today().strftime('%d-%m-%Y')

        query = "INSERT INTO pedidos VALUES (NULL, ?, ?, NULL)"

        logica.consulta(query, [idsss, fecha])

        self.generarJefe(cedulaIdentidad, pagee)

        pagee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El cilindro fue seleccionado"))
        pagee.snack_bar.open = True
        pagee.update()

    def mostrarJornada(self):
        pass

    def eliminarJornada(self, idsss, page):
        idsss = idsss
        page = page

        query = "DELETE FROM pedidos WHERE id =?"
        logica.consulta(query, [idsss])

        self.volverGenerarJornada(page)

        page.update()

    def eliminarJornadaJefe(self, idsss, pagee):
        idsss = idsss
        pagee = pagee
        
        query = "DELETE FROM pedidos WHERE id =?"
        logica.consulta(query, [idsss])

        self.generarJefe(cedulaIdentidad, pagee)

        pagee.update()

    def volverGenerarJornada(self, pageee):
        pageee = pageee

        self.tablaJornadaPrincipal.rows = self.generarJornada(pageee)

        pageee.update()

    def generarJornada(self, pagee):
        pagee = pagee

        jorn = []

        queryy = "SELECT pedidos.id, jefesf.ci, jefesf.nombre, jefesf.apellido, empresas.empresa, tamanos.tamano, picos.pico, pedidos.fechaAgregada FROM pedidos JOIN cilindros ON cilindros_id = cilindros.id JOIN jefesf ON jefesf_id = jefesf.id JOIN empresas ON empresas_id = empresas.id JOIN tamanos ON tamanos_id = tamanos.id JOIN picos ON picos_id = picos.id JOIN lideres ON lideres_id = lideres.id WHERE lideres.id =? AND pedidos.archivos_id IS NULL ORDER BY jefesf.ci ASC"
        resultado = logica.consulta(queryy, [self.iDLiderCalle])

        for idss, cii, nom, ape, empresa, tamano, pico, fechaAgregado in resultado:
            jorn.append(DataRow(
                color="WHITE",
                cells=[
                    DataCell(Text(f"{cii}")),
                    DataCell(Text(f"{nom}")),
                    DataCell(Text(f"{ape}")),
                    DataCell(Text(f"{empresa}")),
                    DataCell(Text(f"{tamano}")),
                    DataCell(Text(f"{pico}")),
                    DataCell(Text(f"{fechaAgregado}")),
                    DataCell(Row(controls=[IconButton(icon=icons.CANCEL, tooltip="Quitar", on_click=lambda _, idss=idss: self.eliminarJornada(idss, pagee))]))
                ],
                #on_select_changed=lambda _, idss = idss: print(idss)
            ),
            )

            pagee.update()

        return jorn

    def confirmarReporte(self, pagee):
        pagee = pagee

        #self.progreso = ProgressRing(visible=False)
        self.textoEspera = Text("Estas seguro que deseas generar el reporte final?. La planilla se vaciara")

        self.alertJornada = AlertDialog(content=self.textoEspera,
            actions=[TextButton("Generar", on_click=lambda _: self.abrirJornada(pagee)), TextButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertJornada))]
        )

        pagee.dialog = self.alertJornada
        self.alertJornada.open = True

        pagee.update()

    def abrirJornada(self, pageee):
        pageee = pageee

        fecha = datetime.today().strftime('%d-%m-%Y')

        validarGeneracion = "SELECT archivos.fechaGenerado FROM pedidos JOIN archivos ON archivos_id IS NOT NULL = archivos.id JOIN cilindros ON cilindros_id = cilindros.id JOIN jefesf ON jefesf_id = jefesf.id WHERE lideres_id = ? AND archivos.fechaGenerado = ?"
        resultado = logica.consulta(validarGeneracion, [self.iDLiderCalle, fecha])
        queryy = "SELECT pedidos.id FROM pedidos JOIN cilindros ON cilindros_id = cilindros.id JOIN jefesf ON jefesf_id = jefesf.id WHERE jefesf.lideres_id = ? AND archivos_id IS NULL"
        if logica.consulta(queryy, [self.iDLiderCalle]):
            if resultado:
                self.cerrarAlertJornada(pageee, self.alertJornada)
                pageee.snack_bar = SnackBar(content=Text("Solo puedes generar un Reporte por Dia"))
                pageee.snack_bar.open = True
                pageee.update()
            else:
                self.alertJornada.actions.clear()
                self.textoEspera.value = "Generando Pdf, por favor espere"
                pageee.update()
                reporte.Pdf()
                self.cerrarAlertJornada(pageee, self.alertJornada)
                self.animar(self.contenedorInicio, self.contenedorInicio, pageee)
                self.cambiar_pagina(5.5)
                pageee.snack_bar = SnackBar(content=Text("Informe generado correctamente en la carpeta Reportas del escritorio"), bgcolor="GREEN")
                pageee.snack_bar.open = True
                pageee.update()
        else:
            self.cerrarAlertJornada(pageee, self.alertJornada)
            pageee.snack_bar = SnackBar(content=Text("No puedes generar el reporte sin agregar a jefes de familia a la jornada"))
            pageee.snack_bar.open = True
            pageee.update()

    def cerrarAlertJornada(self, pageeee, alert):
        pageeee = pageeee
        alert = alert

        alert.open = False

        pageeee.update()

    def cambiarTitulo(self, pagee, titulo):
        pagee = pagee
        titulo = titulo

        self.titulo.value = titulo
        pagee.update()

    def abrirHistorial(self, pagee, fechaa, idss):
        pagee = pagee
        fechaa = fechaa
        idss = idss

        self.tablaLlenarHistorial.rows = self.llenarHistroial(pagee, idss)

        #self.animar(self.contenedorLlenarHistorialJornada, self.contenedorLlenarHistorialJornada, pagee)

        self.alertHistorial = AlertDialog(
            content=Column(
                controls=[
                    Text(f"Jornada realizada el {fechaa}"),
                    Container(
                        bgcolor="white",
                        height=550,
                        border_radius=border_radius.all(7),  
                        content=Column(
                            expand=True,
                            height=550,
                            scroll=ScrollMode.ALWAYS,
                            controls=[
                                self.tablaLlenarHistorial,
                            ]
                        )
                    ),
                ]
            ),
            actions=[ElevatedButton("Descargar Pdf", on_click=lambda _:self.descargarArchivo(pagee, self.alertHistorial, idss)), ElevatedButton("Regresar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertHistorial))]
        )

        pagee.dialog = self.alertHistorial
        self.alertHistorial.open = True

        pagee.update()

    def llenarHistroial(self, pageee, ids):
        pageee = pageee
        ids = ids

        contenido = []

        queryy = "SELECT pedidos.id, jefesf.ci, jefesf.nombre, jefesf.apellido, empresas.empresa, tamanos.tamano, picos.pico, pedidos.fechaAgregada FROM pedidos JOIN jefesf ON jefesf_id = jefesf.id JOIN cilindros ON cilindros_id = cilindros.id JOIN empresas ON cilindros.empresas_id = empresas.id JOIN tamanos ON tamanos_id = tamanos.id JOIN picos ON picos_id = picos.id JOIN lideres ON lideres_id = lideres.id WHERE archivos_id = ? ORDER BY jefesf.ci ASC"
        resultado = logica.consulta(queryy, [ids])

        for idss, cii, nom, ape, empresa, tamano, pico, fech in resultado:
            contenido.append(DataRow(
                color="WHITE",
                cells=[
                    DataCell(Text(f"{cii}")),
                    DataCell(Text(f"{nom}")),
                    DataCell(Text(f"{ape}")),
                    DataCell(Text(f"{empresa}")),
                    DataCell(Text(f"{tamano}")),
                    DataCell(Text(f"{pico}")),
                    DataCell(Text(f"{fech}")),
                ],
            ),
            )

            pageee.update()

        return contenido 

    def volverGenerarArchivos(self, pagee):
        pagee = pagee

        self.bitacoraLista.clear()

        self.tablaSeleccionarHistorial.rows = self.generarArchivos(pagee)

        pagee.update()

    def generarArchivos(self, pageee):
        pageee = pageee

        his = []
        coun = 1

        resultadoId = logica.consulta("SELECT archivos_id FROM pedidos JOIN archivos ON archivos_id IS NOT NULL = archivos.id JOIN cilindros ON cilindros_id = cilindros.id JOIN jefesf ON jefesf_id = jefesf.id JOIN lideres ON lideres_id = lideres.id WHERE lideres_id = ? GROUP BY archivos_id", [self.iDLiderCalle])

        for idss in resultadoId:

            datos = logica.consulta("SELECT fechaGenerado, id FROM archivos WHERE id = ?", [idss[0]])

            self.bitacoraLista.append([datos[0][0], datos[0][1]])

        for fecha, ids in self.bitacoraLista:
            his.append(DataRow(
                color="WHITE",
                cells=[
                    DataCell(Text(f"Jornada {coun}")),
                    DataCell(Text(f"{fecha}")),
                ],
                on_select_changed=lambda _, fecha = fecha, ids = ids: [self.abrirHistorial(pageee, fecha, ids)]
            ),
            )
            coun = coun + 1

            pageee.update()

        return his
    
    def descargarArchivo(self, pageee, alertt, ids):
        pageee = pageee
        alertt = alertt
        ids = ids

        origen = logica.consulta("SELECT rutas FROM archivos WHERE id = ?", [ids])
        destino = os.path.join(os.path.join(os.environ['USERPROFILE']), rf'Desktop\Reportes')

        rutaEscritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), rf'Desktop\Reportes')

        if os.path.exists(rutaEscritorio) == True:
            pass
        else:
            os.mkdir(rutaEscritorio)

        shutil.copy(origen[0][0], destino)

        self.cerrarAlertJornada(pageee, alertt)
        pageee.snack_bar = SnackBar(content=Text("El PDF se descargo correctamente, puede visualizarlo en la caperta Reportes ubicada en el escritorio"), bgcolor="GREEN")
        pageee.snack_bar.open = True
        pageee.update()
#EDITAR DATOS DEL JEFE
    def cargarDatosJefe(self, pagee):
        pagee = pagee

        resultado = logica.consulta("SELECT jefesf.nombre, jefesf.apellido, jefesf.ci, jefesf.telefono, jefesf.correo, lideres.ubicacion FROM jefesf JOIN lideres ON lideres_id = lideres.id  WHERE jefesf.id = ?", [cedulaIdentidad])

        self.nombreJ.value = f"{resultado[0][0]}"
        self.apellidoJ.value = f"{resultado[0][1]}"
        self.cedulaJ.value = f"{resultado[0][2]}"
        self.telefonoJ.value = f"{resultado[0][3]}"
        self.correoJ.value = f"{resultado[0][4]}"
        self.ubicacionJ.value = f"{resultado[0][5]}"

        pagee.update()

#EDITAR DATOS DEL JEFE DE FAMILIA 
    def editNombre(self, pagee, campo):
        pagee = pagee
        campo = campo

        self.entryNombre = TextField(label="Nombre", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryNombre), logica.validarNombres(self.entryNombre, pagee)])
        self.entryNombre.value = campo

        self.alertEditNombre = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.entryNombre,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarNombre(pagee, self.entryNombre, "UPDATE jefesf SET nombre = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditNombre))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditNombre
        self.alertEditNombre.open = True

        pagee.update()

    def editApellido(self, pagee, campo):
        campo = campo
        pagee = pagee

        self.entryApellido = TextField(label="Apellido", hint_text="Minimo 4 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryApellido), logica.validarNombres(self.entryApellido, pagee)])
        self.entryApellido.value = campo

        self.alertEditApellido = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.entryApellido,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarApellido(pagee, self.entryApellido, "UPDATE jefesf SET apellido = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditApellido))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditApellido
        self.alertEditApellido.open = True

        pagee.update()

    def editCedula(self, pagee, tipo, cedula):
        pagee = pagee
        tipo = tipo
        cedula = cedula

        self.selectTipoCi = Dropdown(label="Tipo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.tipoCedula), options=[
                dropdown.Option("V"), dropdown.Option("E")])
        self.selectTipoCi.value = tipo
        self.entryCedula = TextField(label="Cedula", hint_text="Minimo 7 caracteres", border_color="#820000", border_radius=20, width=180, height=60, max_length=8, on_change=lambda _: [self.quitarError(pagee, self.entryCedula), logica.validarNumeros(self.entryCedula, pagee)])
        self.entryCedula.value = cedula

        self.alertEditCedula = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.selectTipoCi,
                        self.entryCedula,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarCedula(pagee, self.selectTipoCi, self.entryCedula, "SELECT jefesf.nombre, jefesf.apellido FROM jefesf WHERE jefesf.ci = ?", "UPDATE jefesf SET ci = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditCedula))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditCedula
        self.alertEditCedula.open = True

        pagee.update()

    def editCorreo(self, pagee, correo):
        pagee = pagee
        correo = correo
        direccion = ""
        tipo = ""

        if correo.value[-10:] == "@gmail.com":
            direccion = correo.value[:-10]
            tipo = correo.value[-10:]
        else:
            direccion = correo.value[:-12]
            tipo = correo.value[-12:]

        self.entryCorreo = TextField(label="Direccion", hint_text="ej: clapcamoruco", border_color="#820000", border_radius=20, width=180, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryCorreo), logica.validarCorreo(self.entryCorreo, pagee)])
        self.entryCorreo.value = direccion
        self.selectTipoCorreo = Dropdown(hint_text="Correo", color="black",border_color="#820000", border_radius=20, width=120, height=60, on_change=lambda _: self.quitarError(pagee, self.selectTipoCorreo), options=[
                dropdown.Option("@gmail.com"), dropdown.Option("@hotmail.com")])
        self.selectTipoCorreo.value = tipo

        self.alertEditCcorreo = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=2,
                    controls=[
                        self.entryCorreo,
                        self.selectTipoCorreo,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarCorreo(pagee, self.selectTipoCorreo, self.entryCorreo, "SELECT jefesf.nombre, jefesf.apellido FROM jefesf WHERE jefesf.correo = ?", "UPDATE jefesf SET correo = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditCcorreo))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditCcorreo
        self.alertEditCcorreo.open = True

        pagee.update()

    def editTelefono(self, pagee, campo):
        pagee = pagee
        campo = campo

        codigo = campo.value[:4]
        telefono = campo.value[-7:]
        #self.telefonoJ.value[:4], self.telefonoJ.value[-7:]

        self.selectTipoTelefono = Dropdown(hint_text="Codigo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(pagee, self.selectTipoTelefono), options=[
                dropdown.Option("0412"), dropdown.Option("0414"), dropdown.Option("0416"), dropdown.Option("0424"), dropdown.Option("0238")])
        self.selectTipoTelefono.value = codigo
        self.entryTelefono = TextField(label="N telefono", hint_text="0000000", border_color="#820000", border_radius=20, width=180, height=60, max_length=7, on_change=lambda _: [self.quitarError(pagee, self.entryTelefono), logica.validarNumeros(self.entryTelefono, pagee)])
        self.entryTelefono.value = telefono

        self.alertEditTelefono = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=2,
                    controls=[
                        self.selectTipoTelefono,
                        self.entryTelefono,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarTelefono(pagee, self.selectTipoTelefono, self.entryTelefono, "SELECT jefesf.nombre, jefesf.apellido FROM jefesf WHERE jefesf.telefono = ?", "UPDATE jefesf SET telefono = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditTelefono))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditTelefono
        self.alertEditTelefono.open = True

        pagee.update()

    def validarNombre(self, pageee, campo, queryy):
        pageee = pageee
        campo = campo
        queryy = queryy

        if (campo.value == "") or (len(campo.value) in range(1, 3)):
            if campo.value == "":
                campo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(campo.value) in range(1, 3):
                campo.error_text = "Minimo de caracteres 3"
                pageee.update()
        else:
            logica.consulta(queryy, [campo.value, cedulaIdentidad])
            self.volverGenerarCartas(pageee)
            self.cargarDatosJefe(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditNombre)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El nombre se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarApellido(self, pageee, campo, queryy):
        pageee = pageee
        campo = campo
        queryy = queryy

        if (campo.value == "") or (len(campo.value) in range(1, 4)):
            if campo.value == "":
                campo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(campo.value) in range(1, 4):
                campo.error_text = "Minimo de caracteres 4"
                pageee.update()
        else:
            logica.consulta(queryy, [campo.value, cedulaIdentidad])
            self.volverGenerarCartas(pageee)
            self.cargarDatosJefe(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditApellido)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El apellido se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarCedula(self, pageee, tipo, cedula, queryy, queryUpdate):
        pageee = pageee
        tipo = tipo
        cedula = cedula
        queryy = queryy
        queryUpdate = queryUpdate

        arregloCi = f"{tipo.value}-{cedula.value}"

        if (cedula.value == "") or (len(cedula.value) in range(1, 7)):
            if cedula.value == "":
                cedula.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if len(cedula.value) in range(1, 7):
                cedula.error_text = "Minimo de caracteres 7"
                pageee.update()

        elif logica.consulta(queryy, [arregloCi]):
            pageee.snack_bar = SnackBar(content=Text("Esta cedula ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloCi, cedulaIdentidad])
            self.volverGenerarCartas(pageee)
            self.cargarDatosJefe(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditCedula)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("La cedula se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarCorreo(self, pageee, tipo, correo, queryy, queryUpdate):
        pageee = pageee
        tipo = tipo
        correo = correo
        queryy = queryy
        queryUpdate = queryUpdate

        arregloCorreo = f"{correo.value}{tipo.value}"

        if (correo.value == ""):
            if correo.value == "":
                correo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

        elif logica.consulta(queryy, [arregloCorreo]):
            pageee.snack_bar = SnackBar(content=Text("Esta correo ya esta registrado"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloCorreo, cedulaIdentidad])
            self.volverGenerarCartas(pageee)
            self.cargarDatosJefe(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditCcorreo)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El correo se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarTelefono(self, pageee, codigo, telefono, queryy, queryUpdate):
        pageee = pageee
        codigo = codigo
        telefono = telefono
        queryy = queryy
        queryUpdate = queryUpdate

        arregloTelefono = f"{codigo.value}-{telefono.value}"

        if (telefono.value == "") or (len(telefono.value) in range(1, 7)):
            if telefono.value == "":
                telefono.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if len(telefono.value) in range(1, 7):
                telefono.error_text = "numero de telefono invalido"
                pageee.update()

        elif logica.consulta(queryy, [arregloTelefono]):
            pageee.snack_bar = SnackBar(content=Text("Esta numero de telefono ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloTelefono, cedulaIdentidad])
            self.volverGenerarCartas(pageee)
            self.cargarDatosJefe(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditTelefono)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El numero de telefono se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

#EDITAR DATOS DEL LIDER
    def cargarDatosLider(self, pagee):
        pagee = pagee

        resultado = logica.consulta("SELECT lideres.nombre, lideres.apellido, lideres.cedula, lideres.telefono, lideres.correo, lideres.ubicacion FROM lideres WHERE lideres.id = ?", [self.iDLiderCalle])

        self.nombreLi.value = f"{resultado[0][0]}"
        self.apellidoLi.value = f"{resultado[0][1]}"
        self.cedulaLi.value = f"{resultado[0][2]}"
        self.telefonoLi.value = f"{resultado[0][3]}"
        self.correoLi.value = f"{resultado[0][4]}"
        self.ubicacionLi.value = f"{resultado[0][5]}"

        pagee.update()

#EDITAR DATOS DEL JEFE DE FAMILIA 
    def editNombreLi(self, pagee, campo):
        pagee = pagee
        campo = campo

        self.entryNombre = TextField(label="Nombre", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryNombre), logica.validarNombres(self.entryNombre, pagee)])
        self.entryNombre.value = campo

        self.alertEditNombre = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.entryNombre,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarNombreLi(pagee, self.entryNombre, "UPDATE lideres SET nombre = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditNombre))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditNombre
        self.alertEditNombre.open = True

        pagee.update()

    def editApellidoLi(self, pagee, campo):
        campo = campo
        pagee = pagee

        self.entryApellido = TextField(label="Apellido", hint_text="Minimo 4 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryApellido), logica.validarNombres(self.entryApellido, pagee)])
        self.entryApellido.value = campo

        self.alertEditApellido = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.entryApellido,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarApellidoLi(pagee, self.entryApellido, "UPDATE lideres SET apellido = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditApellido))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditApellido
        self.alertEditApellido.open = True

        pagee.update()

    def editCedulaLi(self, pagee, tipo, cedula):
        pagee = pagee
        tipo = tipo
        cedula = cedula

        self.selectTipoCi = Dropdown(label="Tipo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.tipoCedula), options=[
                dropdown.Option("V"), dropdown.Option("E")])
        self.selectTipoCi.value = tipo
        self.entryCedula = TextField(label="Cedula", hint_text="Minimo 7 caracteres", border_color="#820000", border_radius=20, width=180, height=60, max_length=8, on_change=lambda _: [self.quitarError(pagee, self.entryCedula), logica.validarNumeros(self.entryCedula, pagee)])
        self.entryCedula.value = cedula

        self.alertEditCedula = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.selectTipoCi,
                        self.entryCedula,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarCedulaLi(pagee, self.selectTipoCi, self.entryCedula, "SELECT lideres.nombre, lideres.apellido FROM lideres WHERE lideres.cedula = ?", "UPDATE lideres SET cedula = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditCedula))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditCedula
        self.alertEditCedula.open = True

        pagee.update()

    def editCorreoLi(self, pagee, correo):
        pagee = pagee
        correo = correo
        direccion = ""
        tipo = ""

        if correo.value[-10:] == "@gmail.com":
            direccion = correo.value[:-10]
            tipo = correo.value[-10:]
        else:
            direccion = correo.value[:-12]
            tipo = correo.value[-12:]

        self.entryCorreo = TextField(label="Direccion", hint_text="ej: clapcamoruco", border_color="#820000", border_radius=20, width=180, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryCorreo), logica.validarCorreo(self.entryCorreo, pagee)])
        self.entryCorreo.value = direccion
        self.selectTipoCorreo = Dropdown(hint_text="Correo", color="black",border_color="#820000", border_radius=20, width=120, height=60, on_change=lambda _: self.quitarError(pagee, self.selectTipoCorreo), options=[
                dropdown.Option("@gmail.com"), dropdown.Option("@hotmail.com")])
        self.selectTipoCorreo.value = tipo

        self.alertEditCcorreo = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=2,
                    controls=[
                        self.entryCorreo,
                        self.selectTipoCorreo,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarCorreoLi(pagee, self.selectTipoCorreo, self.entryCorreo, "SELECT lideres.nombre, lideres.apellido FROM lideres WHERE lideres.correo = ?", "UPDATE lideres SET correo = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditCcorreo))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditCcorreo
        self.alertEditCcorreo.open = True

        pagee.update()

    def editTelefonoLi(self, pagee, campo):
        pagee = pagee
        campo = campo

        codigo = campo.value[:4]
        telefono = campo.value[-7:]
        #self.telefonoJ.value[:4], self.telefonoJ.value[-7:]

        self.selectTipoTelefono = Dropdown(hint_text="Codigo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(pagee, self.selectTipoTelefono), options=[
                dropdown.Option("0412"), dropdown.Option("0414"), dropdown.Option("0416"), dropdown.Option("0424"), dropdown.Option("0238")])
        self.selectTipoTelefono.value = codigo
        self.entryTelefono = TextField(label="N telefono", hint_text="0000000", border_color="#820000", border_radius=20, width=180, height=60, max_length=7, on_change=lambda _: [self.quitarError(pagee, self.entryTelefono), logica.validarNumeros(self.entryTelefono, pagee)])
        self.entryTelefono.value = telefono

        self.alertEditTelefono = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=2,
                    controls=[
                        self.selectTipoTelefono,
                        self.entryTelefono,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarTelefonoLi(pagee, self.selectTipoTelefono, self.entryTelefono, "SELECT lideres.nombre, lideres.apellido FROM lideres WHERE lideres.telefono = ?", "UPDATE lideres SET telefono = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditTelefono))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditTelefono
        self.alertEditTelefono.open = True

        pagee.update()

    def validarNombreLi(self, pageee, campo, queryy):
        pageee = pageee
        campo = campo
        queryy = queryy

        if (campo.value == "") or (len(campo.value) in range(1, 3)):
            if campo.value == "":
                campo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(campo.value) in range(1, 3):
                campo.error_text = "Minimo de caracteres 3"
                pageee.update()
        else:
            logica.consulta(queryy, [campo.value, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.textoSlider.value = f"{campo.value}"
            self.cargarDatosLider(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditNombre)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El nombre se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarApellidoLi(self, pageee, campo, queryy):
        pageee = pageee
        campo = campo
        queryy = queryy

        if (campo.value == "") or (len(campo.value) in range(1, 4)):
            if campo.value == "":
                campo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(campo.value) in range(1, 4):
                campo.error_text = "Minimo de caracteres 4"
                pageee.update()
        else:
            logica.consulta(queryy, [campo.value, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.apellidoLiderCalle = campo.value
            self.cargarDatosLider(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditApellido)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El apellido se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarCedulaLi(self, pageee, tipo, cedula, queryy, queryUpdate):
        pageee = pageee
        tipo = tipo
        cedula = cedula
        queryy = queryy
        queryUpdate = queryUpdate

        arregloCi = f"{tipo.value}-{cedula.value}"

        if (cedula.value == "") or (len(cedula.value) in range(1, 7)):
            if cedula.value == "":
                cedula.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if len(cedula.value) in range(1, 7):
                cedula.error_text = "Minimo de caracteres 7"
                pageee.update()

        elif logica.consulta(queryy, [arregloCi]):
            pageee.snack_bar = SnackBar(content=Text("Esta cedula ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloCi, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.cargarDatosLider(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditCedula)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("La cedula se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarCorreoLi(self, pageee, tipo, correo, queryy, queryUpdate):
        pageee = pageee
        tipo = tipo
        correo = correo
        queryy = queryy
        queryUpdate = queryUpdate

        arregloCorreo = f"{correo.value}{tipo.value}"

        if (correo.value == ""):
            if correo.value == "":
                correo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

        elif logica.consulta(queryy, [arregloCorreo]):
            pageee.snack_bar = SnackBar(content=Text("Esta correo ya esta registrado"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloCorreo, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.cargarDatosLider(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditCcorreo)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El correo se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarTelefonoLi(self, pageee, codigo, telefono, queryy, queryUpdate):
        pageee = pageee
        codigo = codigo
        telefono = telefono
        queryy = queryy
        queryUpdate = queryUpdate

        arregloTelefono = f"{codigo.value}-{telefono.value}"

        if (telefono.value == "") or (len(telefono.value) in range(1, 7)):
            if telefono.value == "":
                telefono.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if len(telefono.value) in range(1, 7):
                telefono.error_text = "numero de telefono invalido"
                pageee.update()

        elif logica.consulta(queryy, [arregloTelefono]):
            pageee.snack_bar = SnackBar(content=Text("Esta numero de telefono ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloTelefono, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.cargarDatosLider(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditTelefono)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El numero de telefono se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def salir(self, pages):
        self.pages = pages

        fechaS = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        logica.consulta("UPDATE bitacora SET fechaSalida = ? WHERE fechaEntrada = ? AND usuarios_id = ?", [fechaS, self.fechaEntradaUser, self.idUsuario])
        self.pages.go("/")
        self.cambiar_pagina(5.5)
        logica.datoUser.clear()



