# encoding: utf-8
import sys

# Get the total number of args passed to the program
totalArgs = len(sys.argv)
 
if totalArgs != 2:
	exit(u"Esta simulación recibe una variable de control N (Cantidad de puestos de atención)")

try:
	N = int(sys.argv[1])
except:
	exit(u"N debe ser el número de equipos a simular.")

def inicializarColas(N):
	for elem in range(N):
		TPS.append(sys.maxint)
		ITO.append(0)
		STO.append(0)

def menorTPS():
	min = sys.maxint
	minIndex = 0
	for index in range(len(TPS)):
		if TPS[index] < min:
			min = TPS[index]
			minIndex = index 
	return minIndex

def HVTPS():
	HV = sys.maxint
	maxIndex = 0
	for index in range(len(TPS)):
		if TPS[index] == HV:
			maxIndex = index
			break
	return maxIndex

def generarTA():
	return 1

def generarIA():
	return 1

def calcularArrep():
	return 1

MENORTPS = 0
CANTARREP =0
TPLL = 0
STS = 0
NS = 0
CLL =0
T = 0
TF = 9999999999999
IA = 0
TA = 0
ARREP = False
TPS = []
ITO = []
STO = []

inicializarColas(N)

while ((T < TF) or (T >= TF and NS > 0)):
	MENORTPS = menorTPS()
	if TPLL <= TPS[MENORTPS]:
		STS += ((TPLL - T) * NS)
		T = TPLL
		IA = generarIA()
		TPLL = T + IA		
		ARREP = calcularArrep()
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
			TPS[MENORTPS] = sys.maxint
	if T >= TF and NS > 0:
		TPLL = sys.maxint

#calcular los valores y hacer rutinas de calcularArrep y generarTA Y generarIA.