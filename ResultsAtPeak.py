##### Functions ####
def MaxIndex(list): #Funzione che ricava l'indice del massimo valore dell'array (su Fulx list.index() non funziona)
  for i in range(len(list)):
    if list[i] == max(list):
      maxindex = i
  return maxindex

def MinIndex(list): #Funzione che ricava l'indice del minimo valore dell'array (su Fulx list.index() non funziona)
  for i in range(len(list)):
    if list[i] == min(list):
      minindex = i
  return minindex

def CreateCurve(name,VariationParamName,VariationParamValue,formula): # Crea una curva 2D in Flux
    Curve = EvolutiveCurve2D(name=name,
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter[VariationParamName[0]],
                                                                             currentValue=VariationParamValue[0]),
                                                           SetParameterFixed(paramEvol=VariationParameter[VariationParamName[1]],
                                                                             currentValue=VariationParamValue[1]),
                                                           SetParameterFixed(paramEvol=VariationParameter[VariationParamName[2]],
                                                                             currentValue=VariationParamValue[2]),
                                                           SetParameterFixed(paramEvol=VariationParameter[VariationParamName[3]],
                                                                             currentValue=VariationParamValue[3]),
                                                           SetParameterFixed(paramEvol=VariationParameter[VariationParamName[4]],
                                                                             currentValue=VariationParamValue[4]),
                                                           SetParameterFixed(paramEvol=VariationParameter[VariationParamName[5]],
                                                                             currentValue=VariationParamValue[5]),
                                                           SetParameterXVariable(paramEvol=VariationParameter['TIME'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=0.015)]),
                 formula=[formula])

def AnalyzeCurve(nome): # Analizza una curva in FLux e restituisce il Y massimo e a che X corrisponde
    # Estrai i valori dalla curva
    xValues = Curve2d[nome].xAxis.x
    yValues = Curve2d[nome].y[0].values
    #Memorizza tempo picco e corrente
    XMin = xValues[MinIndex(yValues)]
    YMin = yValues[MinIndex(yValues)]
    XMax = xValues[MaxIndex(yValues)]
    YMax = yValues[MaxIndex(yValues)]
    if abs(YMin) > abs(YMax):
        return (XMin,YMin)
    else:
        return (XMax,YMax)


Scenario['SCENARIO_1'].selectFirstStep() #seleziono primo step

NumTimeStep = len(Scenario['SCENARIO_1'].getValuesParameter()["TIME"]) # Calcola il numero di time step
VariationParamName = Scenario['SCENARIO_1'].getValuesParameter().keys()  # Cerca i paramentri variabili dello scenario
VariationParamName.remove('TIME') # Rimuovo la variabile TIME
#### File Report ####
f = open("Data.txt", "w")

for t in range(len(VariationParamName)):
    f.write(VariationParamName[t])
    f.write(",")
f.write("Tp,Ip,T1t,T1,T2t,T2,T3t,T3,T4t,T4,T5t,T5,T6t,T6,T7t,T7,S1t,S1,S2t,S2,S3t,S3,S4t,S4,S5t,S5 \n")

def DataWrite(Xp,Yp):
    f.write(str(Xp)+",")
    f.write(str(Yp)+",")

#Itero su tutte le combinazioni dello scenario (con TimeStep = time step finale)
i = 1 # Step di partenza
while (Scenario['SCENARIO_1'].existNextStep()==1):
    Scenario['SCENARIO_1'].selectIndexStep(index=i*NumTimeStep)

    #estraggo nome e valore corrente dei parametri dello step per creare la curva
    VariationParamValue = []
    for c in range(len(VariationParamName)):
        try:
            VariationParamValue.append(ParameterGeom[VariationParamName[c]].value)
        except:
            VariationParamValue.append(VariationParameter[VariationParamName[c]].currentValue[0])

    for t in range(len(VariationParamName)):
        f.write(str(VariationParamValue[t]))
        f.write(",")

    # Creo la curva (nome,nome parametri, valore parametri, formula)
    CreateCurve('I_step'+str(i),VariationParamName,VariationParamValue,'I(B)')
    (Tp,Ip) = AnalyzeCurve('I_step'+str(i))
    DataWrite(Tp,Ip)

    CreateCurve('T1_BAVG_step'+str(i),VariationParamName,VariationParamValue,'T1_BAVG')
    (Tp,Bp) = AnalyzeCurve('T1_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('T2_BAVG_step'+str(i),VariationParamName,VariationParamValue,'T2_BAVG')
    (Tp,Bp) = AnalyzeCurve('T2_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('T3_BAVG_step'+str(i),VariationParamName,VariationParamValue,'T3_BAVG')
    (Tp,Bp) = AnalyzeCurve('T3_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('T4_BAVG_step'+str(i),VariationParamName,VariationParamValue,'T4_BAVG')
    (Tp,Bp) = AnalyzeCurve('T4_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('T5_BAVG_step'+str(i),VariationParamName,VariationParamValue,'T5_BAVG')
    (Tp,Bp) = AnalyzeCurve('T5_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('T6_BAVG_step'+str(i),VariationParamName,VariationParamValue,'T6_BAVG')
    (Tp,Bp) = AnalyzeCurve('T6_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('T7_BAVG_step'+str(i),VariationParamName,VariationParamValue,'T7_BAVG')
    (Tp,Bp) = AnalyzeCurve('T7_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('S1_BAVG_step'+str(i),VariationParamName,VariationParamValue,'S1_BAVG')
    (Tp,Bp) = AnalyzeCurve('S1_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('S2_BAVG_step'+str(i),VariationParamName,VariationParamValue,'S2_BAVG')
    (Tp,Bp) = AnalyzeCurve('S2_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('S3_BAVG_step'+str(i),VariationParamName,VariationParamValue,'S3_BAVG')
    (Tp,Bp) = AnalyzeCurve('S3_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('S4_BAVG_step'+str(i),VariationParamName,VariationParamValue,'S4_BAVG')
    (Tp,Bp) = AnalyzeCurve('S4_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CreateCurve('S5_BAVG_step'+str(i),VariationParamName,VariationParamValue,'S5_BAVG')
    (Tp,Bp) = AnalyzeCurve('S5_BAVG_step'+str(i))
    DataWrite(Tp,Bp)

    CurveVariation2D[ALL].delete()
    f.write("\n")

    i=i+1 # Fine loop while
f.close()
