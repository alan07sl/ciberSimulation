# encoding: utf-8
import sys, random
HV = sys.maxint

def obtenerN():
	if len(sys.argv) != 2:
		exit(u"Esta simulación recibe una variable de control N (Cantidad de puestos de atención)")

	try:
		global N
		N = int(sys.argv[1])
	except:
		exit(u"N debe ser el número de equipos a simular.")

def inicializarColas():
	for elem in range(N):
		TPS.append(HV)
		ITO.append(0)
		STO.append(0)

def condicionesIniciales():
	global MENORTPS, CANTARREP, TPLL, STS, NS, CLL, T, TF, IA, TA, ARREP, TPS, ITO, STO

	MENORTPS = 0
	CANTARREP = 0
	TPLL = 0
	STS = 0
	NS = 0
	CLL =0
	T = 0
	TF = 1000000
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
	if R < 0.1:
		IA = 5
	elif R < 0.3:
		IA = 30
	elif R < 0.8:
		IA = 45
	else:
		IA = 60
	return IA

def generarTA():
	R = random.random()
	if R < 0.1:
		TA = 5
	elif R < 0.2:
		TA = 10
	elif R < 0.3:
		TA = 15
	elif R < 0.5:
		TA = 60
	elif R < 0.7:
		TA = 120
	else:
		TA = 240
	return TA

def calcularArrep():
	global ARREP
	if NS > 3: ARREP = True
	else:
		ARREP = random.random() < 0.8
	return ARREP

if __name__ == "__main__":
	condicionesIniciales()

	while T < TF or NS > 0:
		MENORTPS = menorTPS()
		if TPLL <= TPS[MENORTPS]:
			STS += ((TPLL - T) * NS)
			T = TPLL
			IA = generarIA()
			TPLL = T + IA
			calcularArrep()
			if ARREP:
				CANTARREP += 1
				continue
			NS += 1
			CLL += 1
			if NS < N:
				TA = generarTA()
				HVTPSindex = HVTPS()
				TPS[HVTPSindex] = T + TA
				STO[HVTPSindex] += (T - ITO(HVTPSindex))
		else:
			STS += ((TPS[MENORTPS] - T) * NS)
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

# calcular los valores
