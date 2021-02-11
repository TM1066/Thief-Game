import random
from time import sleep
import sys
from termcolor import colored
from getch import getch
import os

stolen_items = ['back','Thievin Tools']
item_values = [None,10]

possible_colors = ["white","grey","blue","cyan","green","yellow","magenta"]
player_color = "white"
player_attrs = None
health = 100
stamina = 100
wealth = 0

#Random first-time through checks and set-ups
color_change = False
color_change_check = False
first_time = True
Returned = False
Taeris_Talk = True
possible_colors = ["white","grey","blue","cyan","green","yellow","magenta"]

stolen_things = zip(stolen_items,item_values)
stolen_things = list(stolen_things)

#This isn't how you're meant to use classes. Buuuuuuuuuuut, Google is hard & this works well enough for my organisation itch.
class text:
  def basic(content,color,attributes,speed):
    if attributes != None:
      for x in colored(str(content),str(color),attrs=[str(attributes)]):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(speed)
    else:
      for x in colored(str(content),str(color)):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(speed)

  def taeris(content,speed):
    for x in colored(str(content),"red",attrs=["bold"]):
      sys.stdout.write(x)
      sys.stdout.flush()
      sleep(speed)

  def player(content,speed):
    if player_attrs != None:
      for x in colored(str(content).capitalize(),player_color,attrs=[player_attrs]):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(speed)
    else:
      for x in colored(str(content).capitalize(),player_color):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(speed)

  def waiting(time):
    for x in range(time):
      text.basic("...","white","bold",0.1)
      print("\r")
      text.delete_last_line()

  def title(content,speed):
    if player_attrs != None:
      for x in colored(str(content).upper(),player_color,attrs=[player_attrs]):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(speed)
    else:
      for x in colored(str(content).upper(),player_color):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(speed)
  
  def delete_last_line():
    #"Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()

class items:

  def add(item,value):
    global stolen_things
    global stolen_items
    global stolen_values

    stolen_items.append(item)
    item_values.append(value)
    
    stolen_things = zip(stolen_items,item_values)
    stolen_things = list(stolen_things)

  def sell(item_number):
    global wealth
    item_number = int(item_number) - 1
    wealth = wealth + item_values[item_number]
    stolen_things.remove(stolen_things[item_number])

  def show():
    for x,res in enumerate(stolen_things,1):
      for x in str("(" + str(x) + ")" + " " + colored(str(res),player_color)):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(0.05)
      for x in str(len(stolen_things)):
        print()

class stats:
  #using health as a death check & stamina as an event pass check
  global health
  global stamina
  class health_stat:
    def death_check():
      if health <= 0:
        os.system("clear")
        game_over()
      else:
        return
  class stamina_stat:
    def tire_check():
      if stamina < 25:
        print()
        text.basic("You're too tired to even attempt another robbery. You'll need to rest","white","bold",0.05)
        os.system("clear")
        game_main()
    def rest():
      global health
      global stamina
      os.system("clear")
      text.basic("You can kinda do this infinitely right now soooo... Honor System?","grey","bold",0.05)
      print()
      print()
      text.player("BRB, Sleeping",0.05)
      print()
      text.waiting(5)
      stamina = 100
      if health < 100:
        if health <= 20:
          health = health + 50
        elif health:
          health = health + 25

