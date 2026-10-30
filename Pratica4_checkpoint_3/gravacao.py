import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

lendo_cartao = SimpleMFRC522()

# gravando os numeros USP
texto = "15004433/15651561" 

print("Aproxime a tag")
lendo_cartao.write(texto)#gravando o texto no cartão
print("Concluido")
