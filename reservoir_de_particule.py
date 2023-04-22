from tkinter import *
import os
from random import *
from math import *

MaLargeur=400
MaHauteur=230
VitesseMaxBalleX=7
VitesseMaxBalleY=7

RayonMaximum=15 
RayonMinimum=5 
VitesseAnimation=30


PausePlay="play"
AffEcTotEffEcTot="EffEcTot"
AffEcBalEffEcBal="EffEcBal"
ListeCouleur=['red','green','yellow','blue','maroon','violet','orange','white','black','cyan','yellow']
IndiceListeBalle=0
MaxNombreBalle= 30
ListeEnergieCinetiqueTotale=[]
ListeBalle=[]*MaxNombreBalle
temps=0
DisMoyeChocGlob=0

def MiseAJourEnergieCinetiqueBalle(Balle) :
	Balle[7]=((pi*Balle[4]*Balle[4])/2)*((Balle[2]*Balle[2])+(Balle[3]*Balle[3]))

def CalculEnergieCinetiqueGloble():
	TotalEC=0
	if len(ListeBalle)>=1 :
		for Balle in ListeBalle :
			TotalEC=Balle[7]+TotalEC		
	ListeEnergieCinetiqueTotale.append(TotalEC)

def CalculDistanceMoyeneChocGlobale() :
	global DisMoyeChocGlob
	DisTotale=0
	Occurence=0
	for i in ListeBalle :
		for d in i[10] :
			DisTotale+=d
			Occurence+=1
	Occurence-=len(ListeBalle)
	DisMoyeChocGlob=round(DisTotale/Occurence,3)

def RayonMoyenConvertisMM ():
	r=0
	i=0
	for balle in ListeBalle:
		i+=1
		r+=balle[4]
	return round(r/i/50*22,1)

def CentreComparaison(X,Y):
	Verif="Pas De Conflit"
	if len(ListeBalle)>=2:
		for BalleImob in  ListeBalle :
			if BalleImob[0]+(2*RayonMaximum)>= X >=BalleImob[0]-(2*RayonMaximum)  and			 BalleImob[1]+(2*RayonMaximum)>= Y >=BalleImob[1]-(2*RayonMaximum)  :
				Verif = "Conflit"	
	return Verif

def TestColision(BalleMob) :
	global temps
	Colision="NoColision"
	numeroBalleChoke="none"
	for BalleImob in ListeBalle  :
		if BalleImob != BalleMob :
			DistanceCentreBalle=sqrt(((BalleMob[0]-BalleImob[0])*(BalleMob[0]-BalleImob[0]))+((BalleMob[1]-BalleImob[1])*(BalleMob[1]-BalleImob[1])))
			SommeRayon=BalleMob[4]+BalleImob[4]
			if DistanceCentreBalle <= SommeRayon :
				numeroBalleChoke=BalleImob[5]-1
				Modifierlistedestempsetdistance(BalleMob,BalleImob)
				CalculDistanceMoyeneChocGlobale()
				Colision="Colision"
	return[Colision,numeroBalleChoke,BalleMob[5]-1]

def Modifierlistedestempsetdistance(BalleMob,BalleImob) :
	sommetemp1=0
	sommetemp2=0
	for i in BalleMob[11] :
		sommetemp1+=i
	for i in BalleImob[11] :
		sommetemp2+=i	
	BalleMob[11].append(round(temps-sommetemp1,2))
	BalleImob[11].append(round(temps-sommetemp2,2))
	VMob=sqrt((BalleMob[2]*BalleMob[2])+(BalleMob[3]*BalleMob[3]))
	VImob=sqrt((BalleImob[2]*BalleImob[2])+(BalleImob[3]*BalleImob[3]))
	BalleMob[10].append(round(VMob*BalleMob[11][len(BalleMob[11])-1],2))
	BalleImob[10].append(round(VImob*BalleImob[11][len(BalleImob[11])-1],2))

def MouvementBalleGlobal() :
	for BalleMob in ListeBalle :
		BougerUneBalle(BalleMob)
	CalculEnergieCinetiqueGloble()

