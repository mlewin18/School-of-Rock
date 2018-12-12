from time import sleep

intel = {
    'How to play':
        '''
        --School of Rock is a text based interactive story.--
        --Throughout the game you'll be presented with choices, the outcomes of which will determine your success.--
        --Choices and options are marked with vertical bars around their first letter, ex: "|G|et up"--
        --To select a choice or option type the letter between the bars and press "Enter"--
        --At the beginning of every chapter you'll see a description of your current situation.--
        --Next you'll be presented with an options table (below).--
        
                    ----------------------------------------------------------------
                     |L|ook  |F|eel  |H|ear  |S|mell  |T|aste  |M|ove  |I|nventory
                    ----------------------------------------------------------------
        
        --The options table lists your available senses (which may vary) as well as "Move" and "Inventory" options.--
        --Using your senses will not have any direct impact on the story, instead they supplement your decision making.--
        --Taking the time to examine your surroundings can be the difference between a gruesome death and a victorious journey.--
        --When you feel ready to brave your next action, select the "Move" option and choose wisely.--
        --At certain points during your travels you may also be prompted to make smaller choices such as using or obtaining an item.--
        --These choices work the same way as movement options and may be just as impactful.--
        
        ''',
    'Inventory':
        '''
        --Your inventory is an active list of all the items that you have with you in the game including what you've picked up.--
        --If you break or consume an item it will be removed from your inventory and won't show up on the list.--
        --The list can be accessed by typing "i" or "inventory" when presented with the options table (shown below).--
        
                    ----------------------------------------------------------------
                     |L|ook  |F|eel  |H|ear  |S|mell  |T|aste  |M|ove  |I|nventory
                    ----------------------------------------------------------------
        >>> i
        
        --Once inside your inventory you'll be presented with a numbered list of items.--
        --To inspect an item and see details about it enter the number next to it.--
        --When you're finished inspecting your inventory enter "0" to exit and return to the game.--
        
                             (Select an item number for more details)
        
                                        [0]  Exit inventory          
        
                                        [1]  Chewed gum              
                                        [2]  Wallet                  
                                        [3]  Calculator watch        
                                        [4]  Small tin can           
                                        [5]  Severed pinky toe       
                                        [6]  Bobby pin               
''',
}


def instructions():
    print()
    for i in intel:
        print (' '* 50, i)
        text = intel[i].split('\n')
        for k in text:
            print(' '* 50, k)
            sleep(.1)
    print('\n')

    while True:
        print(end='')
if __name__ == '__main__':
    instructions()
