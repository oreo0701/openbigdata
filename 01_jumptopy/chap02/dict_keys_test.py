# coding: cp949
# -*- coding: utf-8 -*-
#big_data_players={"김연아":"피켜스케이팅","류현진":"야구","박지성":"축구"}
big_data_players={"Y Kim":"Figure Skating","H Ryu":"Baseball","J Park":"Soccer"}
korean_str="한글"
print(korean_str)
print("Step1] Printinting the raw  type of dictionary, 'big_data_players'")
print(big_data_players)

print("\nStep2] Printing the key lists of big_data_players.keys()")
print(big_data_players.keys())

print("\nStep3] Printinting the value lists using big_data_players.values() fuction")
print(big_data_players.values())

print("\nStep4] Trying to serch character of 'H Ryu' in the big_data_players dictionary")
if 'H Ryu' in big_data_players:
    for player_key in big_data_players.keys():
        print(player_key)
        if player_key == 'H Ryu':n        
        print("\nI found Hyunjin Ryu! Now, I will talk about him.")
        print("He is a "+big_data_players['H Ryu']+" player")
        break

print("\nProgram End")
