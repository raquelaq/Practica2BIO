from Bio.Seq import Seq

adn = input("Introduce una secuencia de ADN: ")

seq = Seq(adn)

complementaria = seq.complement()
reversa_complementario = seq.reverse_complement()


print("Hebra original (5' -> 3'):", seq)
print("Hebra complementaria (3' -> 5'):", complementaria)
print("Reversa complementaria (5'-> 3'):", reversa_complementario)