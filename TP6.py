import sys

def inicializarColas(N)
	for elem in range(N):
		TPS[elem] = sys.maxint
		ITO[elem] = 0
		STO[elem] = 0

def menorTPS():
	min = sys.maxint
	minIndex = 0
	for index in range(len(TPS)):
		if TPS[index] < min
			min = TPS[index]
			minIndex = index 
	return minIndex

def HVTPS():
	HV = sys.maxint
	maxIndex = 0
	for index in range(len(TPS)):
		if TPS[index] = HV
			maxIndex = index
			break
	return maxIndex

N = 0
TPLL = 0
STS = 0
NS = 0
CLL = 0
T = 0
TF = 9999999999999
IA = 0
TA = 0
ARREP = FALSE
CANTARREP = 0
TPS = []
ITO = []
STO = []
inicializarColas(N)
MENORTPS = 0


while ((T < TF) or (T >= TF && NS > 0)):
	MENORTPS = menorTPS()
	if TPLL <= TPS[MENORTPS]
		STS += ((TPLL - T) * NS)
		T = TPLL
		IA = generarIA()
		TPLL = T + IA		
		ARREP = calcularArrep()
		if ARREP:
			CANTARREP++
			continue
		NS++
		CLL++
		if NS < N
			TA = generarTA()
			HVTPSindex = HVTPS()
			TPS[HVTPSindex] = T + TA
			STO[HVTPSindex] += (T - ITO(HVTPSindex))
	else
		STS += ((TPS[MENORTPS] - T) * NS)
		T = TPS[MENORTPS]
		NS--
		if NS >= N
			TA = generarTA()
			TPS[MENORTPS] = T + TA
		else
			ITO[MENORTPS] = T
			TPS[MENORTPS] = sys.maxint
	if T >= TF && NS > 0
		TPLL = sys.maxint

#calcular los valores y hacer rutinas de calcularArrep y generarTA Y generarIA.