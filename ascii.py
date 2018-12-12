from screenSetup import *
from time import *

AsciiDict = {
    'A': '''
           
     /\\    
    /  \\   
   / /\\ \\  
  / ____ \\ 
 /_/    \_\\
           
           
''',
    'B': '''
  ____  
 |  _ \\ 
 | |_) |
 |  _ < 
 | |_) |
 |____/ 
        
        
''',
    'C': '''
   _____ 
  / ____|
 | |     
 | |     
 | |____ 
  \\_____|
         
         
''',
    'D': '''
  _____  
 |  __ \\ 
 | |  | |
 | |  | |
 | |__| |
 |_____/ 
         
         
''',
    'E': '''
  ______ 
 |  ____|
 | |__   
 |  __|  
 | |____ 
 |______|
         
         
''',
    'F': '''
  ______ 
 |  ____|
 | |__   
 |  __|  
 | |     
 |_|     
         
         
''',
    'G': '''
   _____ 
  / ____|
 | |  __ 
 | | |_ |
 | |__| |
  \\_____|
         
         
''',
    'H': '''
  _    _ 
 | |  | |
 | |__| |
 |  __  |
 | |  | |
 |_|  |_|
         
         
''',
    'I': '''
  _____ 
 |_   _|
   | |  
   | |  
  _| |_ 
 |_____|
        
        
''',
    'J': '''
       _ 
      | |
      | |
  _   | |
 | |__| |
  \\____/ 
         
         
''',
    'K': '''
  _  __
 | |/ /
 | ' / 
 |  <  
 |   \\ 
 |_|\\_\\
       
       
''',
    'L': '''
  _      
 | |     
 | |     
 | |     
 | |____ 
 |______|
         
         
''',
    'M': '''
  __  __ 
 |  \\/  |
 | \\  / |
 | |\\/| |
 | |  | |
 |_|  |_|
         
         
''',
    'N': '''
  _   _ 
 | \\ | |
 |  \\| |
 | . ` |
 | |\\  |
 |_| \\_|
        
        
''',
    'O': '''
   ____  
  / __ \\ 
 | |  | |
 | |  | |
 | |__| |
  \\____/ 
         
         
''',
    'P': '''
  _____  
 |  __ \\ 
 | |__) |
 |  ___/ 
 | |     
 |_|     
         
         
''',
    'Q': '''
   ____  
  / __ \\ 
 | |  | |
 | |  | |
 | |__| |
  \\___\\_\\
         
         
''',
    'R': '''
  _____  
 |  __ \\ 
 | |__) |
 |  _  / 
 | | \\ \\ 
 |_|  \\_\\
         
         
''',
    'S': '''
   _____ 
  / ____|
 | (___  
  \\___ \\ 
  ____) |
 |_____/ 
         
         
''',
    'T': '''
  _______ 
 |__   __|
    | |   
    | |   
    | |   
    |_|   
          
          
''',
    'U': '''
  _    _ 
 | |  | |
 | |  | |
 | |  | |
 | |__| |
  \\____/ 
         
         
''',
    'V': '''
 __      __
 \\ \\    / /
  \\ \\  / / 
   \\ \\/ /  
    \\  /   
     \\/    
           
           
''',
    'W': '''
 __          __
 \\ \\        / /
  \\ \\  /\\  / / 
   \\ \\/  \\/ /  
    \\  /\\  /   
     \\/  \\/    
               
               
''',
    'X': '''
 __   __
 \\ \\ / /
  \\ V / 
   > <  
  / . \\ 
 /_/ \\_\\
        
        
''',
    'Y': '''
 __     __
 \\ \\   / /
  \\ \\_/ / 
   \\   /  
    | |   
    |_|   
          
          
''',
    'Z': '''
  ______
 |___  /
    / / 
   / /  
  / /__ 
 /_____|
        
        
''',
    'a': '''
        
        
   __ _ 
  / _` |
 | (_| |
  \\__,_|
        
        
''',
    'b': '''
  _     
 | |    
 | |__  
 | '_ \\ 
 | |_) |
 |_.__/ 
        
        
''',
    'c': '''
       
       
   ___ 
  / __|
 | (__ 
  \\___|
       
       
''',
    'd': '''
      _ 
     | |
   __| |
  / _` |
 | (_| |
  \\__,_|
        
        
''',
    'e': '''
       
       
   ___ 
  / _ \\
 |  __/
  \\___|
       
       
''',
    'f': '''
   __ 
  / _|
 | |_ 
 |  _|
 | |  
 |_|  
      
      
''',
    'g': '''
        
        
   __ _ 
  / _` |
 | (_| |
  \\__, |
   __/ |
  |___/ 
''',
    'h': '''
  _     
 | |    
 | |__  
 | '_ \\ 
 | | | |
 |_| |_|
        
        
''',
    'i': '''
  _ 
 (_)
  _ 
 | |
 | |
 |_|
    
    
''',
    'j': '''
    _ 
   (_)
    _ 
   | |
   | |
   | |
  _/ |
 |__/ 
''',
    'k': '''
  _    
 | |   
 | | __
 | |/ /
 |   < 
 |_|\\_\\
       
       
''',
    'l': '''
  _ 
 | |
 | |
 | |
 | |
 |_|
    
    
''',
    'm': '''
            
            
  _ __ ___  
 | '_ ` _ \\ 
 | | | | | |
 |_| |_| |_|
            
            
''',
    'n': '''
        
        
  _ __  
 | '_ \\ 
 | | | |
 |_| |_|
        
        
''',
    'o': '''
        
        
   ___  
  / _ \\ 
 | (_) |
  \___/ 
        
        
''',
    'p': '''
        
        
  _ __  
 | '_ \\ 
 | |_) |
 | .__/ 
 | |    
 |_|    
''',
    'q': '''
        
        
   __ _ 
  / _` |
 | (_| |
  \\__, |
     | |
     |_|
''',
    'r': '''
       
       
  _ __ 
 | '__|
 | |   
 |_|   
       
       
''',
    's': '''
      
      
  ___ 
 / __|
 \\__ \\
 |___/
      
      
''',
    't': '''
  _   
 | |  
 | |_ 
 | __|
 | |_ 
  \\__|
      
      
''',
    'u': '''
        
        
  _   _ 
 | | | |
 | |_| |
  \\__,_|
        
        
''',
    'v': '''
        
        
 __   __
 \\ \ / /
  \\ V / 
   \\_/  
        
        
''',
    'w': '''
           
           
 __      __
 \\ \\ /\\ / /
  \\ V  V / 
   \\_/\_/  
           
           
''',
    'x': '''
       
       
 __  __
 \\ \\/ /
  >  < 
 /_/\\_\\
       
       
''',
    'y': '''
        
        
  _   _ 
 | | | |
 | |_| |
  \\__, |
   __/ |
  |___/ 
''',
    'z': '''
      
      
  ____
 |_  /
  / / 
 /___|
      
      
''',
    '1': '''
  __ 
 /_ |
  | |
  | |
  | |
  |_|
     
     
''',
    '2': '''
  ___  
 |__ \\ 
    ) |
   / / 
  / /_ 
 |____|
       
       
''',
    '3': '''
  ____  
 |___ \\ 
   __) |
  |__ < 
  ___) |
 |____/ 
        
        
''',
    '4': '''
  _  _   
 | || |  
 | || |_ 
 |__   _|
    | |  
    |_|  
         
         
''',
    '5': '''
  _____ 
 |  ___|
 | |__  
 |___ \\ 
  ___) |
 |____/ 
        
        
''',
    '6': '''
    __  
   / /  
  / /_  
 | '_ \\ 
 | (_) |
  \\___/ 
        
        
''',
    '7': '''
  ______ 
 |____  |
     / / 
    / /  
   / /   
  /_/    
         
         
''',
    '8': '''
   ___  
  / _ \\ 
 | (_) |
  > _ < 
 | (_) |
  \\___/ 
        
        
''',
    '9': '''
   ___  
  / _ \\ 
 | (_) |
  \\__, |
    / / 
   /_/  
        
        
''',
    '0': '''
   ___  
  / _ \\ 
 | | | |
 | | | |
 | |_| |
  \\___/ 
        
        
''',
    '.': '''
    
    
    
    
  _ 
 (_)
    
    
''',
    '!': '''
  _ 
 | |
 | |
 | |
 '-'
 (_)
    
    
''',
    ' ': '''
       
       
       
       
       
       
       
       
'''
}


