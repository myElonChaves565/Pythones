import tkinter as tk





def adicao():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Entrada inválida")

def subtracao():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Entrada inválida")

def multiplicacao():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Entrada inválida")

def divisao():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 != 0:
            resultado = num1 / num2
            label_resultado.config(text="Resultado: " + str(resultado))
        else:
            label_resultado.config(text="Erro: Divisão por zero")
    except ValueError:
        label_resultado.config(text="Entrada inválida")



window = tk.Tk()
window.title("Calculadora")





label_num1 = tk.Label(window, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()



label_num2 = tk.Label(window, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()


btn_adicao = tk.Button(window, text="+", command=adicao)
btn_adicao.pack()

btn_subtracao = tk.Button(window, text="-", command=subtracao)
btn_subtracao.pack()

btn_multiplicacao = tk.Button(window, text="*", command=multiplicacao)
btn_multiplicacao.pack()

btn_divisao = tk.Button(window, text="/", command=divisao)
btn_divisao.pack()




label_resultado = tk.Label(window, text="Resultado: ")
label_resultado.pack()


window.mainloop()
