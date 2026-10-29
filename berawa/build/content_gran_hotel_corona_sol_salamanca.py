# Contenido de la demo Gran Hotel Corona Sol (Salamanca) (es/ca/en/fr). Hechos de gran-hotelcoronasol.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble 2 camas','Doble matrimonial','Triple'],
'ca':['Doble 2 llits','Doble matrimonial','Triple'],
'en':['Twin room','Double room','Triple room'],
'fr':['Double 2 lits','Double lit double','Triple']}
RD={
'es':['Hasta 2 personas, 24 m², con 2 camas individuales, aire acondicionado, TV de pantalla plana, wifi gratuita, calefacción y caja fuerte.','Hasta 2 personas, con cama de matrimonio de 180 cm y las mismas comodidades que la habitación de 2 camas.','Hasta 3 personas, con cama matrimonial o twin y un sofá adicional o tercera cama.'],
'ca':['Fins a 2 persones, 24 m², amb 2 llits individuals, aire condicionat, TV de pantalla plana, wifi gratuïta, calefacció i caixa forta.','Fins a 2 persones, amb llit de matrimoni de 180 cm i les mateixes comoditats que l\'habitació de 2 llits.','Fins a 3 persones, amb llit matrimonial o twin i un sofà addicional o tercer llit.'],
'en':['Up to 2 guests, 24 m², with 2 single beds, air conditioning, flat-screen TV, free wifi, heating and a safe.','Up to 2 guests, with a 180 cm double bed and the same comforts as the twin room.','Up to 3 guests, with a double or twin bed and an additional sofa or a third bed.'],
'fr':['Jusqu\'à 2 personnes, 24 m², avec 2 lits simples, climatisation, TV à écran plat, wifi gratuit, chauffage et coffre-fort.','Jusqu\'à 2 personnes, avec lit double de 180 cm et le même confort que la chambre à 2 lits.','Jusqu\'à 3 personnes, avec lit double ou twin et un canapé supplémentaire ou un troisième lit.']}
ART={
'hero':('arches',9701,['#e8e3cf','#cdb98a','#9a7a3a','#2f5a4a','#17332a']),
'intro':('columns',9702,['#ebe6d2','#f3eedb','#c0a04a','#3b6b59','#17332a']),
'r1':('arches',9711,['#e7e2cc','#cfbb8c','#977638','#2d5645','#153027']),
'r2':('columns',9712,['#e6e1cb','#f2edda','#bd9c47','#386654','#183629']),
'r3':('skyline',9713,['#2c4a45','#e8935f','#fbd9a0','#2b4943','#1f3732','#13251f']),
'g1':('arches',9721,['#e9e4ce','#d0bc8e','#99793b','#2e5b49','#16322a']),
'g2':('skyline',9722,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g3':('columns',9723,['#e8e3cd','#f3eed9','#bf9f49','#3c6c5a','#1a382d']),
'g4':('hills',9724,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('arches',9725,['#e8e3cd','#cfba8c','#98773a','#2c5846','#153026']),
'g6':('skyline',9726,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Gran Hotel Corona Sol · Hotel de 4 estrellas en el casco histórico de Salamanca',see_rooms='Ver habitaciones',hero_k='Salamanca · Centro histórico',hero_t='En el centro histórico de Salamanca',hero_s='Un hotel de 4 estrellas a 5 minutos a pie de la Plaza Mayor, para viajes de ocio y de negocios.',
 intro_t='El corazón del casco monumental',intro_p1='El Gran Hotel Corona Sol tiene 199 habitaciones de 6 tipos y recepción 24 horas, en el centro histórico de Salamanca.',
 intro_p2='Tiene restaurante, bar-cafetería, desayuno buffet, parking cubierto privado y salón con terraza para eventos. Para reservar, contacta con el hotel por teléfono o correo.',
 stats=['4 estrellas','199 habitaciones','Recepción 24 horas','Parking cubierto privado'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Recepción 24 horas','Wifi gratuita','Parking cubierto privado','Consigna de equipajes','Accesos adaptados','Aire acondicionado','Desayuno buffet','Restaurante y bar-cafetería'],
 loc_p='Victor García de la Concha s/n, 37007 Salamanca.',
 chips=['¿Cuántas habitaciones tiene?','¿Hay parking?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Gran Hotel Corona Sol · Hotel de 4 estrelles al nucli històric de Salamanca',see_rooms='Veure habitacions',hero_k='Salamanca · Centre històric',hero_t='Al centre històric de Salamanca',hero_s='Un hotel de 4 estrelles a 5 minuts a peu de la Plaza Mayor, per a viatges d\'oci i de negocis.',
 intro_t='El cor del nucli monumental',intro_p1='El Gran Hotel Corona Sol té 199 habitacions de 6 tipus i recepció 24 hores, al centre històric de Salamanca.',
 intro_p2='Té restaurant, bar-cafeteria, esmorzar bufet, pàrquing cobert privat i saló amb terrassa per a esdeveniments. Per reservar, contacta amb l\'hotel per telèfon o correu.',
 stats=['4 estrelles','199 habitacions','Recepció 24 hores','Pàrquing cobert privat'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Recepció 24 hores','Wifi gratuïta','Pàrquing cobert privat','Consigna d\'equipatges','Accessos adaptats','Aire condicionat','Esmorzar bufet','Restaurant i bar-cafeteria'],
 loc_p='Victor García de la Concha s/n, 37007 Salamanca.',
 chips=['Quantes habitacions té?','Hi ha pàrquing?','On és?','Com es reserva?']),
'en':dict(title='Gran Hotel Corona Sol · 4-star hotel in the historic centre of Salamanca',see_rooms='See the rooms',hero_k='Salamanca · Historic centre',hero_t='In the historic centre of Salamanca',hero_s='A 4-star hotel a 5-minute walk from the Plaza Mayor, for leisure and business trips.',
 intro_t='The heart of the monumental old town',intro_p1='Gran Hotel Corona Sol has 199 rooms of 6 types and a 24-hour reception, in the historic centre of Salamanca.',
 intro_p2='It has a restaurant, a bar-café, buffet breakfast, private covered parking and a hall with a terrace for events. To book, contact the hotel by phone or email.',
 stats=['4 stars','199 rooms','24-hour reception','Private covered parking'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['24-hour reception','Free wifi','Private covered parking','Luggage storage','Adapted access','Air conditioning','Buffet breakfast','Restaurant and bar-café'],
 loc_p='Victor García de la Concha s/n, 37007 Salamanca.',
 chips=['How many rooms does it have?','Is there parking?','Where is it?','How do I book?']),
'fr':dict(title='Gran Hotel Corona Sol · Hôtel 4 étoiles dans le centre historique de Salamanque',see_rooms='Voir les chambres',hero_k='Salamanque · Centre historique',hero_t='Dans le centre historique de Salamanque',hero_s='Un hôtel 4 étoiles à 5 minutes à pied de la Plaza Mayor, pour séjours de loisirs et d\'affaires.',
 intro_t='Au cœur du centre monumental',intro_p1='Le Gran Hotel Corona Sol compte 199 chambres de 6 types et une réception ouverte 24 heures, dans le centre historique de Salamanque.',
 intro_p2='Il dispose d\'un restaurant, d\'un bar-cafétéria, d\'un petit-déjeuner buffet, d\'un parking couvert privé et d\'un salon avec terrasse pour événements. Pour réserver, contactez l\'hôtel par téléphone ou e-mail.',
 stats=['4 étoiles','199 chambres','Réception 24 heures','Parking couvert privé'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Réception 24 heures','Wifi gratuit','Parking couvert privé','Consigne à bagages','Accès adaptés','Climatisation','Petit-déjeuner buffet','Restaurant et bar-cafétéria'],
 loc_p='Victor García de la Concha s/n, 37007 Salamanque.',
 chips=['Combien de chambres a-t-il ?','Y a-t-il un parking ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='recepcion@gran-hotelcoronasol.es')
D=dict(name='Gran Hotel Corona Sol',ac='#1f4a3c',ac2='#c9a13b',ac2_a11y='#7a5c12',book=BOOK,around=[],foot=FOOT,
 address='Victor García de la Concha s/n · 37007 Salamanca',phones=['923 28 16 16'],emails=['recepcion@gran-hotelcoronasol.es'],maps='Gran Hotel Corona Sol, Victor García de la Concha, Salamanca',t=T)
META=dict(repo='demo-gran-hotel-corona-sol-salamanca',name='Gran Hotel Corona Sol',legal_name='COPITASA OESTE S.L.',registry_ids=['CIF B85399574'],
 url='https://www.gran-hotelcoronasol.es/',domain='gran-hotelcoronasol.es',municipality='Salamanca',province='Salamanca',sector='hotel de 4 estrellas en el casco histórico',
 read_at='2026-10-29T05:53:00+01:00',created_at='2026-10-29T05:54:00+01:00',built_at='2026-10-29T05:54:00+01:00',audit_date='2026-10-29T05:54:00+01:00',
 rating=dict(value=4.1,coincide=['telefono','web'],date='2026-10-29T04:55:11+01:00',url='https://www.google.com/maps/place/Gran+Hotel+Corona+Sol/@40.9690971,-5.6698331,17z/data=!4m9!3m8!1s0xd3f263d1de97e0d:0x9d4f9657c79e054c!5m2!4m1!1i2!8m2!3d40.9690971!4d-5.6698331!16s%2Fg%2F11xh8p9fj'),
 book=dict(mode='mail',email='recepcion@gran-hotelcoronasol.es',note='La web del negocio tiene su propio motor de reservas cuyo enlace no se verifica; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel con precedente en demos de esta tanda')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Qué servicios tiene el hotel?','K03'),('¿Hay parking?','K04'),('¿Hay desayuno?','K05'),('¿Tienen salones para eventos?','K06'),('¿Dónde está el hotel?','K07'),('¿Qué hay para visitar cerca?','K08'),('¿Cómo reservo?','K09'),('¿Cuál es el teléfono?','K10'),('¿Quién es el titular?','K11'),('¿Admiten mascotas?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K09'),('¿Tienen suites?',None),('¿Hay piscina?',None)],
'ca':[('Quantes habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Quins serveis té l\'hotel?','K03'),('Hi ha pàrquing?','K04'),('Hi ha esmorzar?','K05'),('Teniu salons per a esdeveniments?','K06'),('On és l\'hotel?','K07'),('Què hi ha per visitar a prop?','K08'),('Com reservo?','K09'),('Quin és el telèfon?','K10'),('Qui és el titular?','K11'),('Admeteu mascotes?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K09'),('Teniu suites?',None),('Hi ha piscina?',None)],
'en':[('How many rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('What services does the hotel have?','K03'),('Is there parking?','K04'),('Is there breakfast?','K05'),('Do you have event rooms?','K06'),('Where is the hotel?','K07'),('What is there to visit nearby?','K08'),('How do I book?','K09'),('What is the phone number?','K10'),('Who is the owner?','K11'),('Are pets allowed?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K09'),('Do you have suites?',None),('Is there a swimming pool?',None)],
'fr':[('Combien de chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Quels services propose l\'hôtel ?','K03'),('Y a-t-il un parking ?','K04'),('Y a-t-il un petit-déjeuner ?','K05'),('Avez-vous des salons pour événements ?','K06'),('Où est l\'hôtel ?','K07'),('Que visiter à proximité ?','K08'),('Comment réserver ?','K09'),('Quel est le téléphone ?','K10'),('Qui est le titulaire ?','K11'),('Les animaux sont-ils admis ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K09'),('Avez-vous des suites ?',None),('Y a-t-il une piscine ?',None)]}
