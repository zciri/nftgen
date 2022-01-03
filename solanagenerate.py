# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 640x640 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 500, 500


#DIRECTORY VARIABLE NAMES#
dirStart = 'C:/Solana_Fellas'
dirBackground = dirStart + '/Background'
dirAccessory = '...'
dirGender = '...'
dirBase = '...'
dirBeard = '...'
dirClothing = '...'
dirDesign = '...'
dirEye = '...'
dirEyebrow = '...'
dirHair = '...'
dirHat = '...'
dirMouth = '...'

#JSON VARIABLES#
backgroundJSON = '...'
baseJSON = '...'
colorJSON = '...'
beardJSON = '...'
clothingJSON = '...'
clothingColorJSON = '...'
designJSON = '...'
eyeJSON = '...'
eyeColorJSON = '...'
eyebrowJSON = '...'
eyebrowColorJSON = '...'
hairJSON = '...'
mouthJSON = '...'
hatJSON = '...'
accessory1JSON = '...'
accessory2JSON = '...'
accessory3JSON = '...'
accessory4JSON = '...'
accessory5JSON = '...'

for x in range(0, 500):

#INITIALIZING LAYERS
    background = Image.open(dirStart + '/Empty.png').convert("RGBA")
    base = Image.open(dirStart + '/Empty.png').convert("RGBA")
    beard = Image.open(dirStart + '/Empty.png').convert("RGBA")
    clothing = Image.open(dirStart + '/Empty.png').convert("RGBA")
    design = Image.open(dirStart + '/Empty.png').convert("RGBA")
    eye = Image.open(dirStart + '/Empty.png').convert("RGBA")
    eyebrow = Image.open(dirStart + '/Empty.png').convert("RGBA")
    hair = Image.open(dirStart + '/Empty.png').convert("RGBA")
    mouth = Image.open(dirStart + '/Empty.png').convert("RGBA")
    hat = Image.open(dirStart + '/Empty.png').convert("RGBA")
    accessory1 = Image.open(dirStart + '/Empty.png').convert("RGBA")
    accessory2 = Image.open(dirStart + '/Empty.png').convert("RGBA")
    accessory3 = Image.open(dirStart + '/Empty.png').convert("RGBA")
    accessory4 = Image.open(dirStart + '/Empty.png').convert("RGBA")
    accessory5 = Image.open(dirStart + '/Empty.png').convert("RGBA")
    baseRoll = 0
    baseRollG = 0


    # using 18 naked cowboys and the cowboys birth months
    b=72616207261663680694201337
    seed(x+b)
    faceFeatures = 0
    
    # GENDER ROLL #
    genderRoll = randint(1,100)
    if genderRoll <= 62:
        dirGender = dirStart + '/Fella'
        gender = 1
    elif genderRoll > 62:
        dirGender = dirStart + '/Felia'
        gender = 2
        
    # BACKGROUND ROLL # LAYER 1 # FINISHED #
    backgroundRoll = randint(1, 100)
    
    if backgroundRoll <= 40:
        background = Image.open(dirBackground + '/background3.png').convert("RGBA")
        backgroundJSON = 'Blue'
    elif 40 < backgroundRoll <= 70:
        background = Image.open(dirBackground + '/background2.png').convert("RGBA")
        backgroundJSON = 'Purple'
    elif 70 < backgroundRoll <= 90:
        background = Image.open(dirBackground + '/background1.png').convert("RGBA")
        backgroundJSON = 'Green'    
    elif 90 <= backgroundRoll <= 100:
        background = Image.open(dirBackground + '/background4.png' ).convert("RGBA")
        backgroundJSON = 'Red'

   # BASE ROLL #  LAYER 2 # FINISHED #
    if gender == 1:
        baseRoll = randint(1,1000) #black,white,tan,brown = 21% 86/100, 7 robot  5 monkey 2 skeleton
        dirBase = dirGender + '/Base'
        
        if baseRoll <= 215:
            base = Image.open(dirBase + '/White.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'White'
        elif 215 < baseRoll <= 430:
            base = Image.open(dirBase + '/Black.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'Black'
        elif 430 < baseRoll <= 645:
            base = Image.open(dirBase + '/Tan.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'Tan'
        elif 645 < baseRoll <= 860:
            base = Image.open(dirBase + '/Brown.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'Brown'
        elif 860 < baseRoll <= 910:
            base = Image.open(dirBase + '/Monkey.png').convert("RGBA")
            faceFeatures = 2
            baseType = 'monkey'
            baseJSON = 'Monkey'
        elif 910 < baseRoll <= 980:
            base = Image.open(dirBase + '/Robot.png').convert("RGBA")
            faceFeatures = 2
            baseType = 'robot'
            baseJSON = 'Robot'
        elif 980 < baseRoll <= 1000:
            base = Image.open(dirBase + '/Skelly.png').convert("RGBA")
            faceFeatures = 2
            baseType = 'skeleton'
            baseJSON = 'Skeleton'
    elif gender == 2: 
        baseRollG = randint(1,10000) #black,white,tan,brown = 21% 93/100, 7 robot
        dirBase = dirGender + '/Base'
        
        if baseRollG <= 2325:
            base = Image.open(dirBase + '/White.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'White'
            
        elif 2325 < baseRollG <= 4650:
            base = Image.open(dirBase + '/Black.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'Black'
            
        elif 4650 < baseRollG <= 6975:
            base = Image.open(dirBase + '/Tan.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'Tan'
        elif 6975 < baseRollG <= 9300:
            base = Image.open(dirBase + '/Brown.png').convert("RGBA")
            faceFeatures = 1
            baseType = 'human'
            baseJSON = 'Brown'
        elif 9300 < baseRollG <= 10000:
            base = Image.open(dirBase + '/Robot.png').convert("RGBA")
            faceFeatures = 2
            baseType = 'robot'
            baseJSON = 'Robot'
    

    colorRoll = randint(1,100)
    hairRoll = randint(1,1000)
    if faceFeatures == 1:
        # HAIR & COLOR ROLL # LAYER 3 #
        
        dirHair = dirGender + '/Hair'
    
        if colorRoll <= 17:
            color = "/Grey.png"
            colorJSON = 'Grey'
        elif 17 < colorRoll <= 34:
            color = "/Black.png"
            colorJSON = 'Black'
        elif 34 < colorRoll <= 51:
            color = "/Blonde.png"
            colorJSON = 'Blonde'
        elif 51 < colorRoll <= 68:
            color = "/Brown.png"
            colorJSON = 'Brown'
        elif 68 < colorRoll <= 85:
            color = "/Ginger.png"
            colorJSON = 'Ginger'
        elif 85 < colorRoll <= 90:
            color = "/Red.png"
            colorJSON = 'Red'
        elif 90 < colorRoll <= 95:
            color = "/Blue.png"
            colorJSON = 'Blue'
        elif 95 < colorRoll <= 100:
            color = "/Green.png"
            colorJSON = 'Green' 
    
        #FELLA HAIR   
        if gender == 1 and baseType == 'human':
            nohat = False
            if hairRoll <= 125:
                hair = Image.open(dirHair + '/Receding' + color).convert("RGBA")
                hairJSON = 'Receding'
                
            elif 125 < hairRoll <= 250:
                hair = Image.open(dirHair + '/Afro' + color).convert("RGBA")
                nohat = True 
                hairJSON = 'Afro'
                
            elif 250 < hairRoll <= 375:
                hair = Image.open(dirHair + '/Bangs' + color).convert("RGBA")
                hairJSON = 'Bangs'
                
            elif 375 < hairRoll <= 500:
                hair = Image.open(dirHair + '/Fade' + color).convert("RGBA")
                hairJSON = 'Fade'
                
            elif 500 < hairRoll <= 625:
                hair = Image.open(dirHair + '/Greaser' + color).convert("RGBA")
                hairJSON = 'Greaser'
                
            elif 625 < hairRoll <= 750:
                hair = Image.open(dirHair + '/Long' + color).convert("RGBA")
                hairJSON = 'Long'
                
            elif 750 < hairRoll <= 875:
                hair = Image.open(dirHair + '/Normal' + color).convert("RGBA")
                hairJSON = 'Normal'
                
            elif 875 < hairRoll <= 1000:
                hair = Image.open(dirStart + '/Empty.png').convert("RGBA")
                hairJSON = 'Bald'   
                
        elif baseRoll > 860:
            hair = Image.open(dirStart + '/Empty.png').convert("RGBA")
            hairJSON = 'None'    
                
        #FELIA HAIR    
        elif gender == 2 and baseType == 'human':
            if baseRollG <= 9300:
                if hairRoll <= 350:
                    hair = Image.open(dirHair + '/Bob' + color).convert("RGBA")
                    hairJSON = 'Bob'
                elif 350 < hairRoll <= 400:
                    hair = Image.open(dirHair + '/Fade' + color).convert("RGBA")
                    hairJSON = 'Fade'
                elif 400 < hairRoll <= 600:
                    hair = Image.open(dirHair + '/Long' + color).convert("RGBA")
                    hairJSON = 'Long'
                elif 600 < hairRoll <= 800:
                    hair = Image.open(dirHair + '/Pigtail' + color).convert("RGBA")
                    hairJSON = 'Pigtail'
                elif 800 < hairRoll <= 1000:
                    hair = Image.open(dirHair + '/Ponytail' + color).convert("RGBA")
                    hairJSON = 'Ponytail'
            elif baseRollG > 9300:
                hair = Image.open(dirStart + '/Empty.png').convert("RGBA")
                hairJSON = 'None'  
                
    #BEARD ROLL# 
        if gender <=1 and baseType == 'human':
            beardRoll = randint(1,100)
            dirBeard = dirGender + '/Beard'
            if baseRoll <= 910: 
                if beardRoll <=6:
                    beard = Image.open(dirBeard + '/Mustache' + color).convert("RGBA")
                    beardJSON = 'Combined'
                if 6 < beardRoll <= 12:
                    beard = Image.open(dirBeard + '/Beard' + color).convert("RGBA")
                    beardJSON = 'Beard'
        elif gender > 1 or baseType != 'human':
            beard = Image.open(dirStart + '/Empty.png')
            beardJSON = 'No facial hair'
    
        #EYEBROW ROLL #
        dirEyebrow = dirGender + '/Eyebrow'
        eyebrowColor = '...'
    
        if baseRoll <=910 or baseRollG <= 9300:
        
            eyebrowColorRoll = randint(1,3)
            if eyebrowColorRoll <= 2:
                eyebrowColor = dirEyebrow + '/Black'
                eyebrowColorJSON = 'Black'
            elif eyebrowColorRoll > 2:
                eyebrowColor = dirEyebrow +'/Brown'
                eyebrowColorJSON = 'Brown'
        
            eyeBrowRoll = randint(1,100)
        
            if eyeBrowRoll <= 20:
                eyebrow = Image.open(eyebrowColor + "/Normal.png").convert("RGBA")
                eyebrowJSON = 'Normal'
            elif 20 < eyeBrowRoll <=40:
                eyebrow = Image.open(eyebrowColor + "/Right_Raised.png").convert("RGBA")
                eyebrowJSON = 'Raised Right'
            elif 40 < eyeBrowRoll <=60:
                eyebrow = Image.open(eyebrowColor + "/Sliced.png").convert("RGBA")
                eyebrowJSON = 'Sliced'
            elif 60 < eyeBrowRoll <=80:
                eyebrow = Image.open(eyebrowColor + "/Left_Raised.png").convert("RGBA")
                eyebrowJSON = 'Raised Left'
            elif 80 < eyeBrowRoll <=100:
                eyebrow = Image.open(eyebrowColor + "/Raised.png").convert("RGBA")
                eyebrowJSON = 'Both raised'
    else:
        hair = Image.open(dirStart + '/Empty.png')
        mouth = Image.open(dirStart + '/Empty.png')
        eyebrow = Image.open(dirStart + '/Empty.png')
        beard = Image.open(dirStart + '/Empty.png')
        
#EYE ROLL#
    eyeRoll = randint(1,100)
    eyeColorRoll = randint(1,10000)
    dirEye = dirGender + '/Eye'
    
    if baseType == 'human' or baseType == 'monkey':
        
        if eyeColorRoll <= 1385:
            eyeColor = "/Blue.png"
            eyeColorJSON = 'Blue'
        elif 1385 < eyeColorRoll <= 2710:
            eyeColor = "/Brown.png"
            eyeColorJSON = 'Brown'
        elif 2710 < eyeColorRoll <= 4095:
            eyeColor = "/Green.png"
            eyeColorJSON = 'Green'
        elif 4095 < eyeColorRoll <= 5480:
            eyeColor = "/Lightblue.png"
            eyeColorJSON = 'Lightblue'
        elif 5480 < eyeColorRoll <= 6865:
            eyeColor = "/Lightbrown.png"
            eyeColorJSON = 'Lightbrown'
        elif 6865 < eyeColorRoll <= 8250:
            eyeColor = "/Lightgreen.png"
            eyeColorJSON = 'Lightgreen' 
        elif 8250 < eyeColorRoll <= 9125:
            eyeColor = "/Purple.png"
            eyeColorJSON = 'Purple' 
        elif 9125 < eyeColorRoll <= 10000:
            eyeColor = "/Red.png"
            eyeColorJSON = 'Red'
            
        if baseRoll <=910 or baseRollG <= 9300:
            if eyeRoll <=30:
                eye = Image.open(dirEye + '/Center' + eyeColor).convert("RGBA")
                eyeJSON = 'Center'
            elif 30 < eyeRoll <=60:
                eye = Image.open(dirEye + '/Left' + eyeColor).convert("RGBA")
                eyeJSON = 'Left'
            elif 60 < eyeRoll <=90:
                eye = Image.open(dirEye + '/Right' + eyeColor).convert("RGBA")
                eyeJSON = 'Right'
            elif 90 < eyeRoll <=100:
                eye = Image.open(dirEye + '/Derp' + eyeColor).convert("RGBA")
                eyeJSON = 'Derp'
                
    elif baseType == 'robot':
        reyeRoll = randint(1,2)
        if reyeRoll == 1:
            eye = Image.open(dirEye + '/Robot' + "/Terminator.png").convert("RGBA")
            eyeJSON = 'Robot'
            eyeColorJSON = 'Terminator'
        elif reyeRoll == 2:
            eye = Image.open(dirEye + '/Robot' + "/White.png").convert("RGBA")
            eyeJSON = 'Robot'
            eyeColorJSON = 'White'
    elif baseType == 'skeleton':
        eye = Image.open(dirStart + '/Empty.png')
    
    
    
    #MOUTH ROLL# 
    mouthRoll = randint (1,100)
    if baseType == 'human':
        dirMouth = dirGender + '/Mouth/Normal'
        
        if mouthRoll <= 19:
            mouth = Image.open(dirMouth + "/Frown.png").convert("RGBA")
            mouthJSON = 'Frown'
        elif 19 < mouthRoll <= 38:
            mouth = Image.open(dirMouth + "/Normal.png").convert("RGBA")
            mouthJSON = 'Normal'
        elif 38 < mouthRoll <= 57:
            mouth = Image.open(dirMouth + "/Shocked.png").convert("RGBA")
            mouthJSON = 'Shocked' 
        elif 57 < mouthRoll <= 76:
            mouth = Image.open(dirMouth + "/Side.png").convert("RGBA")
            mouthJSON = 'Side'  
        elif 76 < mouthRoll <= 95: 
            mouth = Image.open(dirMouth + "/Smirk.png").convert("RGBA")
            mouthJSON = 'Smirk'
        elif 95 < mouthRoll <= 100:
            mouth = Image.open(dirMouth + "/Derp.png").convert("RGBA")
            mouthJSON = 'Derp' 
        
    elif baseType == 'robot':
        dirMouth = dirGender + '/Mouth/Robot'
        if mouthRoll <=50:
            mouth = Image.open(dirMouth + "/Dark.png").convert("RGBA")
            mouthJSON = 'Robot dark' 
        elif mouthRoll > 50:
            mouth = Image.open(dirMouth + "/Yellow.png").convert("RGBA")
            mouthJSON = 'Robot Yellow' 
            
    #HAT ROLL 
    getHat = randint(1,5)
    hatRoll = randint (1,5)
    dirHat = dirGender + '/Hat'
    if getHat <= 1 and nohat == False:
        if hatRoll == 1:
            hat = Image.open(dirHat + '/Bowling.png').convert("RGBA")
            hatJSON = 'Bowling'
        elif hatRoll == 2:
            hat = Image.open(dirHat + '/Cowboy.png').convert("RGBA")
            hatJSON = 'Cowboy'
        elif hatRoll == 3:
            hat = Image.open(dirHat + '/Phat.png').convert("RGBA")
            hatJSON = 'Party hat'
        elif hatRoll == 4:
            hat = Image.open(dirHat + '/Straw.png').convert("RGBA")
            hatJSON = 'Straw'
        elif hatRoll == 5:
            hat = Image.open(dirHat + '/Wiz.png').convert("RGBA")
            hatJSON = 'Wizard'
    else:
        hat = Image.open(dirStart + '/Empty.png')
        hatJSON = 'No hat'
    #SHIRT ROLL
    clothingTypeRoll = randint(1,3)
    clothingColorRoll = randint(1,9997)
    
    dirClothing = dirGender + '/Clothing'
    
    if clothingColorRoll <= 769:
        clothingColor = "/Black.png"
        clothingColorJSON = 'Black'
    elif 769 < clothingColorRoll <= 1538:
        clothingColor ="/Blue.png"
        clothingColorJSON = 'Blue'
    elif 1538 < clothingColorRoll <= 2307:
        clothingColor ="/Brown.png"
        clothingColorJSON = 'Brown'  
    elif 2307 < clothingColorRoll <= 3076:
        clothingColor ="/Green.png"
        clothingColorJSON = 'Green' 
    elif 3076 < clothingColorRoll <= 3845:
        clothingColor ="/Grey.png"
        clothingColorJSON = 'Grey' 
    elif 3845 < clothingColorRoll <= 4614:
        clothingColor ="/Lightblue.png"
        clothingColorJSON = 'Lightblue'
    elif 4614 < clothingColorRoll <= 5383:
        clothingColor ="/Lightgreen.png"
        clothingColorJSON = 'Lightgreen'
    elif 5383 < clothingColorRoll <= 6152:
        clothingColor ="/Lightpurple.png"
        clothingColorJSON = 'Lightpurple'
    elif 6152 < clothingColorRoll <= 6921:
        clothingColor ="/Lightred.png"
        clothingColorJSON = 'Lightred'
    elif 6921 < clothingColorRoll <= 7690:
        clothingColor ="/Pink.png"
        clothingColorJSON = 'Pink'
    elif 7690 < clothingColorRoll <= 8459:
        clothingColor ="/Purple.png"
        clothingColorJSON = 'Purple'
    elif 8459 < clothingColorRoll <= 9228:
        clothingColor ="/Red.png"
        clothingColorJSON = 'Red'
    elif 9228 < clothingColorRoll <= 9997:
        clothingColor ="/White.png"
        clothingColorJSON = 'White' 
    
    if clothingTypeRoll == 1:
        clothing = Image.open(dirClothing + '/Longsleeve' + clothingColor).convert("RGBA")
        clothingJSON = 'Long sleeve'
    elif clothingTypeRoll == 2:
        clothing = Image.open(dirClothing + '/Shirt' + clothingColor).convert("RGBA")
        clothingJSON = 'Short sleeve'
    elif clothingTypeRoll == 3:
        clothing = Image.open(dirClothing + '/Tank' + clothingColor).convert("RGBA")
        clothingJSON = 'Tank top'
    
    #DESIGN ROLL)
    getDesign = randint(1,7)
    dirDesign = dirGender + '/Design'
    
    if getDesign <= 1:
        designRoll = randint(1,100)
        if designRoll <= 20:
            design = Image.open(dirDesign + "/Algo.png").convert("RGBA")
            designJSON = 'Algorand'
        elif 20 < designRoll <= 40:
            design = Image.open(dirDesign + "/Bitcoin.png").convert("RGBA")
            designJSON = 'Bitcoin'
        elif 40 < designRoll <= 60:
            design = Image.open(dirDesign + "/Doge.png").convert("RGBA")
            designJSON = 'Doge'
        elif 60 < designRoll <= 80:
            design = Image.open(dirDesign + "/Eth.png").convert("RGBA")
            designJSON = 'Eth'
        elif 80 < designRoll <= 100:
            design = Image.open(dirDesign + "/Sol.png").convert("RGBA")
            designJSON = 'Sol'
    elif getDesign > 1:
        design = Image.open(dirStart + '/Empty.png').convert("RGBA")
        designJSON = 'No shirt design'
            
    #ACCESSORY ROLL #
    dirAccessory = dirGender + '/Accessory'
    accessories = 0
    ACC = 0
    ACC1 = 0
    ACC2 = 0
    ACC3 = 0
    ACC4 = 0
    choice = 0
    loop = 1
    cancel = 0
    aMouthRoll = randint(1, 1000)
    earRoll = randint(1,100)
    aEyeRoll = randint(1, 1000)
    wristRoll = randint(1, 100)
    neckRoll = randint(1, 100)
    
    # # OF ACCESSORIES
    chance = randint(1, 1000)
    RNG = 104
    while chance > RNG or cancel == 1:
        RNG = RNG + 104
        accessories = accessories + 1
    
    if accessories == 1:
        ACC = 1
    if accessories == 2:
        ACC = 2
    if accessories == 3:
        ACC = 3
    if accessories == 4:
        ACC = 4
    if accessories == 5:
        ACC = 5
     
    #ACCESSORY #1
    if ACC >= 1:
        dirAccessory = dirGender + '/Accessory'
        choice = randint(1, 100)
        if choice <= 20:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 1
            dirAccessory = dirAccessory + '/Mouth'
            if aMouthRoll <= 167:
                accessory1 = Image.open(dirAccessory + '/Blunt.png').convert("RGBA")
                accessory1JSON = 'Blunt'
            if 167 < aMouthRoll <= 333:
                accessory1 = Image.open(dirAccessory + '/Cigarette.png').convert("RGBA")
                accessory1JSON = 'Cigarette'
            if 333 < aMouthRoll <= 499:
                accessory1 = Image.open(dirAccessory + '/Mask.png').convert("RGBA")
                accessory1JSON = 'Mask'    
            if 499 < aMouthRoll <= 665:
                accessory1 = Image.open(dirAccessory + '/Puke.png').convert("RGBA")
                accessory1JSON = 'Puke'
            if 665 < aMouthRoll <= 831:
                accessory1 = Image.open(dirAccessory + '/Tear.png').convert("RGBA")
                accessory1JSON = 'Tear'
            if 831 < aMouthRoll <= 1000:
                accessory1 = Image.open(dirAccessory + '/Vape.png').convert("RGBA")
                accessory1JSON = 'Vape'
                
        elif 21 < choice <= 40:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 2
            dirAccessory = dirAccessory + '/Ear'
            
            if baseType == 'skeleton':
                dirAccessory = dirAccessory + '/Skeleton'
                if earRoll <= 33:
                    accessory1 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory1JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory1 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory1JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory1 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory1JSON = 'Earring_Gold'

            else:
                if earRoll <= 33:
                    accessory1 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory1JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory1 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory1JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory1 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory1JSON = 'Earring_Gold'
                
        elif 41 < choice <= 60:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 3
            dirAccessory = dirAccessory + '/Eye'
            
            if aEyeRoll >= 166:
                accessory1 = Image.open(dirAccessory + '/3D.png').convert("RGBA")
                accessory1JSON = '3D'
            if 167 < aEyeRoll <= 333:
                accessory1 = Image.open(dirAccessory + '/Eyepatch.png').convert("RGBA")
                accessory1JSON = 'Eyepatch'
            if 334 < aEyeRoll <= 499:
                accessory1 = Image.open(dirAccessory + '/Glasses.png').convert("RGBA")
                accessory1JSON = 'Glasses'
            if 500 < aEyeRoll <= 665:
                accessory1 = Image.open(dirAccessory + '/Monocle.png').convert("RGBA")
                accessory1JSON = 'Monocle'
            if 666 < aEyeRoll <= 830:
                accessory1 = Image.open(dirAccessory + '/Sunglasses.png').convert("RGBA")
                accessory1JSON = 'Sunglasses'
            if 831 < aEyeRoll <= 1000:
                accessory1 = Image.open(dirAccessory + '/Sunglasses_Polarized.png').convert("RGBA")
                accessory1JSON = 'Sunglasses_Polarized'
                
        elif 61 < choice <= 80:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 4
            dirAccessory = dirAccessory + '/Wrist'
            
            if wristRoll < 50:
                accessory1 = Image.open(dirAccessory + '/Watch_Gold.png').convert("RGBA")
                accessory1JSON = 'Watch_Gold'
            elif wristRoll >=50:
                accessory1 = Image.open(dirAccessory + '/Watch_White.png').convert("RGBA")
                accessory1JSON = 'Watch_White'
                
        elif 81 < choice <= 100:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 5
            dirAccessory = dirAccessory + '/Neck'
            
            if neckRoll <= 50:
                accessory1 = Image.open(dirAccessory + '/Chain_Silver.png').convert("RGBA")
                accessory1JSON = 'Chain_Silver'
            elif 51 < neckRoll <= 85:
                accessory1 = Image.open(dirAccessory + '/Chain_Gold.png').convert("RGBA")
                accessory1JSON = 'Chain_Gold'
            else:
                accessory1 = Image.open(dirAccessory + '/Chain_Diamond.png').convert("RGBA")
                accessory1JSON = 'Chain_Diamond'
                
    #ACCESSORY #2
    if ACC >= 2:
        dirAccessory = dirGender + '/Accessory'
        choice = randint(1, 100)
        if choice <= 20 and ACC1 != 1:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 1
            dirAccessory = dirAccessory + '/Mouth'
            if aMouthRoll <= 166:
                accessory2 = Image.open(dirAccessory + '/Blunt.png').convert("RGBA")
                accessory2JSON = 'Blunt'
            if 167 < aMouthRoll <= 333:
                accessory2 = Image.open(dirAccessory + '/Cigarette.png').convert("RGBA")
                accessory2JSON = 'Cigarette'
            if 334 < aMouthRoll <= 499:
                accessory2 = Image.open(dirAccessory + '/Mask.png') .convert("RGBA")
                accessory2JSON = 'Mask'
            if 500 < aMouthRoll <= 665:
                accessory2 = Image.open(dirAccessory + '/Puke.png').convert("RGBA")
                accessory2JSON = 'Puke'
            if 666 < aMouthRoll <= 830:
                accessory2 = Image.open(dirAccessory + '/Tear.png') .convert("RGBA")
                accessory2JSON = 'Tear'
            if 831 < aMouthRoll <= 1000:
                accessory2 = Image.open(dirAccessory + '/Vape.png').convert("RGBA")
                accessory2JSON = 'Vape'
                
        elif 21 < choice <= 40 and ACC1 != 2:   
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 2
            dirAccessory = dirAccessory + '/Ear'
            
            if baseType == 'skeleton':
                dirAccessory = dirAccessory + '/Skeleton'
                if earRoll <= 33:
                    accessory2 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory2JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory2 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory2JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory2 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory2JSON = 'Earring_Gold'

            else:
                if earRoll <= 33:
                    accessory2 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory2JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory2 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory2JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory2 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory2JSON = 'Earring_Gold'
                    
        elif 41 < choice <= 60:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 3
            dirAccessory = dirAccessory + '/Eye'
            if aEyeRoll >= 166:
                accessory2 = Image.open(dirAccessory + '/3D.png').convert("RGBA")
                accessory2JSON = '3D'
            if 167 < aEyeRoll <= 333:
                accessory2 = Image.open(dirAccessory + '/Eyepatch.png').convert("RGBA")
                accessory2JSON = 'Eyepatch'
            if 334 < aEyeRoll <= 499:
                accessory2 = Image.open(dirAccessory + '/Glasses.png').convert("RGBA")
                accessory2JSON = 'Glasses'
            if 500 < aEyeRoll <= 665:
                accessory2 = Image.open(dirAccessory + '/Monocle.png').convert("RGBA")
                accessory2JSON = 'Monocle'
            if 666 < aEyeRoll <= 830:
                accessory2 = Image.open(dirAccessory + '/Sunglasses.png').convert("RGBA")
                accessory2JSON = 'Sunglasses'
            if 831 < aEyeRoll <= 1000:
                accessory2 = Image.open(dirAccessory + '/Sunglasses_Polarized.png').convert("RGBA")
                accessory2JSON = 'Sunglasses_Polarized'
                
        elif 61 < choice <= 80 and ACC1 != 4:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 4
            dirAccessory = dirAccessory + '/Wrist'
            if wristRoll < 50:
                accessory2 = Image.open(dirAccessory + '/Watch_Gold.png').convert("RGBA")
                accessory2JSON = 'Watch_Gold'
            else:
                accessory2 = Image.open(dirAccessory + '/Watch_White.png').convert("RGBA")
                accessory2JSON = 'Watch_White'
        elif 81 < choice <= 100 and ACC1 != 4:
            dirAccessory = dirGender + '/Accessory'
            ACC1 = 5
            dirAccessory = dirAccessory + '/Neck'
            if neckRoll < 50:
                accessory2 = Image.open(dirAccessory + '/Chain_Silver.png').convert("RGBA")
                accessory2JSON = 'Chain_Silver'
            elif 51 < neckRoll <= 85:
                accessory2 = Image.open(dirAccessory + '/Chain_Gold.png').convert("RGBA")
                accessory2JSON = 'Chain_Gold'
            else:
                accessory2 = Image.open(dirAccessory + '/Chain_Diamond.png').convert("RGBA")
                accessory2JSON = 'Chain_Diamond'
                
    #ACCESSORY #3
    if ACC >= 3:
        dirAccessory = dirGender + '/Accessory'
        choice = randint(1, 100)
        if choice <= 20 and ACC1 != 1 and ACC2 != 1:
            dirAccessory = dirGender + '/Accessory'
            ACC3 = 1
            dirAccessory = dirAccessory + '/Mouth'
            if aMouthRoll <= 166:
                accessory3 = Image.open(dirAccessory + '/Blunt.png').convert("RGBA")
                accessory3JSON = 'Blunt'
            if 167 < aMouthRoll <= 333:
                accessory3 = Image.open(dirAccessory + '/Cigarette.png').convert("RGBA")
                accessory3JSON = 'Cigarette'
            if 334 < aMouthRoll <= 499:
                accessory3 = Image.open(dirAccessory + '/Mask.png').convert("RGBA")
                accessory3JSON = 'Mask'
            if 500 < aMouthRoll <= 665:
                accessory3 = Image.open(dirAccessory + '/Puke.png').convert("RGBA")
                accessory3JSON = 'Puke'
            if 666 < aMouthRoll <= 830:
                accessory3 = Image.open(dirAccessory + '/Tear.png') .convert("RGBA")
                accessory3JSON = 'Tear'
            if 831 < aMouthRoll <= 1000:
                accessory3 = Image.open(dirAccessory + '/Vape.png').convert("RGBA")
                accessory3JSON = 'Vape'
                
        elif 21 < choice <= 40 and ACC1 != 2 and ACC2 != 2:
            dirAccessory = dirGender + '/Accessory'
            ACC3 = 2
            dirAccessory = dirAccessory + '/Ear'
            if baseType == 'skeleton':
                dirAccessory = dirAccessory + '/Skeleton'
                if earRoll <= 33:
                    accessory3 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory3JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory3 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory3JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory3 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory3JSON = 'Earring_Gold'

            else:
                if earRoll <= 33:
                    accessory3 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory3JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory3 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory3JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory3 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory3JSON = 'Earring_Gold'
                    
        elif 41 < choice <= 60:
            dirAccessory = dirGender + '/Accessory'
            ACC3 = 3
            dirAccessory = dirAccessory + '/Eye'
            if aEyeRoll >= 166 and ACC1 != 3 and ACC2 != 3:
                accessory3 = Image.open(dirAccessory + '/3D.png').convert("RGBA")
                accessory3JSON = '3D'
            if 167 < aEyeRoll <= 333:
                accessory3 = Image.open(dirAccessory + '/Eyepatch.png').convert("RGBA")
                accessory3JSON = 'Eyepatch'
            if 334 < aEyeRoll <= 499:
                accessory3 = Image.open(dirAccessory + '/Glasses.png').convert("RGBA")
                accessory3JSON = 'Glasses'
            if 500 < aEyeRoll <= 665:
                accessory3 = Image.open(dirAccessory + '/Monocle.png').convert("RGBA")
                accessory3JSON = 'Monocle'
            if 666 < aEyeRoll <= 830:
                accessory3 = Image.open(dirAccessory + '/Sunglasses.png').convert("RGBA")
                accessory3JSON = 'Sunglasses'
            if 831 < aEyeRoll <= 1000:
                accessory3 = Image.open(dirAccessory + '/Sunglasses_Polarized.png').convert("RGBA")
                accessory3JSON = 'Sunglasses_Polarized'
                
        elif 61 < choice <= 80 and ACC1 != 4 and ACC2 != 4:
            dirAccessory = dirGender + '/Accessory'
            ACC3 = 4
            dirAccessory = dirAccessory + '/Wrist'
            if wristRoll < 50:
                accessory3 = Image.open(dirAccessory + '/Watch_Gold.png').convert("RGBA")
                accessory3JSON = 'Watch_Gold'
            else:
                accessory3 = Image.open(dirAccessory + '/Watch_White.png').convert("RGBA")
                accessory3JSON = 'Watch_White'
                
        elif 81 < choice <= 100 and ACC1 != 5 and ACC2 != 5:
            dirAccessory = dirGender + '/Accessory'
            ACC3 = 5
            dirAccessory = dirAccessory + '/Neck'
            if neckRoll < 50:
                accessory3 = Image.open(dirAccessory + '/Chain_Silver.png').convert("RGBA")
                accessory3JSON = 'Chain_Silver'
            elif 51 < neckRoll <= 85:
                accessory3 = Image.open(dirAccessory + '/Chain_Gold.png').convert("RGBA")
                accessory3JSON = 'Chain_Gold'
            else:
                accessory3 = Image.open(dirAccessory + '/Chain_Diamond.png').convert("RGBA")
                accessory3JSON = 'Chain_Diamond'
                
    #ACCESSORY #4
    if ACC >= 4:
        dirAccessory = dirGender + '/Accessory'
        choice = randint(1, 100)
        if choice <= 20 and ACC1 != 1 and ACC2 != 1 and ACC3 != 1:
            dirAccessory = dirGender + '/Accessory'
            ACC4 = 1
            dirAccessory = dirAccessory + '/Mouth'
            if aMouthRoll <= 166:
                accessory4 = Image.open(dirAccessory + '/Blunt.png').convert("RGBA")
                accessory4JSON = 'Blunt'
            if 167 < aMouthRoll <= 333:
                accessory4 = Image.open(dirAccessory + '/Cigarette.png').convert("RGBA")
                accessory4JSON = 'Cigarette'
            if 334 < aMouthRoll <= 499:
                accessory4 = Image.open(dirAccessory + '/Mask.png').convert("RGBA")
                accessory4JSON = 'Mask'
            if 500 < aMouthRoll <= 665:
                accessory4 = Image.open(dirAccessory + '/Puke.png').convert("RGBA")
                accessory4JSON = 'Puke'
            if 666 < aMouthRoll <= 830:
                accessory4 = Image.open(dirAccessory + '/Tear.png') .convert("RGBA")
                accessory4JSON = 'Tear'
            if 831 < aMouthRoll <= 1000:
                accessory4 =  Image.open(dirAccessory + '/Vape.png').convert("RGBA")
                accessory4JSON = 'Vape'
                
                
        elif 21 < choice <= 40 and ACC1 != 2 and ACC2 != 2 and ACC3 != 2:
            dirAccessory = dirGender + '/Accessory'
            ACC4 = 2
            dirAccessory = dirAccessory + '/Ear'
            if baseType == 'skeleton':
                dirAccessory = dirAccessory + '/Skeleton'
                if earRoll <= 33:
                    accessory4 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory4JSON = 'Airpods'
                    
                if 34 < earRoll <= 66:
                    accessory4 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory4JSON = 'Earring_Diamond'
                    
                if 67 < earRoll <= 100:
                    accessory4 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory4JSON = 'Earring_Gold'
                    

            else:
                if earRoll <= 33:
                    accessory4 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory4JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory4 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory4JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory4 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory4JSON = 'Earring_Gold'
                    
        elif 41 < choice <= 60 and ACC1 != 3 and ACC2 != 3 and ACC3 != 3:
            dirAccessory = dirGender + '/Accessory'
            ACC4 = 3
            dirAccessory = dirAccessory + '/Eye'
            if aEyeRoll >= 166:
                accessory4 = Image.open(dirAccessory + '/3D.png').convert("RGBA")
                accessory4JSON = '3D'
            if 167 < aEyeRoll <= 333:
                accessory4 =  Image.open(dirAccessory + '/Eyepatch.png').convert("RGBA")
                accessory4JSON = 'Eyepatch'
            if 334 < aEyeRoll <= 499:
                accessory4 =  Image.open(dirAccessory + '/Glasses.png').convert("RGBA")
                accessory4JSON = 'Glasses'
            if 500 < aEyeRoll <= 665:
                accessory4 =  Image.open(dirAccessory + '/Monocle.png').convert("RGBA")
                accessory4JSON = 'Monocle'
            if 666 < aEyeRoll <= 830:
                accessory4 =  Image.open(dirAccessory + '/Sunglasses.png').convert("RGBA")
                accessory4JSON = 'Sunglasses'
            if 831 < aEyeRoll <= 1000:
                accessory4 = Image.open(dirAccessory + '/Sunglasses_Polarized.png').convert("RGBA")
                accessory4JSON = 'Sunglasses_Polarized'
                
        elif 61 < choice <= 80 and ACC1 != 4 and ACC2 != 4 and ACC3 != 4:   
            dirAccessory = dirGender + '/Accessory'
            ACC4 = 4
            dirAccessory = dirAccessory + '/Wrist'
            if wristRoll < 50:
                accessory4 = Image.open(dirAccessory + '/Watch_Gold.png').convert("RGBA")
                accessory4JSON = 'Watch_Gold'
            else:
                accessory4 = Image.open(dirAccessory + '/Watch_White.png').convert("RGBA")
                accessory4JSON = 'Watch_White'
                
        elif 81 < choice <= 100 and ACC1 != 5 and ACC2 != 5 and ACC3 != 5:
            dirAccessory = dirGender + '/Accessory'
            ACC4 = 5
            dirAccessory = dirAccessory + '/Neck'
            if neckRoll < 50:
                accessory4 =  Image.open(dirAccessory + '/Chain_Silver.png').convert("RGBA")
                accessory4JSON = 'Chain_Silver'
            elif 51 < neckRoll <= 85:
                accessory4 = Image.open(dirAccessory + '/Chain_Gold.png').convert("RGBA")
                accessory4JSON = 'Chain_Gold'
            else:
                accessory4 = Image.open(dirAccessory + '/Chain_Diamond.png').convert("RGBA")
                accessory4JSON = 'Chain_Diamond'
    #ACCESSORY #5
    if ACC >= 5:
        dirAccessory = dirGender + '/Accessory'
        choice = randint(1, 100)
        if choice <= 20 and ACC1 != 1 and ACC2 != 1 and ACC3 != 1 and ACC4 != 1:
            dirAccessory = dirGender + '/Accessory'
            dirAccessory = dirAccessory + '/Mouth'
            if aMouthRoll <= 166:
                accessory5 = Image.open(dirAccessory + '/Blunt.png').convert("RGBA")
                accessory5JSON = 'Blunt'
            if 167 < aMouthRoll <= 333:
                accessory5 = Image.open(dirAccessory + '/Cigarette.png').convert("RGBA")
                accessory5JSON = 'Cigarette'
            if 334 < aMouthRoll <= 499:
                accessory5 = Image.open(dirAccessory + '/Mask.png').convert("RGBA")
                accessory5JSON = 'Mask'
            if 500 < aMouthRoll <= 665:
                accessory5 = Image.open(dirAccessory + '/Puke.png').convert("RGBA")
                accessory5JSON = 'Puke'
            if 666 < aMouthRoll <= 830:
                accessory5 = Image.open(dirAccessory + '/Tear.png') .convert("RGBA")
                accessory5JSON = 'Tear'
            if 831 < aMouthRoll <= 1000:
                accessory5 = Image.open(dirAccessory + '/Vape.png').convert("RGBA")
                accessory5JSON = 'Vape'
                
        elif 21 < choice <= 40 and ACC1 != 2 and ACC2 != 2 and ACC3 != 2 and ACC4 != 2:
            dirAccessory = dirGender + '/Accessory'
            dirAccessory = dirAccessory + '/Ear'
            if baseType == 'skeleton':
                dirAccessory = dirAccessory + '/Skeleton'
                if earRoll <= 33:
                    accessory5 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory5JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory5 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory5JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory5 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory5JSON = 'Earring_Gold'

            else:
                if earRoll <= 33:
                    accessory5 = Image.open(dirAccessory + '/Airpods.png').convert("RGBA")
                    accessory5JSON = 'Airpods'
                if 34 < earRoll <= 66:
                    accessory5 = Image.open(dirAccessory + '/Earring_Diamond.png').convert("RGBA")
                    accessory5JSON = 'Earring_Diamond'
                if 67 < earRoll <= 100:
                    accessory5 = Image.open(dirAccessory + '/Earring_Gold.png').convert("RGBA")
                    accessory5JSON = 'Earring_Gold'
                
        elif 41 < choice <= 60 and ACC1 != 3 and ACC2 != 3 and ACC3 != 3 and ACC4 != 3:
            dirAccessory = dirGender + '/Accessory'
            dirAccessory = dirAccessory + '/Eye'
            if aEyeRoll >= 166:
                accessory5 = Image.open(dirAccessory + '/3D.png') .convert("RGBA")
                accessory5JSON = '3D'
            if 167 < aEyeRoll <= 333:
                accessory5 = Image.open(dirAccessory + '/Eyepatch.png').convert("RGBA")
                accessory5JSON = 'Eyepatch'
            if 334 < aEyeRoll <= 499:
                accessory5 = Image.open(dirAccessory + '/Glasses.png').convert("RGBA")
                accessory5JSON = 'Glasses'
            if 500 < aEyeRoll <= 665:
                accessory5 = Image.open(dirAccessory + '/Monocle.png').convert("RGBA")
                accessory5JSON = 'Monocle'
            if 666 < aEyeRoll <= 830:
                accessory5 = Image.open(dirAccessory + '/Sunglasses.png').convert("RGBA")
                accessory5JSON = 'Sunglasses'
            if 831 < aEyeRoll <= 1000:
                accessory5 = Image.open(dirAccessory + '/Sunglasses_Polarized.png').convert("RGBA")
                accessory5JSON = 'Sunglasses_Polarized'
                
        elif 61 < choice <= 80 and ACC1 != 4 and ACC2 != 4 and ACC3 != 4 and ACC4 != 4:
            dirAccessory = dirGender + '/Accessory'
            dirAccessory = dirGender + '/Accessory'
            dirAccessory = dirAccessory + '/Wrist'
            if wristRoll < 50:
                accessory5 = Image.open(dirAccessory + '/Watch_Gold.png').convert("RGBA")
                accessory5JSON = 'Watch_Gold'
            else:
                accessory5 = Image.open(dirAccessory + '/Watch_White.png').convert("RGBA")
                accessory5JSON = 'Watch_White'
        elif 81 < choice <= 100 and ACC1 != 5 and ACC2 != 5 and ACC3 != 5 and ACC4 != 5:
            dirAccessory = dirGender + '/Accessory'
            dirAccessory = dirAccessory + '/Neck'
            if neckRoll < 50:
                accessory5 = Image.open(dirAccessory + '/Chain_Silver.png').convert("RGBA")
                accessory5JSON = 'Chain_Silver'
            elif 51 < neckRoll <= 85:
                accessory5 =  Image.open(dirAccessory + '/Chain_Gold.png').convert("RGBA")
                accessory5JSON = 'Chain_Gold'
            else:
                accessory5 = Image.open(dirAccessory + '/Chain_Diamond.png').convert("RGBA")
                accessory5JSON = 'Chain_Diamond'
    
    if accessories == 0:
        accessory1 = Image.open(dirStart + '/Empty.png')
        accessory2 = Image.open(dirStart + '/Empty.png')
        accessory3 = Image.open(dirStart + '/Empty.png')
        accessory4 = Image.open(dirStart + '/Empty.png')
        accessory5 = Image.open(dirStart + '/Empty.png')
    elif accessories == 1:
        accessory2 = Image.open(dirStart + '/Empty.png')
        accessory3 = Image.open(dirStart + '/Empty.png')
        accessory4 = Image.open(dirStart + '/Empty.png')
        accessory5 = Image.open(dirStart + '/Empty.png')
    elif accessories == 2:
        accessory3 = Image.open(dirStart + '/Empty.png')
        accessory4 = Image.open(dirStart + '/Empty.png')
        accessory5 = Image.open(dirStart + '/Empty.png')
    elif accessories == 3:
        accessory4 = Image.open(dirStart + '/Empty.png')
        accessory5 = Image.open(dirStart + '/Empty.png')
    elif accessories == 4:
        accessory5 = Image.open(dirStart + '/Empty.png')
        
    
    start = Image.new("RGBA", background.size, color=(0,0,0))
    
    start.paste(background, (0,0), background)
    start.paste(base, (0,0), base)
    start.paste(clothing, (0,0), clothing)
    start.paste(design, (0,0), design)
    start.paste(eye, (0,0), eye)
    start.paste(eyebrow, (0,0), eyebrow)
    start.paste(mouth, (0,0), mouth)
    start.paste(beard, (0,0), beard)
    start.paste(accessory1, (0,0), accessory1)
    start.paste(accessory2, (0,0), accessory2)
    start.paste(accessory3, (0,0), accessory3)
    start.paste(accessory4, (0,0), accessory4)
    start.paste(accessory5, (0,0), accessory5)
    
    start.paste(hair, (0,0), hair)
    start.paste(hat, (0,0), hat)
    
    start = start.resize(dimensions, resample=0)
    imgname = str(x)
    start.save(imgname + '.png')
    
    dirJson = dirStart + '/GENERATED/'
    
    f = open(dirJson + imgname + '.json', 'x')
    if baseType == 'human':
        f.write(
            '{\n'
            '  "name": "Solana Fellas #' + str(x+1) + '",\n'
            '  "symbol": "FEL",\n'
            '  "description": "1 of 5000 Fellas on the Solana Network",\n'
            '  "seller_fee_basis_points": 750,\n'
            '  "image": "image.png",\n'
            '  "attributes": [\n'
            '    {\n'
            '      "trait_type": "Base",\n'
            '      "value": "' + baseJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Hair",\n'
            '      "value": "' + hairJSON + '"\n'
            '    },\n'
            '	{\n'
            '      "trait_type": "Hair Color",\n'
            '      "value": "' + colorJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Clothing",\n'
            '      "value": "' + clothingJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Clothing Color",\n'
            '      "value": "' + clothingColorJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Design",\n'
            '      "value": "' + designJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Eyebrow",\n'
            '      "value": "' + eyebrowJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Eyebrow Color",\n'
            '      "value": "' + eyebrowColorJSON + '"\n'
            '   },\n'
            '      {\n'
            '      "trait_type": "Eye",\n'
            '      "value": "' + eyeJSON + '"\n'
            '   },\n'
            '      {\n'
            '      "trait_type": "Eye Color",\n'
            '      "value": "' + eyeColorJSON + '"\n'
            '   },\n'
            '      {\n'
            '      "trait_type": "Mouth",\n'
            '      "value": "' + mouthJSON + '"\n'
            '   },\n'
            '    {\n'
            '      "trait_type": "Hat",\n'
            '      "value": "' + hatJSON + '"\n' 
            '    },\n'
        )
    if baseType == 'monkey' or baseType == 'robot':
        f.write(
            '{\n'
            '  "name": "Solana Fellas #' + str(x+1) + '",\n'
            '  "symbol": "FEL",\n'
            '  "description": "1 of 5000 Fellas on the Solana Network",\n'
            '  "seller_fee_basis_points": 750,\n'
            '  "image": "image.png",\n'
            '  "attributes": [\n'
            '    {\n'
            '      "trait_type": "Base",\n'
            '      "value": "' + baseJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Clothing",\n'
            '      "value": "' + clothingJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Clothing Color",\n'
            '      "value": "' + clothingColorJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Design",\n'
            '      "value": "' + designJSON + '"\n'
            '   },\n'
            '      {\n'
            '      "trait_type": "Eye",\n'
            '      "value": "' + eyeJSON + '"\n'
            '   },\n'
            '      {\n'
            '      "trait_type": "Eye Color",\n'
            '      "value": "' + eyeColorJSON + '"\n'
            '   },\n'
            '      {\n'
            '      "trait_type": "Mouth",\n'
            '      "value": "' + mouthJSON + '"\n'
            '   },\n'
            '    {\n'
            '      "trait_type": "Hat",\n'
            '      "value": "' + hatJSON + '"\n' 
            '    },\n'
        )
        
    if baseType == 'skeleton':
        f.write(
            '{\n'
            '  "name": "Solana Fellas #' + str(x+1) + '",\n'
            '  "symbol": "FEL",\n'
            '  "description": "1 of 5000 Fellas on the Solana Network",\n'
            '  "seller_fee_basis_points": 750,\n'
            '  "image": "image.png",\n'
            '  "attributes": [\n'
            '    {\n'
            '      "trait_type": "Base",\n'
            '      "value": "' + baseJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Clothing",\n'
            '      "value": "' + clothingJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Clothing Color",\n'
            '      "value": "' + clothingColorJSON + '"\n'
            '   },\n'
            '   {\n'
            '      "trait_type": "Design",\n'
            '      "value": "' + designJSON + '"\n'
            '   },\n'
            '    {\n'
            '      "trait_type": "Hat",\n'
            '      "value": "' + hatJSON + '"\n' 
            '    },\n'
        )
    if accessories > 1:
        f.write(
            '    {\n'
            '      "trait_type": "Accessory #1",\n'
            '      "value": "' + accessory1JSON + '"\n'
            '    },\n'
        )
    if accessories > 2:
        f.write(
            '    {\n'
            '      "trait_type": "Accessory #2",\n'
            '      "value": "' + accessory2JSON + '"\n'
            '    },\n'
        )
    if accessories > 3:
        f.write(
            '    {\n'
            '      "trait_type": "Accessory #3",\n'
            '      "value": "' + accessory3JSON + '"\n'
            '    },\n'
        )
    if accessories > 4:    
        f.write(
            '    {\n'
            '      "trait_type": "Accessory #4",\n'
            '      "value": "' + accessory4JSON + '"\n'
            '    },\n'
        )
    if accessories > 5:
        
        f.write(
            '    {\n'
            '      "trait_type": "Accessory #5",\n'
            '      "value": "' + accessory5JSON + '"\n'
            '    },\n'
        )
    f.write(
        '    {\n'
        '      "trait_type": "Background",\n'
        '      "value": "' + backgroundJSON  + '"\n'
        '    }\n'
        '  ],\n'
        '  "collection": {\n'
        '     "name": "Solana Fellas",\n'
        '     "family": "NFT"\n'
        '  },\n'
        '  "properties": {\n'
        '    "files": [\n'
        '      {\n'
        '        "uri": "image.png",\n'
        '        "type": "image/png"\n'
        '      }\n'
        '    ],\n'
        '    "category": "image",\n'
        '    "creators": [\n'
        '      {\n'
        '        "address": "9qsK4BpdZC3xdFuBcDHdZbkKr9DKrQifRb5YiKQh5YuQ",\n'
        '        "share": 50\n'
        '     },\n'
        '	  {\n'
        '        "address": "8cQmHHb8urJfPjuMtEvZZmRNGvRi2T4TThmtG6tCizR8",\n'
        '        "share": 50\n'
        '      }\n'
        '    ]\n'
        '  }\n'
        '}\n'
    )
   
