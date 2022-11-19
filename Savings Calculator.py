# Introduction
print("GAME CURRENCY SAVINGS CALCULATOR"
      "\n1. Genshin Impact"
      "\n2. Punishing: Gray Raven"
      "\n3. Cancel")
game_option = 0
while game_option in (0,1,2,3):
      # Game option menu
      game_option = int(input("Enter the game:"))
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
            print("Your total primogems is: ", total_fates)
            print("Estimated pity to hit: ", pity_hit)

