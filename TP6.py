# encoding: utf-8
import sys, random
HV = sys.maxint

def obtenerN():
	if len(sys.argv) != 2:
		exit(u"Esta simulacion recibe una variable de control N (Cantidad de puestos de atencion)")

	try:
		global N
		N = int(sys.argv[1])
	except:
		exit(u"N debe ser el numero de equipos a simular.")

def inicializarColas():
	for elem in range(N):
		TPS.append(HV)
		ITO.append(0)
		STO.append(0)

def condicionesIniciales():
	global MENORTPS, CANTARREP, TPLL, SPS, NS, CLL, T, TF, IA, TA, ARREP, TPS, ITO, STO

	MENORTPS = 0
	CANTARREP = 0
	TPLL = 0
	SPS = 0
	NS = 0
	CLL = 0
	T = 0
	TF = 13140000
	IA = 0
	TA = 0
	ARREP = False
	TPS = []
	ITO = []
	STO = []

	obtenerN()
	inicializarColas()

def menorTPS(): 
	min = HV
	minIndex = 0
	for index in range(len(TPS)):
		if TPS[index] < min:
			min = TPS[index]
			minIndex = index
	return minIndex

def HVTPS():
	maxIndex = 0
	for index in range(len(TPS)):
		if TPS[index] == HV:
			maxIndex = index
			break
	return maxIndex

def generarIA():
	R = random.random()
	IA = int((R * 1000) % 15)
	return IA

def generarTA():
	R = random.random()
	TA = int(( 10 + (R * 500) % 120))
	return TA

def calcularArrep():
	global ARREP
	if NS - N > 4: ARREP = True
	else:
		ARREP = random.random() < 0.8
	return ARREP

def calcularEImprimirResultados():

	PPS = SPS * 1.0 / CLL
	PTO = [ e * 100.0 / T for e in STO ]
	PPA = CANTARREP * 100.0 / (CLL + CANTARREP)

	print "Resultados de la simulacion para N = %d :" % N
	print "PPS=%d" % PPS
	print "PTO=" + repr([int(round(e)) for e in PTO])
	print "PPA=%d" % PPA

if __name__ == "__main__":
	condicionesIniciales()

	print "Simulando con N = %d " % N

	while T < TF or NS > 0:

		MENORTPS = menorTPS()

		if TPLL <= TPS[MENORTPS]:
			SPS += (TPLL - T) * NS
			T = TPLL
			IA = generarIA()
			TPLL = T + IA
			calcularArrep()
			if ARREP:
				CANTARREP += 1
				continue
			NS += 1
			CLL += 1
			if NS <= N:
				TA = generarTA()
				HVTPSindex = HVTPS()
				TPS[HVTPSindex] = T + TA
				STO[HVTPSindex] += T - ITO[HVTPSindex]
		else:
			SPS += (TPS[MENORTPS] - T) * NS
			T = TPS[MENORTPS]
			NS -= 1
			if NS >= N:
				TA = generarTA()
				TPS[MENORTPS] = T + TA
			else:
				ITO[MENORTPS] = T
				TPS[MENORTPS] = HV
		if T >= TF and NS > 0:
			TPLL = HV

	calcularEImprimirResultados()