class tutorials:

  def health():
    global first_time
    text.taeris("Health is quite simply a measure of your physical wellbeing.",0.05)
    print()
    text.taeris("Should it reach 0, or you become damaged beyond your limits,",0.05)
    print()
    text.taeris("You will swiftly be delivered back to me and I shall deal with the fallout.",0.05)
    print()
    print()
    text.taeris("Anything else?",0.05)
    print()
    player_choices("Stamina","Wealth","Encounters","Nope")
    print()
    tutorial_choice = getch()

    if tutorial_choice == "1":
      os.system("clear")
      tutorials.stamina()
    elif tutorial_choice == "2":
      os.system("clear")
      tutorials.wealth()
    elif tutorial_choice == "3":
      os.system("clear")
      tutorials.encounters()
    elif tutorial_choice == "4":
      os.system("clear")
      text.taeris("Good, now get on with the daring robberies.",0.05)
      sleep(1)
      first_time = False
      game_main()

  def stamina():
    global first_time
    text.taeris("Stamina is a measure of how much you can exert yourself before you tire.",0.05)
    print()
    text.taeris("Should it reach 0, or you exert yourself too much,",0.05)
    print()
    text.taeris("You'll be returned back to the hideout\n and you shall have to rest before attempting any more thefts.",0.05)
    print()
    print()
    text.taeris("Anything else?",0.05)
    print()
    player_choices("Health","Wealth","Encounters","Nope")
    print()
    tutorial_choice = getch()

    if tutorial_choice == "1":
      os.system("clear")
      tutorials.health()
    elif tutorial_choice == "2":
      os.system("clear")
      tutorials.wealth()
    elif tutorial_choice == "3":
      os.system("clear")
      tutorials.encounters()
    elif tutorial_choice == "4":
      os.system("clear")
      text.taeris("Good, now get on with the daring robberies.",0.05)
      sleep(1)
      first_time = False
      game_main()

  def wealth():
    global first_time
    text.taeris("Wealth is quite self-explanatory, however,\n",0.05)
    text.taeris("It shouldn't be underestimated as it is the primary evidence of your place in our world.",0.05)
    print()
    text.taeris("Should you fail to incur enough, it will reflect badly on us all.",0.05)
    print()
    sleep(1)
    print()
    text.taeris("Anything else?",0.05)
    print()
    player_choices("Health","Stamina","Encounters","Nope")
    print()
    tutorial_choice = getch()

    if tutorial_choice == "1":
      os.system("clear")
      tutorials.health()
    elif tutorial_choice == "2":
      os.system("clear")
      tutorials.stamina()
    elif tutorial_choice == "3":
      os.system("clear")
      tutorials.encounters()
    elif tutorial_choice == "4":
      os.system("clear")
      text.taeris("Good, now get on with the daring robberies.",0.05)
      sleep(1)
      first_time = False
      game_main()

  def encounters():
    global first_time
    text.taeris("Encounters are your primary source of items to sell",0.05)
    print()
    text.taeris("It generally goes:\nYou find someone(or something) you want to steal from;\nYou choose a method to steal something from them\nand then you see if you can carry out your daring plan.",0.05)
    print()
    print()
    text.taeris("You may fail with your selected plan if you are too tired\n or incur too much damage during the operation",0.05)
    print()
    print()
    text.taeris("It should also be noted that it is often an option of great prevalence to just run. \n",0.05)
    text.taeris("I do not feel the need to explain how this would reflect badly on you and us.",0.05)
    print()
    sleep(3)
    print()
    text.taeris("Anything else?\n",0.05)
    print()
    player_choices("Health","Stamina","Wealth","Nope")
    print()
    tutorial_choice = getch()

    if tutorial_choice == "1":
      os.system("clear")
      tutorials.health()
    elif tutorial_choice == "2":
      os.system("clear")
      tutorials.stamina()
    elif tutorial_choice == "3":
      os.system("clear")
      tutorials.wealth()
    elif tutorial_choice == "4":
      os.system("clear")
      text.taeris("Good, now get on with the daring robberies.",0.05)
      sleep(1)
      first_time = False
      game_main()

class event_setup:

    def event_difficulty_check(difficulty):
      global stamina
      global health
      if str(difficulty).lower() == "easy":
        if stamina >= 25:
          stamina = stamina - 25
          return True
        elif stamina < 25:
          return False

      if str(difficulty).lower() == "medium":
        if stamina >= 50:
          stamina = stamina - 50
          return True
        elif stamina < 50:
          return False

      if str(difficulty).lower() == "hard":
        if stamina >= 75:
          stamina = stamina - 75
          return True
        elif stamina < 75:
          return False

    def event_prompt(content,color,attrs,speed):
      text.basic(content,color,attrs,speed)
      print()
      print()

    def event_choices(*choices):
      event_options = []
      for x in choices:
        event_options.append([str(x)])
      for x,res in enumerate(event_options,1):
        for x in str("(" + str(x) + ")" + " " + colored(str(res),player_color)):
          sys.stdout.write(x)
          sys.stdout.flush()
          sleep(0.05)
        for x in str(len(event_options)):
          print()

    def return_repeat():
      player_choices("continue searching?","return back to your stash?")
      n = getch()
      if n == "1":
        stats.stamina_stat.tire_check()
        events.event(random.randint(0,15))
      else:
        game_main()

    def event_outcome(content,difficulty,minus_health,item,value):
        global stolen_items
        global stolen_values
        global health
        random.seed(random.randint(0,15))
        text.player(content,0.05)
        print()
        text.waiting(3)
        stats.health_stat.death_check()
        print()
        event_pass = bool(event_setup.event_difficulty_check(difficulty))
        if event_pass == True and item != None:
          text.player("You succeed! and along the way you find a/an ",0.05)
          text.player(str(item),0.05)
          text.player("!",0.05)
          print()
          text.player("You estimate it to be worth about ",0.05)
          text.player(str(value),0.05)
          text.player(" universal moneys.",0.05)
          print()
          print()
          items.add(item,value)
          event_setup.return_repeat()
        elif event_setup.event_difficulty_check(difficulty) == True and item == None:
          text.player("You succeed! But,(sadly) can't find any items to grab.",0.05)
          print()
          print()
          event_setup.return_repeat()

        else:
          health = health - minus_health
          text.player("You fail (miserably),lose whatever items may have been gained and take some scuffs along the way.",0.05)
          stats.health_stat.death_check()
          print()
          print()
          event_setup.return_repeat()