class Ascii:
    def __init__(self, text):
        self.text = text

    def compile(self):
        screenCenter = center_finder()
        title = []
        centered = []
        # COMPILE
        for i in range(9):  # Loops through the string grabbing slices of the corresponding Ascii text from the top down
            for j in self.text:  # Loops through the letters in the string passed to the function ex: "Hello World"
                letter = AsciiDict[j].split('\n')  # grabs the corresponding letter from the ascii dict and stores it
                title.append(letter[i])  # adds the (i)th slice of the letter to title[]
            title.append('\n')  # So that the list will print out on multiple lines
        uncentered = ''.join(title).split('\n')  # joins the whole list and then splits it by \n

        # CENTER
        for i in uncentered:  # Prepares the ascii text to be returned by adding centering spaces before each line
            centerVar = screenCenter-(len(i)//2)
            centered.append(' ' * centerVar + i)
        return '\n'.join(centered)

    def flatten(self):
        title = self.compile()
        fulltitle = title.split('\n')
        del fulltitle[0]
        lwidth = 70
        rwidth = 0
        height = 22
        # COMPILE
        for i in fulltitle:
            lwidthtemp = 0
            for j in i:
                if j in '/\|_':
                    if lwidthtemp < lwidth:
                        lwidth = lwidthtemp
                    break
                else:
                    print(j, end='')
                    lwidthtemp += 1
        for i in fulltitle:
            rwidthtemp = 0
            for j in i:
                if j == '\n':
                    break
                else:
                    rwidthtemp += 1
            if rwidthtemp > rwidth:
                rwidth = rwidthtemp
        bump = 0
        compactor = ' ' * (lwidth+bump) + '-' * (rwidth - (lwidth + (bump * 2)))
        final = ' ' * lwidth + '=' * (rwidth - lwidth)
        fulltitle.insert(0, '')
        fulltitle.insert(0, '')
        fulltitle.insert(-1, '')
        # PRINT
        speed = .03
        print('\n' * 100)
        print(compactor)
        print('\n'.join(fulltitle))
        print(compactor)
        print('\n' * (height-(len(fulltitle)//2)+1))
        sleep(3)
        for i in range(5):
            print('\n' * 100)
            print(compactor)
            print('\n'.join(fulltitle))
            print(compactor)
            if len(fulltitle) > 1:
                del fulltitle[0]
                del fulltitle[-1]
            print('\n' * (height-(len(fulltitle)//2)))
            sleep(speed)
        print('\n' * 100)
        print(compactor)
        print(compactor)
        print('\n' * (height+2))
        sleep(speed)
        print('\n' * 100)
        print(final)
        print('\n' * (height+2))
        sleep(speed)
        print('\n' * 100)
        print(compactor)
        print('\n' * (height+2))
        for i in range(5):
            sleep(speed/2)
            bump += 10
            compactor = ' ' * (lwidth + bump) + '-' * (rwidth - (lwidth + (bump * 2)))
            print('\n' * 100)
            print(compactor)
            print('\n' * (height+2))
        print('\n' * 100)
        sleep(2)


if __name__ == '__main__':
    text = Ascii(input('>>> '))
    x = text.compile()
    print(x)
