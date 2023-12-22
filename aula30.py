""" CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim) """

velocidade = 61 #velocidade atual do carro
local_carro = 101 #local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega


""" if velocidade > RADAR_1:
    print("Você está acima da velocidade máxima permitida")

    if local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        local_carro >= (LOCAL_1 - RADAR_RANGE):
            print("Você foi multado") """

velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= local_carro <= (LOCAL_1 + RADAR_RANGE) and local_carro >= (LOCAL_1 - RADAR_RANGE)

if velocidade_carro_passou_radar1:
    print ("Você está acima da velocidade")
if carro_multado_radar_1:
    print ("Você foi multado!")