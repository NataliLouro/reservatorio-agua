from colorama import Fore, Style, init

# Inicializa o colorama para garantir o funcionamento correto no terminal
init(autoreset=True)


def definir_alerta(nivel):
  """Retorna a tupla contendo a mensagem de situação e a cor correspondente

  com base no nível do reservatório informado (de 1 a 5).
  """
  if nivel == 1:
    return "Nível 1: Muito baixo (crítico)", Fore.RED
  elif nivel == 2:
    return "Nível 2: Baixo", Fore.YELLOW
  elif nivel == 3:
    return "Nível 3: Médio", Fore.GREEN
  elif nivel == 4:
    return "Nível 4: Alto", Fore.CYAN
  elif nivel == 5:
    return "Nível 5: Muito alto (alerta)", Fore.BLUE
  else:
    return "Nível inválido", Fore.WHITE


def simular_monitoramento():
  # Lista contendo os níveis do reservatório a serem simulados
  niveis_reservatorio = [1, 2, 3, 4, 5]

  print("=" * 50)
  print("     MONITORAMENTO DE NÍVEIS DO RESERVATÓRIO DE ÁGUA")
  print("=" * 50 + "\n")

  # Itera sobre cada nível presente na lista para realizar a simulação
  for nivel in niveis_reservatorio:
    mensagem, cor = definir_alerta(nivel)

    # Exibe a situação atual com a cor correspondente
    print(f"{cor}{mensagem}{Style.RESET_ALL}")


if __name__ == "__main__":
  simular_monitoramento()