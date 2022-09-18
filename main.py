from jogo_da_velha import crirarBoard, fazMovimento, getIputValido, printBoard, verificaGanhador, verificaMovimento

board = criarBoard()
print(board)
ganhador = verificaGanhador(board)
while(not ganhador):
    print("teste")
    break


print("saiu")