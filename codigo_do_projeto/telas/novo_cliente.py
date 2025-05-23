import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from telas.ordem_servico import ordem_servico

def novo_cliente():
  
  def botao_gerar_os():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    endereco = endereco_entry.get("1.0", tk.END).strip()
    marca = marca_entry.get()
    modelo = modelo_entry.get()
    placa = placa_entry.get()
    chassi = chassi_entry.get()
    ano = ano_fabricacao_entry.get()
    cor = cor_entry.get()
    servico = servico_entry.get("1.0", tk.END).strip()
    data_hora = data_hora_atendimento_entry.get()
    observacoes = observacoes_entry.get("1.0", tk.END).strip()
    forma_pagamento = forma_pagamento_combo.get()
    Dados = {
      "Nome": nome,
      "CPF": cpf,
      "Email": email,
      "Telefone": telefone,
      "Endereco": endereco,
      "Marca": marca,
      "Modelo": modelo,
      "Placa": placa,
      "Chassi": chassi,
      "Ano": ano,
      "Cor": cor,
      "Servico": servico,
      "DataHora": data_hora,
      "Observacoes": observacoes,
      "FormaPagamento": forma_pagamento
  }
    janelacadastro.destroy()  # Fecha a janela após gerar a ordem de serviço
    ordem_servico(Dados)

  # Cria a janela principal
  global janelacadastro
  janelacadastro = tk.Tk()
  janelacadastro.title("Cadastrar Novo Cliente")

  # Canvas para a barra de rolagem
  canvas = tk.Canvas(janelacadastro)
  scrollbar = ttk.Scrollbar(janelacadastro, orient="vertical", command=canvas.yview)
  scrollable_frame = ttk.Frame(canvas)

  scrollable_frame.bind(
      "<Configure>",
      lambda e: canvas.configure(
          scrollregion=canvas.bbox("all")
      )
  )

  canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
  canvas.configure(yscrollcommand=scrollbar.set)

  canvas.grid(row=0, column=0, sticky="nsew")
  scrollbar.grid(row=0, column=1, sticky="ns")

  # Título principal na tela
  titulo_label = ttk.Label(scrollable_frame, text="Cadastrar Novo Cliente", font=("Arial", 16))
  titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20))

  # --- Frame para Dados do Cliente ---
  cliente_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Cliente")
  cliente_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

  nome_label = ttk.Label(cliente_frame, text="Nome:")
  nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
  nome_entry = ttk.Entry(cliente_frame, width=30)
  nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

  cpf_label = ttk.Label(cliente_frame, text="CPF:")
  cpf_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
  cpf_entry = ttk.Entry(cliente_frame, width=20)
  cpf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

  telefone_label = ttk.Label(cliente_frame, text="Telefone:")
  telefone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
  telefone_entry = ttk.Entry(cliente_frame, width=20)
  telefone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

  email_label = ttk.Label(cliente_frame, text="E-mail:")
  email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
  email_entry = ttk.Entry(cliente_frame, width=30)
  email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

  endereco_label = ttk.Label(cliente_frame, text="Endereço:")
  endereco_label.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
  endereco_entry = tk.Text(cliente_frame, height=3, width=30)
  endereco_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

  # --- Frame para Dados do Veículo ---
  veiculo_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Veículo")
  veiculo_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

  marca_label = ttk.Label(veiculo_frame, text="Marca:")
  marca_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
  marca_entry = ttk.Entry(veiculo_frame, width=20)
  marca_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

  placa_label = ttk.Label(veiculo_frame, text="Placa:")
  placa_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
  placa_entry = ttk.Entry(veiculo_frame, width=10)
  placa_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

  chassi_label = ttk.Label(veiculo_frame, text="Chassi:")
  chassi_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
  chassi_entry = ttk.Entry(veiculo_frame, width=30)
  chassi_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

  modelo_label = ttk.Label(veiculo_frame, text="Modelo:")
  modelo_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
  modelo_entry = ttk.Entry(veiculo_frame, width=20)
  modelo_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

  ano_fabricacao_label = ttk.Label(veiculo_frame, text="Ano de Fabricação:")
  ano_fabricacao_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
  ano_fabricacao_entry = ttk.Entry(veiculo_frame, width=10)
  ano_fabricacao_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

  cor_label = ttk.Label(veiculo_frame, text="Cor:")
  cor_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
  cor_entry = ttk.Entry(veiculo_frame, width=15)
  cor_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

  # --- Frame para Serviço ---
  servico_frame = ttk.LabelFrame(scrollable_frame, text="Serviço")
  servico_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

  servico_solicitado_label = ttk.Label(servico_frame, text="Serviço Solicitado:")
  servico_solicitado_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
  servico_entry = tk.Text(servico_frame, height=3, width=30)
  servico_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

  data_hora_atendimento_label = ttk.Label(servico_frame, text="Data e Hora do Atendimento:")
  data_hora_atendimento_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
  data_hora_atendimento_entry = ttk.Entry(servico_frame, width=25)
  data_hora_atendimento_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

  observacoes_label = ttk.Label(servico_frame, text="Observações Adicionais:")
  observacoes_label.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
  observacoes_entry = tk.Text(servico_frame, height=3, width=30)
  observacoes_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

  forma_pagamento_label = ttk.Label(servico_frame, text="Forma de Pagamento:")
  forma_pagamento_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
  forma_pagamento_opcoes = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"] # Adicione mais opções se necessário
  forma_pagamento_combo = ttk.Combobox(servico_frame, values=forma_pagamento_opcoes, width=20)
  forma_pagamento_combo.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
  forma_pagamento_combo.set(forma_pagamento_opcoes[0]) # Define um valor padrão

  # --- Botões Adicionais ---
  alterar_button = ttk.Button(scrollable_frame, text="Salvar", command=botao_gerar_os)
  alterar_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")



  # Configura o gerenciamento de layout para redimensionamento da coluna principal
  janelacadastro.columnconfigure(0, weight=1)
  janelacadastro.rowconfigure(0, weight=1) # Permite que o canvas se expanda

  scrollable_frame.columnconfigure(0, weight=1)
  cliente_frame.columnconfigure(1, weight=1)
  veiculo_frame.columnconfigure(1, weight=1)
  servico_frame.columnconfigure(1, weight=1)

