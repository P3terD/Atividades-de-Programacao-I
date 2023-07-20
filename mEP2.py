#Verifica se uma pessoa é elegível para doar sangue

# INFO

isEligible = 1
weight = float(input())
age = int(input())
auth = ""

if 16 <= age <= 17:
    auth = str(input())

isHealth = str(input())
useDrugs = str(input())
firstDonation = str(input())
lastDonation = 0
donsLastYear = 0

if firstDonation == "N":
    lastDonation = int(input())
    donsLastYear = int(input())

bioGender = str(input())
isPregnant = ""
isBF = ""
babyAge = 0

if bioGender == "F":
    isPregnant = str(input())
    isBF = str(input()) #BF stands for Breastfeeding
    if isBF == "S":
        babyAge = int(input())

# SHOW INFO
print(f"Peso: {weight}")
print(f"Idade: {age}")

if 16 <= age <= 17:
    print(f"Documento de autorizacao: {auth}")

print(f"Boa saude: {isHealth}")
print(f"Uso de drogas injetaveis: {useDrugs}")
print(f"Primeira doacao: {firstDonation}")

if firstDonation == "N":
    print(f"Meses desde ultima doacao: {lastDonation}")
    print(f"Doacoes nos ultimos 12 meses: {donsLastYear}")

print(f"Sexo biologico: {bioGender}")

if bioGender == "F":
    print(f"Gravidez: {isPregnant}")
    print(f"Amamentando: {isBF}")
    if isBF == "S":
        print(f"Meses bebe: {babyAge}")

# IMPEDIMENTS
if weight < 50:
    print("Impedimento: abaixo do peso minimo.")
    isEligible = 0

if age < 16:
    print("Impedimento: menor de 16 anos.")
    isEligible = 0

if 17 >= age >= 16 and auth == "N":
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    isEligible = 0

if 60 < age <= 69 and firstDonation == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
    isEligible = 0

if age > 69:
    print("Impedimento: maior de 69 anos.")
    isEligible = 0

if isHealth == "N":
    print("Impedimento: nao esta em boa saude.")
    isEligible = 0

if useDrugs == "S":
    print("Impedimento: uso de drogas injetaveis.")
    isEligible = 0

if ((bioGender == "M" and 0 <= lastDonation < 2) or (bioGender == "F" and 0 <= lastDonation < 3)) and firstDonation == "N":
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    isEligible = 0

if ((bioGender == "M" and donsLastYear >= 4) or (bioGender == "F" and donsLastYear >= 3)) and firstDonation == "N":
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    isEligible = 0

if isPregnant == "S":
    print("Impedimento: gravidez.")
    isEligible = 0

if isBF == "S" and babyAge < 12:
    print("Impedimento: amamentacao.")
    isEligible = 0

if isEligible == 1:
    print("Procure um hemocentro.")
