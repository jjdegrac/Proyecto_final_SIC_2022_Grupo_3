import json


def save_json(datos):
    data_file = open("intent.json", "w")
    json.dump(datos, data_file, indent=4)


def start_intents():

    library = {"intents":
           [
               {"tag": "saludos",
                "patterns": ["hola",
                             "buenos dias",
                             "buenas tardes",
                             "buenas noches",
                             "como estas",
                             "hay alguien ahi?",
                             "hey",
                             "saludos",
                             "que tal"
                             ],
                "responses":["hola soy Uni-BOT , tu asistente virtual universitario, ¿en que puedo ayudarte?"
                             ]
                },

               {"tag": "admision",
                "patterns": ["admision",
                             "Cual es proceso de admision",
                             "Como funciona proceso de admision",
                             "que pasos deben seguir para admision",
                             "como ingreso a la universidad",
                             "Como hago la admision",
                             "como inicio el procesos de admision",
                             "informacion sobre admision"
                             ],

                "responses":["Los pasos para seguir el proceso de admisión son los siguientes:\nPaso 1: Realizar la Inscripción en Línea.\nPaso 2: Pagar la Prueba de Ubicación.\nPaso 3: Participar en la Aplicación de la Prueba de Ubicación.\nPaso 4: Consultar Resultados.\nPaso 5: Pagar la Prueba de Inglés, solo los aspirantes a las carreras de Aviación y la carrera de Licenciatura  en Comunicación Ejecutiva Bilingüe\nPaso 6: Matricular el Programa de Verano.\n\nPara más información, ingrese al siguiente enlace https://utp.ac.pa/proceso-de-admision"]
                },

                {"tag": "ofertaAcademica",
                "patterns": ["oferta academica",
                             "carreras disponibles",
                             "carreras existen",
                             "puedo estudiar en la utp",
                             "estudiar universidad",
                             "oferta academica de la universidad",
                             "informacion sobre las carreras",
                             "quisiera estudiar en la utp",
                             "ir a universidad",
                             "carreras existentes",
                             "estudios utp"                           
                             ],

                "responses":["""Si desea conocer la variedad de carreras que existen en la UTP, haga click en el siguiente enlace para acceder al panorama total de la oferta académica de la UTP https://utp.ac.pa/oferta-academica-de-la-utp"""]
                },

                {"tag": "calendario",
                "patterns": ["calendario de clases",
                             "dias libres",
                             "feriados",
                             "no hay clases",
                             "dias sin clases",
                             "oferta academica de la universidad",
                             "eventos importantes"              
                             ],

                "responses":["""Si desea conocer sobre el cronograma, fechas y eventos importantes concernientes a la universidad, en el siguiente enlace puede acceder a los calendarios académicos, de matrícula,etc. https://utp.ac.pa/calendario-academico"""]
                },

               {"tag": "Inscripcion",
                "patterns": ["inscripcion",
                             "donde  inscribo",
                             "como  inscribo",
                             "inscribo en la universidad",
                             "proceso de inscripcion en linea",
                             "que hago para inscribirme",
                             "informacion sobre inscripcion",
                             "info inscripcion"
                             ],
                "responses":["Todo estudiante que aspire a realizar la Prueba de Ubicación debe inscribirse.\nRealice la inscripción en: http://matricula.utp.ac.pa/siu/paso1.aspx.\nPara más información sobre el proceso de inscripción, haga click en el siguiente enlace https://utp.ac.pa/proceso-de-admision "
                             ]
                },

               {"tag": "Costos",
                "patterns": ["Cuanto cuesta examenes",
                             "Cuanto cuesta inscripcion",
                             "cuesta prueba",
                             "Costo",
                             "Costo prueba ingreso",
                             "Costo  admisión",
                             "cuesta el examen de ingreso",
                             "costo  prueba ",
                             "cuanto debo pagar para prueba",
                             "cuanto se paga para inscripcion",
                             "pagar prueba",
                             "pagan examenes",
                             "paga la inscripcion",
                             "informacion sobre costos de prueba",
                             "info sobre pagar prueba",
                             "cuanto cuesta"
                             ],
                "responses":["Los costos de las pruebas de admisión son los siguientes:\nPago de la Prueba de Ubicación (B/. 30.00)\nPago de la Prueba de Inglés (B/. 15.00)\nPago de la Prueba Psicológica (B/. 10.00).\n\nLa Prueba de Ubicación se paga de forma presencial en las cajas de la UTP de acuerdo a la CITA DE PAGO que se le proporcionó al completar su inscripción.\n\nLa Prueba de Ubicación se paga de forma presencial en las cajas de la UTP de acuerdo a la CITA DE PAGO que se le proporcionó al completar su inscripción."
                             ]
                },

               {"tag": "PruebaDeUbicacion",
                "patterns": ["donde prueba",
                             "cuando prueba",
                             "donde examen",
                             "cuando examen",
                             "cuando es la convocatoria",
                             "donde es la convocatoria",
                             "fecha prueba",
                             "hora prueba",
                             "fecha examen",
                             "hora examen",
                             "devolucion de dinero de la prueba",
                             "cuando la prueba de admision",
                             "reembolso dinero",
                             "que dia es la prueba o examen",
                             "dia de prueba",
                             "dia de examen"
                             ],
                "responses":['Debe asistir a la Prueba de Ubicación en la fecha y hora que indica su recibo de pago, de lo contrario, perderá su prueba, pero podrá aplicar para la convocatoria siguiente, realizando el pago correspondiente. La UTP no hará devolución del dinero si no asiste en la fecha y hora programada.\n\nPara conocer la fecha y hora de la aplicación de su prueba, ingrese al sistema de matrícula: matricula.utp.ac.pa, introduzca su cédula, contraseña y haga clic en "Buscar Aula". Para mayor informacion ingrese a https://www.utp.ac.pa/informacion-sobre-las-pruebas'
                             ]
                },

               {"tag": "resultadosPrueba",
                "patterns": [
                    "entrega resultados de las pruebas de admision",
                    "recojer resultados de las pruebas",
                    "que dia entregan examenes",
                    "se entrega de notas",
                    "que se entregan notas",
                    "resultados de las notas",
                    "saque en las pruebas",
                    "quiero ver resultados de prueba",
                    "puntaje pruebas",
                    "calificacion examen"
                  ],
                "responses":['El resultado de la Prueba de Ubicación se publica a los 15 días calendario, posteriores a la fecha de aplicación de esta prueba. Para ver sus resultados, ingrese a matricula.utp.ac.pa , introduzca su cédula, contraseña y haga clic en la opción del menú "Consultar Resultados".'
                             ]
                },

               {"tag": "matricula",
                "patterns": ["matricula",
                             "como matriculo",
                             "como matricula",
                             "procedimiento matricula",
                             "como matriculo pagina web",
                             "informacion sobre la matricuka",
                             "donde me matriculo",
                             "info sobre matricula",
                             "informacion de la matricula"
                             ],
                "responses":["En el siguiente enlace, se le explica de forma detallada el procedimiento para completar la matrícula del estudiante https://utp.ac.pa/pasos-para-la-matricula-regular-de-la-utp"
                             ]
                },

               {"tag": "olvidarContrasena",
                "patterns": ["olvide mi contraseña",
                             "olvido la contraseña",
                             "perdi mi contraseña",
                             "donde consigo una contraseña",
                             "olvide mi contraseña",
                             "olvide mi clave",
                             "se me perdio mi clave de inscripcion",
                             "perdi mi contraseña de inscripcion",
                             "donde consigo la clave de la cuenta",
                             ],
                "responses":["Si ha perdido u olvidado su clave de inscripción, deberá enviar un correo a su sede correspondiente con su nombre y número de cédula solicitando su clave de inscripción. A continuación se le brinda los correos electronicos de las distintas sedes UTP:\n-Panamá siu.panama@utp.ac.pa\n-Bocas del Toro siu.bocasdeltoro@utp.ac.pa\n-Azuero siu.azuero@utp.ac.pa\n-Chiriquí siu.chiriqui@utp.ac.pa\n-Coclé siu.cocle@utp.ac.pa\n-Colón siu.colon@utp.ac.pa\n-Panamá Oeste siu.panamaoeste@utp.ac.pa\n-Veraguas siu.veraguas@utp.ac.pa"]
                },

                {"tag":"reprobarAdmision",
                 "patterns":["no aprobe",
                             "reprobe la prueba",
                             "no paso debo inscribirme de nuevo",
                             "no pase admision",
                             "debo volver inscribirme",
                             "falle prueba",
                             "fracase prueba",
                             "no obtuve puntaje suficiente",
                             "no asisti prueba de admision",
                             "no tengo puntaje necesario para la prueba"                      
                             ],
                 "responses":["Si no pudo aprobar en la primera convocatoria,No debe volver a inscribirse, ya que sus datos quedan guardados en el sistema, al momento en que realizó su inscripción para realizar la prueba en la Primera Convocatoria. En caso de que vaya a reintentar la prueba de admisión en el próximo año, debe volver a inscribirse y es obligatorio que cumpla con todo el Proceso de Admisión. La inscripción solo es válida para el año en que presenta la prueba"
                             ]
                 },

                 {"tag":"cambiarInscripcion",
                 "patterns":["Cambiar opciones de matricula",
                             "corregir inscripcion",
                             "cambiar de carrera",
                             "corregir inscripcion",
                             "modificar datos de incripcion",
                             "cambiar datos de carrera",
                             "modificar datos de carrera"                    
                             ],
                 "responses":["Podra cambiar datos relacionados con su inscripción inicial hasta un mes antes de que culmine sus clases del periodo de verano."
                             ]
                 },

                 {"tag":"Convalidar",
                 "patterns":["Quisiera convalidar creditos",
                             "quiero convalidar materias",
                             "soy otra universidad",
                             "convalidar creditos otra universidad" ,
                             "convalidar carrera",
                             "universidad privada"                   
                             ],
                 "responses":["Puede encontrar información al respecto en el siguiente enlace http://www.utp.ac.pa/sites/default/files/documentos/2020/pdf/utp-req-convalidacion-4.pdf"
                             ]
                 },


               {"tag": "ingMecanica",
                "patterns": ["ingeneria mecanica",
                             "ing mecanica",
                             "ingeniero mecanico", 
                             "que hace un ing mecanico",
                             "de que trata la ing mecanica",
                             "mecanico"                             
                             ],
                "responses":["El Licenciado en Ingeniería Mecánica será capaz de enfrentarse al reto tecnológico en todo momento en el ámbito nacional e internacional, que tenga actitud científica; de autorrealización y la habilidad de diseñar, construir, instalar, operar, mantener y reparar todo tipo de sistemas-equipos-componentes mecánicos. Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-ingenieria-mecanica"
                             ]
                },

                {"tag": "ingMantenimiento",
                "patterns": ["mantenimiento",
                             "hacer mantenimiento"
                             ],
                "responses":["La carrera de Licenciatura en Ingeniería de Mantenimiento, tiene como fin formar un profesional capaz de enfrentarse al reto del avance tecnológico en todo momento en el ámbito nacional e internacional, que tenga una actitud científica; de autorrealización; y la habilidad de construir, instalar, operar, mantener y reparar todo tipo de sistemas-equipos-componentes mecánicos.Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-ingenieria-de-mantenimiento"
                             ]
                },

                {"tag": "ingNaval",
                "patterns": ["ing naval",
                             "ingenieria naval",
                             "hacer barcos",
                             "reparar barcos",
                             "buques",
                             "astillero",
                             "bote"
                             ],
                "responses":["El Licenciado en Ingeniería Naval se ocupa del diseño, planificación, proyecto y construcción de toda estructura flotante. La ingeniería naval abarca las funciones de ingeniería incluyendo el proyecto creativo del buque y artefactos flotantes, la investigación aplicada, el desarrollo técnico en los campos de diseño, construcción y la administración de los centros de producción de material flotante (astilleros). Así como también del mantenimiento y reparación de estos. Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-ingenieria-naval"
                             ]
                },

                {"tag": "ingAero",
                "patterns": ["ing aeronautica",
                             "que es la ing aeronautica",
                             "ingenieria aeronautica",
                             "ing aeronautica",
                             "aeroespacial",
                             "aviones"
                             ],
                "responses":["La carrera de Licenciatura en Ingeniería Aeronáutica, tiene como meta formar profesionales con fundamentos esenciales para desempeñarse como parte de los equipos a cargo del diseño y mantenimiento de aeronaves y sus sistemas de apoyo, tales como estructuras, motores, instrumentos, sistemas de control, de navegación y comunicación, de aterrizaje, de acondicionamiento de cabina y de protección. Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-ingenieria-aeronautica"
                             ]
                },

                {"tag": "ingEnergia",
                "patterns": ["ing de energia y ambiente",
                             "energia y ambiente",
                             "ingenieria de energia y ambiente",
                             "energia y ambiente",
                             "energias renovables",
                             "energias limpias",
                             "energia solar"
                             "energia geotermica",
                             "hidroelectrica",
                             "mareomotriz",
                             "undimotriz",
                             "eolica"
                             ],
                "responses":["El Ingeniero de Energía y Ambiente es un profesional con conocimientos técnicos y teóricos para el diseño y operación de sistemas de eficiencia energética, incluyendo la incorporación de fuentes renovables de energía y criterios de sostenibilidad ambiental. Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-ingenieria-de-energia-y-ambiente"
                             ]
                },

                {"tag": "ingMecInd",
                "patterns": ["mecanica industrial",
                             "reparar maquinas",
                             "tecnico de maquinas",
                             "mecanica industrial",
                             "de que trata la mecanica industrial",
                             "licenciatura en mecanica",
                             "arreglar aparatos",
                             "arreglar maquinas",
                             "maquinaria industrial",
                             "equipo pesado",
                             ""
                             ],
                "responses":["La carrera de Licenciatura en Mecánica Industrial tiene como meta formar profesionales con la veracidad de atender las áreas Tecnológicas de la Mecánica Industrial. Esto se logra del entrenamiento sistemático en la aplicación racional y empírica de los procedimientos de diseño, proyección instalación, fabricación, mantenimiento y reparación de equipos e instalaciones mecánicas. Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-mecanica-industrial"
                             ]
                },

                {"tag": "refrigeracion",
                "patterns": ["refrigeracion",
                             "aire acondicionado",
                             "refrigeracion y aire acondicionado",
                             "refrigeracion",
                             "aire acondicionado",
                             "enfriamiento",
                             "cuartos frios",
                             "congeladores",
                             "congelar",
                             "enfriar",
                             "instalar aire acondicionado",
                             "poner aires",
                             "estudiar instalar poner aire acondicionado"                        
                             ],
                "responses":["La carrera de Licenciatura en Refrigeración y Aire Acondicionado tiene la finalidad en formar un profesional capaz de enfrentarse al reto del avance tecnológico en todo momento en el ámbito nacional e internacional, que tenga una actitud científica; de autorrealización; y habilidad de diseñar, construir, instalar, operar, mantener, y reparar todo tipo de sistema de aire acondicionado y refrigeración. Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-refrigeracion-y-aire-acondicionado"
                             ]
                },

                {"tag": "automotriz",
                "patterns": ["licenciatura en  automotriz",
                             "que es  automotriz",
                             "automotriz",
                             "que hace un  automotriz",
                             "reparacion de carros",
                             "mecanico de carros",
                             "reparacion de autos",
                             "carrera de reparacion de autos",
                             "reparacion de autos",
                             "coches",
                             "automoviles",
                             "arreglar o reparar carros,autos,coches"
                             ],
                "responses":["La carrera de Licenciatura en Mecánica Automotriz, tiene la finalidad de formar un profesional capaz de enfrentarse al reto del avance tecnológico en todo momento en el ámbito nacional e internacional, que tenga actitud científica, de autorrealización y la habilidad de reparar, mantener e instalar todo tipo de sistema automotriz. Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-mecanica-automotriz"
                             ]
                },

                {"tag":"soldadura",
                 "patterns":["soldadura",
                             "licenciatura soldadura",
                             "que trata soldadura",
                             "como suelda",
                             "soldador",
                             "soldar",
                             "como soldar"
                             ],
                 "responses":["La Carrera de Licenciatura en Soldadura cumple con los requisitos necesarios para que el profesional egresado pueda optar a la certificación de Técnico Internacional en Soldadura de acuerdo a las normas del IIW",
                 "ha sido un placer, vuelva pronto.Va dirigida a todos que desarrollen o pretendan desarrollar su actividad profesional en empresas donde la soldadura forme parte de sus procesos de trabajo.Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-soldadura"
                             ]
                 },

                 {"tag":"piloto",
                 "patterns":["piloto",
                             "piloto de avion",
                             "opcion a vuelo (piloto)",
                             "carrera de piloto de avion",
                             "manejar avion",
                             "pilotar aeronaves",
                             "volar aviones"
                             ],
                 "responses":["La Licenciatura en Administración de Aviación con Opción a Vuelo Forma profesionales con vasto conocimiento de administración de empresas de aviación, en paralelo con el entrenamiento de piloto en cumplimiento con los estándares de las regulaciones vigentes.Para más información sobre la carrera ingrese al siguiente enlance https://fim.utp.ac.pa/licenciatura-en-administracion-de-aviacion-con-opcion-vuelo"
                             ]
                 },

                 {"tag":"despachoVuelo",
                 "patterns":["despacho vuelo",
                             "tecnico en despacho de vuelo",
                             "preparacion vuelos",
                             "dirigir aviones",
                             "administrar aviones",
                             "preparacion de vuelos"
                             ],
                 "responses":["La carrera de Técnico en Despacho de Vuelo busca formar técnicos capacitados para atender la logística relacionada a la preparación de los vuelos, tomando en consideración todas las normas de vuelo y seguridad operacional establecidas y estándares operacionales."
                             ]
                 },

                 {"tag":"mantMotor",
                 "patterns":["aeronaves",
                             "aviones",
                             "aeronaves",
                             "reparacion de aviones",
                             "Mantenimiento de Aeronaves con Especialización en Motores y Fuselajes"
                             ],
                 "responses":["La carrera de Técnico en Ingeniería de Mantenimiento de Aeronaves con Especialización en Motores y Fuselajes tiene el objetivo de formar profesionales capacitados para trabajar en estaciones reparadores de aviones y que adquieran conocimientos generales de técnico en mantenimiento de sistemas, motores y estructuras de las aeronaves."
                             ]
                 },

                 {"tag":"despedidas",
                 "patterns":["chao",
                             "adios",
                             "hasta luego",
                             "nos vemos",
                             "bye",
                             "hasta pronto",
                             "hasta la proxima"
                             ],
                 "responses":["hasta luego, tenga un buen dia",
                 "ha sido un placer, vuelva pronto"
                             ]
                 },
             

                
               {"tag": "agradecimientos",
                "patterns": ["gracias",
                             "muchas gracias",
                             "mil gracias",
                             "muy amable",
                             "se lo agradezco",
                             "fue de ayuda",
                             "gracias por la ayuda",
                             "muy agradecido",
                             "   gracias por su tiempo",
                             "ty"
                             ],
                "responses":["de nada",
                             "feliz por ayudarlo",
                             "gracias a usted",
                             "estamos para servirle",
                             "fue un placer"
                             ]
                },
               {"tag": "norespuesta",
                "patterns": [""],
                "responses":["no se detecto una respuesta"
                             ]
                }
           ]
           }
    save_json(library)


# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':
    start_intents()
    '''También podemos hacer comentarios multilíneas con comillas simples.'''