def BougerUneBalle(BalleMob) :
	V1=sqrt((BalleMob[2]*BalleMob[2])+(BalleMob[3]*BalleMob[3]))
	NouveauX=BalleMob[0]+BalleMob[2]
	NouveauY=BalleMob[1]+BalleMob[3]
	AncienX=BalleMob[0]
	AncienY=BalleMob[1]
	BalleMob[0]=NouveauX
	BalleMob[1]=NouveauY
	FaireUnTestColision=TestColision(BalleMob)
	if FaireUnTestColision[0]=="Colision":	
		Vx1=BalleMob[2]
		Vx2=ListeBalle[FaireUnTestColision[1]][2]
		Vy1=BalleMob[3]
		Vy2=ListeBalle[FaireUnTestColision[1]][3]
		M1=BalleMob[6]
		M2=ListeBalle[FaireUnTestColision[1]][6]
		V1=sqrt((Vx1*Vx1)+(Vy1*Vy1))
		V2=sqrt((Vx2*Vx2)+(Vy2*Vy2))
		BalleMob[2]=(((M1-M2)/(M1+M2))*Vx1)+(((M2+M2)/(M1+M2))*Vx2)
		BalleMob[3]=(((M1-M2)/(M1+M2))*Vy1)+(((M2+M2)/(M1+M2))*Vy2)
		ListeBalle[FaireUnTestColision[1]][2]=(((M2-M1)/(M1+M2))*Vx2)+(((M1+M1)/(M1+M2))*Vx1)
		ListeBalle[FaireUnTestColision[1]][3]=(((M2-M1)/(M1+M2))*Vy2)+(((M1+M1)/(M1+M2))*Vy1)
		NouveauX=AncienX
		NouveauY=AncienY
		BalleMob[0]=NouveauX
		BalleMob[1]=NouveauY	
	if NouveauY-BalleMob[4]<=0 or NouveauY+BalleMob[4]>=MaHauteur:
		NouveauY=BalleMob[1]-BalleMob[3]
		BalleMob[3]*=-1
	if NouveauX-BalleMob[4]<=0 or NouveauX+BalleMob[4]>=MaLargeur:
		NouveauX=BalleMob[0]-BalleMob[2]
		BalleMob[2]*=-1
	BalleMob[0]=NouveauX
	BalleMob[1]=NouveauY
	MiseAJourEnergieCinetiqueBalle(BalleMob)
	myCanvas.coords(BalleMob[5],\
                    BalleMob[0]-BalleMob[4],\
										BalleMob[1]-BalleMob[4],\
                    BalleMob[0]+BalleMob[4],\
										BalleMob[1]+BalleMob[4])

def CreerUneBalle() :
	global IndiceListeBalle
	dx=randint(-VitesseMaxBalleX,VitesseMaxBalleX)
	dy=randint(-VitesseMaxBalleY,VitesseMaxBalleY)
	while dx==0 or dy==0 :
		dx=randint(-VitesseMaxBalleX,VitesseMaxBalleX)
		dy=randint(-VitesseMaxBalleY,VitesseMaxBalleY)
	global ListeCouleur
	color=choice(ListeCouleur)
	rayon = randint(RayonMinimum,RayonMaximum)
	centreX=randint(0+rayon,MaLargeur-rayon)
	centreY=randint(0+rayon,MaHauteur-rayon)
	while CentreComparaison(centreX,centreY) == "Conflit": 
		centreX=randint(0+rayon,MaLargeur-rayon)
		centreY=randint(0+rayon,MaHauteur-rayon)
	centre = [centreX,centreY]
	EnergieCinetique = ((pi*rayon*rayon)/2)*((dx*dx)+(dy*dy))
	QuantiteDeMouvement = ((pi*rayon*rayon)/2)*sqrt((dx*dx)+(dy*dy))
	b=[centreX,centreY,dx,dy,rayon]
	b.append(myCanvas.create_oval(centre[0]-rayon,centre[1]-rayon,centre[0]+rayon,centre[1]+rayon,width=1,fill=color))
	b.append(pi*rayon*rayon)
	b.append(EnergieCinetique)
	b.append(QuantiteDeMouvement)
	b.append(color)
	b.append([0])
	b.append([0])
	ListeBalle.append([0])
	ListeBalle[IndiceListeBalle]=b
	IndiceListeBalle+=1

def Quitter():
	MaFenetre1.destroy()

def SwithPausePlay() :
	global PausePlay	
	if PausePlay== "play" :
		PausePlay="pause"
	else:
		PausePlay="play"