class events:
  global health
  global stamina
  def event(event_id):
    os.system("clear")
    HUD()
    print()
    print()
    stats.health_stat.death_check()
    #Probably a much better way of doing this, I know.
    #----------------------------------Event(0)--------------------------------------#
    if event_id == 0:
      event_setup.event_prompt("suddenly, a DOG appears!","white","bold",0.05)

      event_setup.event_choices("attack!","RUN!","Pet it")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You rush forwards and attack the dog!","medium",50,"Dog Collar",5)
      elif event_choice == "2":
        event_setup.event_outcome("You run as fast as you can!","easy",10,None,1)
      elif event_choice == "3":
        event_setup.event_outcome("You approach it carefully in an attempt to russle its ears.","easy",10,"Dogs Collar",20)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(1)--------------------------------------#
    elif event_id == 1:
      event_setup.event_prompt("You find a random rich person walking along the street.","white","bold",0.05)

      event_setup.event_choices("try to pickpocket him","RUN")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You swiftly manoeuvre yourself into an encounter with the mans valuables and...","medium",20,"Smart-Looking Watch",80)
      elif event_choice == "2":
        event_setup.event_outcome("You just start booking it in a straight line away from the stranger!","easy",10,None,1)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(2)--------------------------------------#
    elif event_id == 2:
      event_setup.event_prompt("You're just minding your own business looking for something to steal when,\nsuddenly, some gangstah comes up and starts dissin' ya fly girl. Whatever shall you do?","white","bold",0.05)

      event_setup.event_choices("Give im' one a these: Brandish a firearm","Cower")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("The weapon kicks back hard and you struggle to keep it under control.","hard",50,"Empty Shotgun",50)
      elif event_choice == "2":
        event_setup.event_outcome("You cower pathetically and hope he passes you by","easy",40,None,1)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(3)--------------------------------------#
    elif event_id == 3:
      event_setup.event_prompt("You arrive outside a bank and size it up for a robbery.","white","bold",0.05)

      event_setup.event_choices("Sneak in around the back","befriend the faculty")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You slither around the bank to its rear like a snake and attempt to sneak in unnoticed.","hard",50,"Big Bag of Swag",160)
      elif event_choice == "2":
        event_setup.event_outcome("You swagger into the bank and attempt to charm its staff into looking the other way.","hard",30,"Expensive Necklace",80)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(4)--------------------------------------#
    elif event_id == 4:
      event_setup.event_prompt("You come across a proselytizing man in the street.","white","bold",0.05)

      event_setup.event_choices("Steal his donations","Convince him that you have seen the error of your ways")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You snatch up his cup of donations and begin dashing away!","medium",20,"Full Donation Cup",30)
      elif event_choice == "2":
        event_setup.event_outcome("You meagerly limp over and begin lecturing the man in return as to your own spiritual ascension in hopes that he'll give you something.","hard",10,"Holy Ornament",60)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(5)--------------------------------------#
    elif event_id == 5:
      event_setup.event_prompt("You're walking along a forest trail when you suddenly fall into the ground!\nYou appear to have fallen into a trap!","white","bold",0.05)

      event_setup.event_choices("Scramble out","Rummage around for secrets")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You deftly grasp at a tree branch and try to leverage yourself out of the hole.","easy",50,None,1)
      elif event_choice == "2":
        event_setup.event_outcome("You rumble around like a rodent when you come acroos a skeleton covered in gold!\nYou grab some of its jewellery and attempt to escape.","hard",70,"Various Doubloons",240)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(6)--------------------------------------#
    elif event_id == 6:
      event_setup.event_prompt("You're walking along the road when a glint hits the corner of your eye!\nThere appears to be a magpies stash of valuables hidden in one of the surrounding trees.","white","bold",0.05)

      event_setup.event_choices("Try to clamber up the tree and grab the nest","Leave it be")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You grab branches and haphazardly rush up the tree in hopes of stealing the birds fortune.","hard",50,"Magpies Fortune",140)
      elif event_choice == "2":
        event_setup.event_outcome("You attempt to abstain from the clear fortune awaiting you in the tree.","easy",10,"New-Found Self-Respect",0)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(7)--------------------------------------#
    elif event_id == 7:
      event_setup.event_prompt("You find yourself in a bar when a tough guy walks in and begins flashing his packed wallet to everybody.","white","bold",0.05)

      event_setup.event_choices("try to fight him","Drown your sorrows")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You saunter through the bar and berate his choice of hair gel.\n This enrages him and he launches across the bar towards you.","hard",70,"Bulky Wallet",200)
      elif event_choice == "2":
        event_setup.event_outcome("You attempt to find riches at the bottom of your pint.","easy",10,"Alcholism",0)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(8)--------------------------------------#
    elif event_id == 8:
      event_setup.event_prompt("Along your journey to riches,\nyou find yourself in a prestigous library during a talk being given by a learned man of great years.","white","bold",0.05)

      event_setup.event_choices("Outwit him","Steal his stuff")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You trek up the podium steps and begin attempting to mentally destroy this man in a war of wits.","hard",0,"Old Mans Pride",0)
      elif event_choice == "2":
        event_setup.event_outcome("You sprint up to the stage and steal his bag","easy",10,"Wizened Mans Bag",30)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(9)--------------------------------------#
    elif event_id == 9:
      event_setup.event_prompt("You're out at the seaside, relaxing away from the conventionalities of modern living.","white","bold",0.05)

      event_setup.event_choices("Hit the waves","Steal unattended valuables")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("""You grab a surfboard and attempt to "shred some gnar" as the lads would say.""","medium",30,"Cool Surfboard",30)
      elif event_choice == "2":
        event_setup.event_outcome("You march up and down the beach looking for bags or anything potentially valuable like a kleptomaniactic seagull","easy",20,"Variety of Sunscreens and Hats",20)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(10)--------------------------------------#
    elif event_id == 10:
      event_setup.event_prompt("You're on a plane yet to take off when the assistant comes over and offers various rations for the journey.","white","bold",0.05)

      event_setup.event_choices("Take one.","Take her purse")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You accept a solitary bottle of water and settle in.\nSuddenly, you realise you're still bound by the thiefs code and must escape the plane before you leave the city.","easy",40,"Water Bottle",5)
      elif event_choice == "2":
        event_setup.event_outcome("You grab her bag and attempt to have off with it!","medium",20,"Flight-Attendants Purse",30)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(11)--------------------------------------#
    elif event_id == 11:
      event_setup.event_prompt("You eventually tire of hunting for more items all the time and are studying under your local thief master\nwhen you see his things left unattended.","white","bold",0.05)

      event_setup.event_choices("Grab and Run","Respect his seniority")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You grab it and rush out of the front door.\n\nYou look back momentarily and swear you can see stood in the front door looking proud.","medium",50,"Master Thief Tools",250)
      elif event_choice == "2":
        event_setup.event_outcome(""""Seniority!?" comes booming from the top of the roof.\n"You're a thief! act like it!" He berates you as he attempts to leap at you.\nYou attempt to dodge and attack back in an attempt to survive his onslaught.""","hard",100,None,1)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(12)--------------------------------------#
    elif event_id == 12:
      event_setup.event_prompt("You're dining with some of the finer society in the city.","white","bold",0.05)

      event_setup.event_choices("Rob somebody","Steal some unattended valuables")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You tail somebody rich-looking into a more secluded spot and ask kindly for their money.","medium",20,"Rich-People Money",300)
      elif event_choice == "2":
        event_setup.event_outcome("You spot a crown/tiara left unattended and try to make off with it.","easy",30,"Fanciful Headwear",150)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(13)--------------------------------------#
    elif event_id == 13:
      event_setup.event_prompt("You're browsing the web when you see a listing for \nan irritatingly expensive painting being sold not two street away!'.","white","bold",0.05)

      event_setup.event_choices("Rush there and attempt to steal it","Make your own painting")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You rush down the street, into the exhibit and attempt to grab the painting, \nsubsequently exiting the exhibit post-haste.","hard",50,"Expensive Painting",150)
      elif event_choice == "2":
        event_setup.event_outcome("""'Screw these rich people! I'll make my own.' \nYou think to yourself as you scrawl haphazardly at a piece of paper.""","hard",5,"scrawled masterpiece and a sense of accomplishment",10)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(14)--------------------------------------#
    elif event_id == 14:
      event_setup.event_prompt("A cat walks up to you amidst your purloining spree and seems to want you to follow it.","white","bold",0.05)

      event_setup.event_choices("Follow it","Take it with you")
      event_choice = getch()
      print()
      if event_choice == "1":
        event_setup.event_outcome("You stay close to the feline whilst being led across rooftops and through alleys \nin hopes it leads you to something useful.","easy",20,"Shiny, Jingly Bell",20)
      elif event_choice == "2":
        event_setup.event_outcome("The cat seems rather insistant that you go with it, but you insist in return that it come with you.","hard",30,"rather indignant Cat",10)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)
    #----------------------------------Event(15)--------------------------------------#
    elif event_id == 15:
      global wealth
      event_setup.event_prompt("You waddle down the street as usual when you notice a wandering salesmen has set up shop and is selling his wares.","white","bold",0.05)

      event_setup.event_choices("Haggle with him","Steam from him")
      event_choice = getch()
      print()
      if event_choice == "1":
        global wealth
        event_setup.event_outcome("You use your collected knowledge of the trade to move him down from 60 UMs to only 10 for an item you know to be worth 80.","medium",0,"Vase",80)
        wealth = wealth - 10
      elif event_choice == "2":
        event_setup.event_outcome("You chat to him whilst sneaking an item worth about 80 UMs into your coat, hoping he doesn't notice.","medium",10,"Vase",80)

      else:
        text.taeris("look, just pick one, it'll be a lot more fun.",0.05)
        sleep(1)
        events.event(event_id)

