def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    values = []
    top_arr = str()
    low_arr = str()
    line = str()
    line_result = str()
    contador2 = 0
    for count, operations in enumerate(problems):
        if "+" not in operations and "-" not in operations:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

        operation_no_spaces = operations.replace(" ", "")  # se usa para obtener los valores
        if "+" in operations:
            values.append(operation_no_spaces.split("+"))
            symbol = "+"
            try:
                resultado = int(values[count][0]) + int(values[count][1])
            except:
                arranged_problems = "Error: Numbers must only contain digits."
                return arranged_problems

        else:
            values.append(operation_no_spaces.split("-"))
            symbol = "-"
            try:
                resultado = int(values[count][0]) - int(values[count][1])
            except:
                arranged_problems = "Error: Numbers must only contain digits."
                print("exepcion")
                return arranged_problems

        if len(values[count][0]) > 4 or len(values[count][1]) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

        difference_digits = len(values[count][0]) - len(values[count][1])

        if difference_digits >= 0:
            top_arr = top_arr + 2 * " " + values[count][0] + 4 * " "
            line = line + 2 * "-" + len(values[count][0]) * "-" + 4 * " "
            low_arr = low_arr + symbol + " " + difference_digits * " " + values[count][1] + 4 * " "

        else:
            top_arr = top_arr + 2 * " " + abs(difference_digits) * " " + values[count][0] + 4 * " "
            line = line + 2 * "-" + len(values[count][1]) * "-" + 4 * " "
            low_arr = low_arr + symbol + " " + values[count][1] + 4 * " "

        resultado = str(resultado)

        lista = []
        contador = 0

        for x in line:

            if x == "-":
                es_simbolo = True
                contador = contador + 1
            else:
                if es_simbolo:
                    lista.append(contador)
                    es_simbolo = False
                contador = 0
        resta = lista[contador2] - len(resultado)
        contador2 = contador2 + 1
        line_result = line_result + resta * " " + resultado + 4 * " "

    arranged_problems = top_arr[0:len(top_arr) - 4] + "\n" + low_arr[0:len(low_arr) - 4] + "\n" + line[0:len(line) - 4]
    if solve:
        arranged_problems = top_arr[0:len(top_arr) - 4] + "\n" + low_arr[0:len(low_arr) - 4] + "\n" + line[0:len(
            line) - 4] + "\n" + line_result[0:len(line_result) - 4]

    return arranged_problems