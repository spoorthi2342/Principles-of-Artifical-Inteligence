import random
def print_board(heap):
    print(f"current heap:{'|'*heap}")
def stick_by_user(heap):
    while True:
        try:
            sticks_to_remove=int(input(f"enter the sticks to remove min(1,max{min(heap,heap//2)})"))
            if 1<=sticks_to_remove<=min(heap,heap//2):
                break
            else:
                print(f"please put number between 1 and {min(heap,heap//2)}")
        except ValueError:
            print("please enter correct in")
    return sticks_to_remove
def sticks_by_computer(heap):
    xor_sum=heap
    for i in range(heap):
       xor_sum^=i
    if xor_sum==0:
        max_stick=min(heap,heap//2)
        sticks_to_remove=random.randint(1,max_stick)
    else:
        max_stick=min(heap//2,heap)
        sticks_to_remove=max(1,min(max_stick,heap-xor_sum))
    return sticks_to_remove
def nim_game():
    heap=16
    player_turn=1
    while heap>1:
        print_board(heap)
        if  player_turn==1:
         player_name="player 1"
         min=stick_by_user(heap)
        else:
            player_name="computer"
            min=sticks_by_computer(heap)
        heap-=min
        print(f"player {player_name} is removing {min} sticks")
        player_turn=3-player_turn

    print_board(heap)
    winner="player 1"if player_turn==2 else "computer"
    print(f"player {player_turn} picks the last stick")
    print(f"\n {winner} is the winner!")
if __name__ == "__main__":
    nim_game()