class draw:
  def title():
    text.title("     TTTTTTTTTTTT   HHH     HHH   IIIIIIIIIII   EEEEEEEEEEE   FFFFFFFFFFF\n",0.01)
    text.title("         TTT        HHH     HHH       III       EEE           FFF        \n",0.01)
    text.title("         TTT        HHH     HHH       III       EEE           FFF        \n",0.01)
    text.title("         TTT        HHHHHHHHHHH       III       EEEEEEEEEEE   FFFFFFFFFFF\n",0.01)
    text.title("         TTT        HHH     HHH       III       EEE           FFF        \n",0.01)
    text.title("         TTT        HHH     HHH       III       EEE           FFF        \n",0.01)
    text.title("         TTT        HHH     HHH   IIIIIIIIIII   EEEEEEEEEEE   FFF        \n",0.01)

  def game_over():
    def G():
        text.title("                 GGGGGGGGGGGG             \n",0.01)
        text.title("               GGGG        GGGG            \n",0.01)
        text.title("              GGGG          GG             \n",0.01)
        text.title("             GGGG                             \n",0.01)
        text.title("             GGGG        GGGGGGGG             \n",0.01)
        text.title("              GGG          GGGG             \n",0.01)
        text.title("               GGGG        GGGG             \n",0.01)
        text.title("                 GGGGGGGGGGGG             \n",0.01)

    def A():
        text.title("                      A             \n",0.01)
        text.title("                    AA AA             \n",0.01)
        text.title("                 AAAA   AAAA            \n",0.01)
        text.title("               AAAA       AAAA            \n",0.01)
        text.title("             AAAAAAAAAAAAAAAAAA             \n",0.01)
        text.title("           AAAA              AAAA             \n",0.01)
        text.title("         AAAA                  AAAA             \n",0.01)
        text.title("       AAAAAAA                AAAAAAA             \n",0.01)

    def M():
        text.title("       MMMMMMM              MMMMMMM             \n",0.01)
        text.title("       MMMMM  MM           MM MMMMM             \n",0.01)
        text.title("       MMMM    MM         MM   MMMM             \n",0.01)
        text.title("       MMMM     MM       MM    MMMM             \n",0.01)
        text.title("       MMMM      MM     MM     MMMM             \n",0.01)
        text.title("       MMMM       MM   MM      MMMM             \n",0.01)
        text.title("       MMMM         MMMM       MMMM             \n",0.01)
        text.title("       MMMM          MM        MMMM             \n",0.01)


    def E():
        text.title("               EEEEEEEEEEEEEE                 \n",0.01)
        text.title("               EEEEE               \n",0.01)
        text.title("               EEEE               \n",0.01)
        text.title("               EEEEEEEEEEE                 \n",0.01)
        text.title("               EEEEEEEEEEE                \n",0.01)
        text.title("               EEEE               \n",0.01)
        text.title("               EEEEE               \n",0.01)
        text.title("               EEEEEEEEEEEEEE                  \n",0.01) 

    def O():
        text.title("                 GGGGGGGGGGGG             \n",0.01)
        text.title("               GGG          GGG            \n",0.01)
        text.title("              GGG            GGG             \n",0.01)
        text.title("             GGGG            GGGG                 \n",0.01)
        text.title("             GGGG            GGGG             \n",0.01)
        text.title("              GGG            GGG             \n",0.01)
        text.title("               GGG          GGG             \n",0.01)
        text.title("                 GGGGGGGGGGGG             \n",0.01)

    def V():
        text.title("             VV              VV             \n",0.01)
        text.title("              VV            VV             \n",0.01)
        text.title("               VV          VV             \n",0.01)
        text.title("                VV        VV             \n",0.01)
        text.title("                 VV      VV            \n",0.01)
        text.title("                  VV    VV            \n",0.01)
        text.title("                   VV  VV            \n",0.01)
        text.title("                     VV             \n",0.01)

    def R():
        text.title("               RRRRRRRRRRR                 \n",0.01)
        text.title("               RRRR      RRR               \n",0.01)
        text.title("               RRRR      RRRR         \n",0.01)
        text.title("               RRRR      RRR                \n",0.01)
        text.title("               RRRRRRRRRRR                \n",0.01)
        text.title("               RRRR   RRRR           \n",0.01)
        text.title("               RRRR    RRRR         \n",0.01)
        text.title("               RRRR     RRRR           \n",0.01) 

    G()
    print()
    A()
    print()
    M()
    print()
    E()
    print()
    print()
    print()
    print()
    O()
    print()
    V()
    print()
    E()
    print()
    R()
    print()
    print()
    print()
    print()
    print()
    print()