def FaireUneSauvegarde () :
	global PausePlay
	PausePlay="pause"
	open('Save.txt','w').close()
	Fichier=open("Save.txt",'a')

def AffichageEnergieCinetiqueTotale():
	global TexteEnergieCinetiqueTolate,ListeEnergieCinetiqueTotale
	TexteEnergieCinetiqueTolate.destroy()
	TexteEnergieCinetiqueTolate= Label(CanvasTexteEnergicinetiqueTotale,text=str(round(ListeEnergieCinetiqueTotale[len(ListeEnergieCinetiqueTotale)-1],2)))
	TexteEnergieCinetiqueTolate.pack(side=BOTTOM)

def AffichageEnergieCinetiqueDesBalles():
	for Balle in ListeBalle:
		print("Ec Balle "+Balle[9]+" = "+str(round(Balle[7],2)))
	
def ChangerLeTemps () :
	global temps,TexteValeurTemp,IndiceListeBalle
	if IndiceListeBalle !=0 :
		temps+=0.0425
		TexteValeurTemp.destroy()
		TexteValeurTemp= Label(myCanvasValeurTemps,text=str(round(temps,2)))
		TexteValeurTemp.pack()

def AffichageDistanceMoyene ():
	print("Les Balles Parcourent en moyene "+str(DisMoyeChocGlob/2)+" cm entre chaque chocs")
	if len(ListeBalle)<=1:
		print("il y as "+str(len(ListeBalle))+" balle")
	else :
		print("il y as "+str(len(ListeBalle))+" balles de rayon moyen de "+str(RayonMoyenConvertisMM())+" mm")
	
			
def animation():
	if PausePlay== "play" :
		os.system('clear')
		ChangerLeTemps()
		MouvementBalleGlobal()
		AffichageEnergieCinetiqueTotale()
		AffichageEnergieCinetiqueDesBalles()
		AffichageDistanceMoyene()
	MaFenetre1.after(VitesseAnimation,animation)	

MaFenetre1=Tk()                   
MaFenetre1.title('Réservoir Particule')
MaFenetre1.geometry(str((MaLargeur+150))+'x'+str((MaHauteur+170)))

myCanvas=Canvas(MaFenetre1,bg='dark grey',height=MaHauteur,width=MaLargeur)
myCanvasTemp=Canvas(MaFenetre1,height=10,width=100)
myCanvasValeurTemps=Canvas(MaFenetre1,height=10,width=100)
CanvasTexteEnergicinetiqueTotaleText=Canvas(MaFenetre1,height=10,width=100)
CanvasTexteEnergicinetiqueTotale=Canvas(MaFenetre1,height=10,width=100)

TexteTempEnSeconde=Label(myCanvasTemp,text="Temps (en seconde) : ")
TexteEnergieCinetiqueTolateNom=Label(CanvasTexteEnergicinetiqueTotaleText,text="Ec Totale = ")
TexteValeurTemp=Label(myCanvasTemp,text="0")
TexteEnergieCinetiqueTolate=Label(CanvasTexteEnergicinetiqueTotale,text=" 0 ")

bouEnregistrer=Button(MaFenetre1,text='Enregistrer',command=FaireUneSauvegarde)
bouPausePlay=Button(MaFenetre1,text='Play/Pause',command=SwithPausePlay)
bouAjout=Button(MaFenetre1,text='Ajouter Une Balle',bg="green",command=CreerUneBalle)
bouQuit=Button(MaFenetre1,bg="red",text='Quitter',command=Quitter)

bouAjout.pack(side=TOP)
bouPausePlay.pack(side=TOP)
myCanvasTemp.pack(side=TOP)
myCanvasValeurTemps.pack(side=TOP)
myCanvas.pack(side=TOP)
TexteTempEnSeconde.pack(side=TOP)
TexteValeurTemp.pack(side=TOP)
bouEnregistrer.pack(side=LEFT)

bouQuit.pack(side=BOTTOM)
CanvasTexteEnergicinetiqueTotale.pack(side=RIGHT)
CanvasTexteEnergicinetiqueTotaleText.pack(side=RIGHT)


TexteEnergieCinetiqueTolateNom.pack()

animation()

MaFenetre1.mainloop()
