# encoding: utf-8

''' 
Simulador de cibercafé
Modo de uso: TP6.py <G> <W>
Donde G y W son variables de control:
 G: cantidad de máquinas para juegos (gaming PCs)
 W: cantidad de estaciones de trabajo (workstations)
'''

import sys, random
HV = float("inf")

def VariablesDeControl():
	global G, W

	try:
		if len(sys.argv) == 3:
			G = int(sys.argv[1])
			W = int(sys.argv[2])
		else:
			G = int(raw_input('G='))
			W = int(raw_input('W='))
	except ValueError:
		print 'Error: G y W deben ser valores enteros.'
		exit(1)

def CondicionesIniciales():
	global T, TF, TPLL, TPSW, TPSG, NSW, NSG, CLL, \
			ITOW, ITOG, STOW, STOG, CARRW, CARRG

	T = 0
	TF = 10000 # 13140000

	TPLL = 0
	TPSW = [HV for _ in xrange(W)]
	TPSG = [HV for _ in xrange(G)]

	NSW = NSG = CLL = 0

	ITOW = [0 for _ in xrange(W)]
	ITOG = [0 for _ in xrange(G)]

	STOW = ITOW[:]
	STOG = ITOG[:]

	CARRW = CARRG = 0

def MinTPSWorker():
	return TPSW.index(min(TPSW))

def MinTPSGamer():
	return TPSG.index(min(TPSG))

def HVTPS(TPS):
	return TPS.index(HV)

def GenerarIA():
	R = random.random()
	IA = int((R * 1000) % 30)
	return IA

def GenerarTA():
	R = random.random()
	TA = int(10 + (R * 500) % 120)
	return TA

def ArrepentimientoWorker():
	global NSW, W
	return NSW - W > 3

def ArrepentimientoGamer():
	global NSG, G
	return NSG - G > 5

def EntraWorker():
	global NSW, CLL, W, T, TPSW, STOW, ITOW
	NSW += 1
	CLL += 1
	if W > NSW:
		i = HVTPS(TPSW)
		TA = GenerarTA()
		TPSW[i] = T + TA
		STOW[i] += T - ITOW[i]

def Worker():
	global NSW, W, NSG, G
	if NSW >= W:
		if NSG < G:
			R = random.random()
			if R < 0.15:
				Gamer()
			else:
				ARR = ArrepentimientoWorker()
				if not ARR:
					EntraWorker()
		else:
			ARR = ArrepentimientoWorker()
			if not ARR:
				EntraWorker()
	else:
		EntraWorker()

def Gamer():
	global NSG, CLL, G, T, TPSG, STOG, ITOG
	ARR = ArrepentimientoGamer()
	if not ARR:
		NSG += 1
		CLL += 1
		if G > NSG:
			i = HVTPS(TPSG)
			TA = GenerarTA()
			TPSG[i] = T + TA
			STOG[i] += T - ITOG[i]


def LlegaCliente():
	global T, TPLL
	T = TPLL
	IA = GenerarIA()
	TPLL = T + IA

	R = random.random()
	if R < 0.7:
		Gamer()
	else:
		Worker()

def Sale(TPS, i, NS, M, ITO):
	global T
	T = TPS[i]
	NS -= 1

	if NS < M:
		ITO[i] = T
		TPS[i] = HV
	else:
		TA = GenerarTA()
		TPS[i] = T + TA

def ImprimirResultados():
	pass
	# TODO
	# PPS = SPS * 1.0 / CLL
	# PTO = [ e * 100.0 / T for e in STO ]
	# PPA = CANTARREP * 100.0 / (CLL + CANTARREP)

	# print "Resultados de la simulacion para N = %d:" % N
	# print "PPS=%d" % PPS
	# print "PTO=" + repr([int(round(e)) for e in PTO])
	# print "PPA=%d" % PPA

if __name__ == "__main__":
	VariablesDeControl()
	CondicionesIniciales()

	print "Simulando con G=%d, W=%d..." % (G, W)

	while True:
		i = MinTPSWorker()
		j = MinTPSGamer()

		if TPSW[i] < TPSG[j]:
			if TPLL <= TPSW[i]:
				LlegaCliente()
			else:
				Sale(TPSW, i, NSW, W, ITOW)
		else:
			if TPLL <= TPSG[j]:
				LlegaCliente()
			else:
				Sale(TPSG, j, NSG, G, ITOG)

		if T <= TF: continue
		if NSW + NSG > 0:
			TPLL = HV
			continue
		break

	print "Fin de simulación"

	ImprimirResultados()