#the cooler cool bit
def player_choices(*args):
  options = []
  for x in args:
    options.append([str(x)])
  for x,res in enumerate(options,1):
    for x in str("(" + str(x) + ")" + " " + colored(str(res),player_color)):
      sys.stdout.write(x)
      sys.stdout.flush()
      sleep(0.05)
    for x in str(len(options)):
      print()

def generic_choices(*args):
  options = []
  for x in args:
    options.append([str(x)])
  for x,res in enumerate(options,1):
    for x in str("(" + str(x) + ")" + " " + colored(res,"white")):
      sys.stdout.write(x)
      sys.stdout.flush()
      sleep(0.05)
    for x in str(len(options)):
      print()

def game_end_choice(*args):
  options = []
  for x in args:
    options.append([str(x)])
  for x,res in enumerate(options,1):
    for x in str("(" + str(x) + ")" + " " + colored(res,"red","on_white",attrs=["bold"])):
      sys.stdout.write(x)
      sys.stdout.flush()
      sleep(0.05)
    for x in str(len(options)):
      print()

def settings():
    global Taeris_Talk
    text.basic("----------", "white",None,0.05)
    text.player("Welcome to the Settings!",0.05)
    text.basic("----------", "white",None,0.05)

    print()
    print()
    print()

    player_choices("Change Text Color","Change Random Seed","Allow Taeris Talk(tutorials)","Back")

    choice = getch()

    if choice == "1":
        os.system("clear")
        text_choice()
        os.system("clear")
        settings()

    elif choice == "2":
        os.system("clear")
        print()
        print()
        print()
        text.basic("What would you like to set the random seed to? (Numbers only)","white","bold",0.05)
        print()
        chose_seed = int(input("\n"))
        print()
        random.seed(chose_seed)
        text.basic("Seed=Set!","white","bold",0.05)
        sleep(1)
        os.system("clear")
        settings()

    elif choice == "3":
      os.system("clear")
      print()
      print()
      print()
      player_choices("Enabled","Disabled")
      print()

      ena_dis = getch()

      if ena_dis == "1":
        Taeris_Talk = True
        os.system("clear")
        settings()

      elif ena_dis == "2":
        Taeris_Talk = False
        os.system("clear")
        settings()

      else:
        os.system("clear")
        settings()
      
    else:
      return

