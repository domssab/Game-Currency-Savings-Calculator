# Introduction
print("GAME CURRENCY SAVINGS CALCULATOR"
      "\n1. Genshin Impact"
      "\n2. Punishing: Gray Raven"
      "\n3. Cancel")
game_option = 0
while game_option in (0,1,2,3):
      # Game option menu
      game_option = int(input("Enter the game: "))
      # Option 1: Genshin Impact
      if game_option == 1:
            print("GENSHIN IMPACT")
            primogems = int(input("Amount of primogems: "))
            masterless_starglitter = int(input("Amount of masterless starglitter: "))
            intertwined_fates = int(input("Amount of intertwined fates: "))
            pity = int(input("Your current pity: "))
            commission = int(input("How many days until the target banner?: "))
            commission_pay = commission * 60
            commission_primogems = commission_pay + primogems
            primogems_fates = commission_primogems / 160
            master_fates = masterless_starglitter / 5
            total_fates = primogems_fates + master_fates + intertwined_fates
            pity_hit = pity + total_fates
            print("Your total primogems is:", commission_primogems)
            print("Your total intertwined fates is:", total_fates)
            print("Estimated pity to hit:", pity_hit)
      # Option 2: Punishing: Gray Raven
      if game_option == 2:
            print("PUNISHING: GRAY RAVEN")
            black_cards = int(input("Amount of black cards: "))
            missions = int(input("How many days until target banner?: "))
            daily = missions * 30
            total_weeks = missions / 7
            weekly = total_weeks * 1000
            total_black_cards = black_cards + daily + weekly
            event_rd = total_black_cards / 250
            print("Your total black cards is:", total_black_cards)
            print("Your total Event R&D Tickets is:", event_rd)

