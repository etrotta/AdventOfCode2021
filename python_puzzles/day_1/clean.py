increases = 0  # Resultado
window_size = 3  # Distancia entre os pontos que nos temos que medir

with open("inputs/day1.txt", "r") as file:
    values = [int(file.readline()) for _ in range(window_size)]  # Guarda os primeiros N numeros numa lista
    for pos, line in enumerate(file):  # Para cada linha (e o numero da linha)
        line = int(line)  # converte para um numero
        which = pos % window_size  # 0, 1, 2, 0, 1, 2, 0, 1, ...
        value = values[which]  # para poder comparar com o numero N linhas atras
        values[which] = line  # e guarda o novo valor, depois de pegar o antigo
        if line > value:
            increases += 1
        #     print("Increased", end = "")
        # print()
        # print("from", value, "to", line)
        # elif line < last:
        #     decreases += 1
        # else:
        #     no_change += 1

print(increases)