def text_choice():
  global player_color
  global player_attrs
  global color_change
  if color_change == False:
    text.basic("What would you like your colour of text to be?\n","white",None,0.05)
    print()
    sleep(0.5)
    text.basic("Remember, it is a stand-in for you as an entity in this world.\n","blue",None,0.05)
    print()
    sleep(1)
    text.taeris("and likewise for the other characters in our story...",0.05)
  print()
  print()
  print()

  #the cool bit
  for x,res in enumerate(possible_colors,1):
    for x in str("(" + str(x) + ")" + " " + colored(res,str(res))):
      sys.stdout.write(x)
      sys.stdout.flush()
      sleep(0.05)
    for x in str(len(possible_colors)):
      print()

  choice = int(getch())
  if choice != 7:
    for x in range(len(possible_colors)):
      if choice == x:
        player_color = possible_colors[x - 1]
  elif choice == 7:
    player_color = "magenta"
  color_change = True
  os.system("clear")

def HUD():
  global health
  text.basic("Health: ","red","bold",0)
  text.basic(health,"white","bold",0)
  print()
  global stamina
  text.basic("Stamina: ","yellow","bold",0)
  text.basic(stamina,"white","bold",0)
  print()
  global wealth
  text.basic("Wealth: ","green","bold",0)
  text.basic(wealth,"white","bold",0)

