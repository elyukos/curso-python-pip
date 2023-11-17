import random

def choose_options():
  print("test1")
  options_game = ("piedra", "papel","tijera")
  options_user = ("piedra", "papel","tijera","reset")
  user_option = input("piedra, papel o tijera? => ")
  user_option = user_option.lower()
  print("test2")
  if user_option not in options_user:
    print('opción no valida')
  #  return None, None
  
  computer_option = random.choice(options_game)
  
  print('user option: ', user_option)
  print('computer_option: ', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, empates, 
                user_score, computer_score):
  if(user_option == computer_option):
    print("resultado: empate")
    empates += 1
  elif user_option == "piedra": 
    if(computer_option == "tijera"):
      print("resultado: ganaste")
      user_score += 1
    else:
      print("resultado: perdiste")
      computer_score += 1
  elif user_option == "papel": 
    if(computer_option == "piedra"):
      print("resultado: ganaste")
      user_score += 1
    else:
      print("resultado: perdiste")
      computer_score += 1
  elif user_option == "tijera": 
    if(computer_option == "papel"):
      print("resultado: ganaste")
      user_score += 1
    else:
      print("resultado: perdiste")
      computer_score += 1
  elif user_option == "reset": 
    user_score = 0
    computer_score = 0
    empates = 0
  return empates, user_score, computer_score

def run_game():
  empates = 0
  user_score = 0
  computer_score = 0
  game_count = 1
  user_games = input("cuantos juegos? => ")
  user_games = int(user_games)
  
  while game_count <= user_games:
    print('-' * 29)
    print('JUEGO: ',game_count)
    print('-' * 29)
    print("empate - ", empates)
    print("user_score - ", user_score)
    print("computer_score - ", computer_score)
      
    user_option, computer_option = choose_options()
    print("test 1")
    empates, user_score, computer_score = check_rules(user_option, 
                                                      computer_option,
                                                      empates,  
                                                      user_score, 
                                                      computer_score)
    game_count = game_count + 1
  check_winner(empates, user_score, computer_score)

def check_winner(empates, user_score, computer_score):
  print('*' * 39)
  print("RESULTADO FINAL: ")
  print("empate - ", empates)
  print("user_score - ", user_score)
  print("computer_score - ", computer_score)
  if user_score == computer_score:
    print('EMPATASTE')
  elif user_score > computer_score:
    print('GANASTE')
  elif user_score < computer_score:
    print('PERDISTE')
  print('*' * 39)

run_game()

