# Introduction
print(" ==================================="
      "\n| GAME CURRENCY SAVINGS CALCULATOR  |"
      "\n|        1. Genshin Impact          |"
      "\n|     2. Punishing: Gray Raven      |"
      "\n|             3. Cancel             |"
      "\n ===================================")
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
            commission_pay = int(commission * 60)
            commission_primogems = int(commission_pay + primogems)
            primogems_fates = int(commission_primogems / 160)
            master_fates = int(masterless_starglitter / 5)
            total_fates = int(primogems_fates + master_fates + intertwined_fates)
            pity_hit = int(pity + total_fates)
            print("\n############ TOTAL ############")
            print("\nTotal Primogems:", commission_primogems)
            print("Total Intertwined Fates:", total_fates)
            print("Estimated pity to hit:", pity_hit)
            print("\n###############################")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                  "\n MAY THE RNG ARCHON BLESS YOU! "
                  "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      # Option 2: Punishing: Gray Raven
      if game_option == 2:
            print("PUNISHING: GRAY RAVEN")
            black_cards = int(input("Amount of black cards: "))
            missions = int(input("How many days until target banner?: "))
            daily = missions * 30
            total_weeks = missions / 7
            weekly = total_weeks * 1000
            total_black_cards = int(black_cards + daily + weekly)
            event_rd = int(total_black_cards / 250)
            print("\n############ TOTAL ############")
            print("Total Black Cards:", total_black_cards)
            print("Total Event R&D Tickets:", event_rd)
            print("\n###############################")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                  "\nMAY ASIMOV'S BLESSINGS BE ON YOU"
                  "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      # Option 3: Cancel
      if game_option == 3:
            print("Thank you for trying!")
            break

