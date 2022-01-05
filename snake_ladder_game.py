# player tose the die
import random
import sys

def move(player, position, final_position,dice_number):
   
   old_position=position
   position = position+dice_number
   
   
   snake={
       20:5,
       30:2,
       57:1,
       40:8
   }
   ladder={
       5:20,
       2:30,
       1:57,
       8:40
   }
   
   print("Player: ", player, "moved from", old_position, "to ", position)
   
   if position in snake:
       value = snake.get(position)
       final_position=value
       position=final_position
       print("Oh! oh! Was bitten by a snake now moved back to ", position)
   elif position in ladder:
        final_position=ladder.get(position)
        position = final_position
        print("Waoh! a ladder, climbing you up now to ",final_position)
   else:
       
       final_position=position
       
  
   
   return final_position, player
        
if __name__=="__main__":
     player1_position=0
     player2_position=0
     player1_final_position=0
     player2_final_position = 0
     player1 = input("Player 1: Enter Your Name:>")
     player2 = input("Player 2: Enter Your Name:>")
     print("The game is between ", player1,"and ", player2)
     while True:
      enter_btn_pressed1 = input("\n"+player1+" it is your turn: Press the Enter button")
      dicenumber = random.randint(1, 6)
      print(player1,"is moving.....")
      if(player1_final_position>100):
         print(player1, ", You have", player1_final_position -
               player1_position, "to win this game")
      else:
        player1_final_position, player = move(
            player1, player1_position, player1_final_position, dicenumber)
        player1_position = player1_final_position
        if player1_final_position==100:
           print("Yea! Congratulations ", player, "you won.")
           sys.exit(1)
        
      enter_btn_pressed1 = input("\n"+player2+" it is your turn: Press the Enter button")
      dicenumber = random.randint(1, 6)
      print(player2, "is moving.....")
      
      if(player2_final_position > 100):
         print(player2, ", You have", player2_final_position -
               player2_position, "to win this game")
      else:
        player2_final_position, player = move(
            player2, player2_position, player2_final_position, dicenumber)
        player2_position = player2_final_position
        if player2_final_position==100:
           print("Yea! Congratulations ", player, "you won.")
           sys.exit(1)

        
        
        
        
        