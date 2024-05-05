import tkinter as tk

class AppCalculo:
  
  def __init__(self,root):
    self.root = root
    root.title("Calculo")
    root.configure(bg="black")

    self.var_result = tk.StringVar()
    self.var_result.set("")


    self.entrada = tk.Entry(root,textvariable=self.var_result,justify="right",font=('Arial',14),bg="white")

    self.entrada.grid(row=0,column=0,columnspan=4,sticky="nsew")


    botoes = [
      
      ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
      ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
      ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
      ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("-", 4, 3),

    ]


    for (texto, linha, coluna) in botoes:

        botao = tk.Button(root,text=texto,command=lambda t=texto:
        self.click_button(t),font=('Arial',14))

        botao.grid(row=linha, column=coluna, sticky="nsew")

        botao.configure(bg="black", fg="white")


    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(4, weight=1)


  def click_button(self, char):
        if char == '=':
            try:
                result = eval(self.var_result.get())
                self.var_result.set(str(result))
            except:
                self.var_result.set("Erro")
        else:
            texto_atual = self.var_result.get()
            self.var_result.set(texto_atual + char)


if __name__ == "__main__":

   root = tk.Tk()
   app = AppCalculo(root)
   root.mainloop() 