def shop():
  global wealth
  global stolen_things

  os.system("clear")

  HUD()
  print()
  print()
  print()

  text.basic("Welcome to the shop, we'll buy everything you obtain at... OK prices!","blue","bold",0.05)
  print()
  print()
  print()
  items.show()
  print()
  print()
  print()
  sell_choice = getch()
  if sell_choice == "1":
    os.system("clear")
    game_main()
  if sell_choice == "2":
    text.basic("Those are your thievin tools. You're gonna want those with you.","blue","bold",0.05)
    sleep(1)
    os.system("clear")
    shop()
  else:
    items.sell(sell_choice)

    text.basic("A fine item, you shall be compensated accordingly.","blue","bold",0.05)
    print()
    print()
    print()
    player_choices("Sell again","Return to hideout")
    print()

    repeat = getch()

    if repeat == "1":
      os.system("clear")
      shop()
    else:
      game_main()

def start():
  os.system("clear")
  draw.title()
  print()
  print()
  print()

  generic_choices("Start Game", "Options")

  print()

  choice = getch()

  if choice == "1" and Taeris_Talk == True:
    os.system("clear")
    Set_Up()
  elif choice == "1" and Taeris_Talk == False:
    os.system("clear")
    game_main()
  elif choice == "2":
    os.system("clear")
    settings()
    os.system("clear")
    start()

def Set_Up():

      text.taeris("Welcome to your Life of Crime.",0.05)
      print()
      print()
      print()
      text.taeris("Might you require any assistance on the path ahead of you?",0.05)
      print()
      print()
      print()
      player_choices("Yes","No")
      print()
      first_choice = getch()

      if first_choice == "1":
        first_time = False
        tutorial()
      elif first_choice == "2":
        first_time = False
        text.taeris("Fine, suit yourself, but don't say I didn't offer.",0.05)
        sleep(2)
        print()
        text.taeris("Now then, off with you. Go steal me some stuff.",0.05)
        sleep(3)
        os.system("clear")
        game_main()

def tutorial():
  global player_color
  global color_change
  global first_time
  os.system("clear")
  if first_time == False:
    text.taeris("We've been through this before, need you any additional guidance?",0.04)
    print()
    print()
    print()
    player_choices("Yes","No","Fight Me!")

    player_choice = getch()
    if player_choice == "1":
      first_time = False
      tutorial()
    elif player_choice == "2":
      print()
      text.taeris("Very well, on with it.",0.04)
      os.system("clear")
      game_main()
    elif player_choice == "3":
      text.taeris("No",1)
      print()
      print()
      print()
      player_choices("Yes!","no...")
      print()
      player_challenge = getch()
      if player_challenge == "1":
        text.taeris("I had such high hopes.",0.04)
        text.waiting(1)
        os.system("clear")
        game_over()
      elif player_challenge == "2":
        text.taeris("Get on with it then.",0.04)
        sleep(1)
        os.system("clear")
        game_main()
  else:
      
    if color_change == False:
      text.taeris("Sorry, I can't help but notice your text is quite plain. Do you wish to change?",0.04)
      print()
      print()
      print()
      player_choices("Yes","No")

      color_change_Y_N = getch()

      if color_change_Y_N == "1":
          os.system("clear")
          text_choice()
          print()
          text.taeris("Now then, let's get on with it.",0.04)
          sleep(0.5)
          os.system("clear")
          tutorial()
      elif color_change_Y_N == "2":
        print()
        text.taeris("Rather abhorrent to my eyes, but so have you.",0.04)
        os.system("clear")

    text.taeris("First, what would you like explained?",0.05)
    print()
    print()
    print()
    player_choices("Health","Stamina","Wealth","Encounters")
    print()
    tutorial_choice = getch()

    if tutorial_choice == "1":
      os.system("clear")
      tutorials.health()
    elif tutorial_choice == "2":
      os.system("clear")
      tutorials.stamina()
    elif tutorial_choice == "3":
      os.system("clear")
      tutorials.wealth()
    elif tutorial_choice == "4":
      os.system("clear")
      tutorials.encounters()

def game_over():
  global health
  global stamina
  global wealth
  os.system("clear")
  text.taeris("hmmm, I had such high hopes, but it appears you've overextended yourself.",0.06)
  sleep(2)
  text.waiting(5)

  os.system("clear")

  draw.game_over()
  

  text.basic("Start Again?","white","bold",0.05)
  print()
  player_choices("Yes","No")

  choice = getch()
  if choice == "1":
    os.system("clear")
    start()
  else:
    text.basic("You've kinda gotta. Sorry.","white","bold",0.06)
    sleep(2)
    print()
    text.basic("Or you could just close the browser...","grey","bold",0.07)
    sleep(4)
    print()
    text.basic("On we go then!","white","bold",0.04)
    sleep(1)
    os.system("clear")
    health = 100
    stamina = 100
    wealth = 0
    start()

def game_win():
  global wealth
  global health
  global stamina
  global Returned
  if Returned == False:
    text.taeris("Well... You've done it.",0.07)
    print()
    sleep(2)
    text.taeris("To be honest, I didn't expect you to actually amass this much wealth.",0.06)
    print()
    sleep(2)
    text.taeris("That isn't to say I'm not very proud, but there isn't much for you to do now.",0.07)
    print()
    sleep(2)
    text.taeris("You may, however, choose to do one of two things.",0.08)
    print()
    sleep(2)
    Returned = True
  print()
  game_end_choice("Restart","Go Back")
  print()
  end_choose = getch()
  if end_choose == "1":
    text.taeris("I respect your decision even if I don't understand it.",0.06)
    os.system("clear")
    health = 100
    stamina = 100
    wealth = 0

    start()

  elif end_choose == "2":
    text.taeris("Come back whenever you wish.",0.09)
    os.system("clear")
    game_main()

  else:
    text.taeris("that's all there is now, so you better choose one.",0.05)

def game_main():
  global Taeris_Talk
  stats.health_stat.death_check()
  os.system("clear")

  HUD()

  print()
  print()
  print()

  if wealth < 1000:
    player_choices("Look for Things to Steal","Try to Sell Some Stolen Stuff","See Items","Rest","Settings","Exit")

    choice = getch()
    if choice == "1":
        stats.stamina_stat.tire_check()
        os.system("clear")
        random.seed(random.randint(0,1168))
        events.event(random.randint(0,15))
    elif choice == "2":
        shop()
    elif choice == "3":
        os.system("clear")
        HUD()
        print()
        print()
        items.show()
        print()
        print()
        text.basic("Press any key to close","white","bold",0.05)
        getch()
        os.system("clear")
        game_main()
    elif choice == "4":
        stats.stamina_stat.rest()
        os.system("clear")
        game_main()
    elif choice == "5":
      os.system("clear")
      settings()
      os.system("clear")
      game_main()
    elif choice == "6":
        Taeris_Talk = False
        os.system("clear")
        start()
  elif wealth >= 1000:
      player_choices("Look for Things to Steal","Try to Sell Some Stolen Stuff","See Items","Rest","Return to Taeris","Settings","exit")

      choice = getch()
      if choice == "1":
        stats.stamina_stat.tire_check()
        os.system("clear")
        random.seed(random.randint(0,1204))
        events.event(random.randint(0,15))
      elif choice == "2":
        shop()
      elif choice == "3":
        os.system("clear")
        HUD()
        print()
        print()
        items.show()
        print()
        print()
        text.basic("Press any key to close","white","bold",0.05)
        getch()
        os.system("clear")
        game_main()
      elif choice == "4":
        stats.stamina_stat.rest()
        os.system("clear")
        game_main()
      elif choice == "5":
        os.system("clear")
        game_win()
      elif choice == "6":
        os.system("clear")
        settings()
        os.system("")
        game_main()
      elif choice == "7":
        os.system("clear")
        start()


start()
