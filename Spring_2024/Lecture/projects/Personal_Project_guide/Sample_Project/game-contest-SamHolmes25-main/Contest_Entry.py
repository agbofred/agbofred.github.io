# Name: Red vs Green

"""

*PLEASE when you play this game press in the box that says show hitboxes, and do a few attacks.Calculating the hitboxes took
me so long, additionally please look at the different weapons hitboxes when this is enabled

*The window closing when you kill the last enemy is not a glitch, it starts a prompt in a terminal that lets you replay the level or go
to a new one

When you start the game you will be asked to choose a level(1-6) in the terminal, this selects the level you are playing. In the game itself you are a green
cube that you can control using the arrow keys. Your goal is to get rid of all the red bouncing cubes on the screen without your health reaching zero.
Both your green cube and all the red cubes each have 10 HP, and if the cube has 0 HP then it is removed from the graphics window and nothing else can 
interact with it. When cubes hit each other they both lose 1 HP and bounce off each other. If you click in the window you release an attack in the direction of
the click, if a cube hits your attack that cube takes 1 damage and you take none. You can swap between weapons by clicking on the top row of boxes, this
changes both the shape and appearance of your attack. Clicking on the show hitboxes box reveals the hitboxes of the weapon(what the cubes will actually bounce off of
rather than graphic of the attack). The second box on the bottom row shows your current HP and the third box is the name of the level.

Because of the way that the hitboxes of attacks are calculated it often is better to inpale the red boxes with your attack, rather than letting them
move into it. If you inpale them properly it instantly kills them, if they move into your attack they bounce off it only taking one damage.

Because of the differing shapes of the attacks and how entity collisions are calculated, hitboxes are a series of rectangles that are calculated based
off the variables of ATTACK_HEIGHT, ATTACK_PROP, ATTACK_WIDTH, HIT_QUALITY and the angle of the attack itself. The formula I devised to calculate these
rectangles is inspired by Riemann Sums, and uses a lot of trigonometry to find the height of these rectangles. It is accurate and works with a variety of 
attacks but in order to further increase the accuracy I manuelly adjusted a few variables within the 3 set attacks. If I had more time I would have the
formula switch from calculating the height with a set width to calculating the width with a set height. This would make the hitboxes more accurate between the
angles of 45-135 degrees and 225-295 degrees

When you either kill all of the red cubes or your HP reaches 0, the window closes and the terminal will ask you what level you want to go to next.
This allows you to continue playing the game without having to restart the code, if you respond exit the game ends.

This game is data driven so the text file Levels.txt determines the level designs, enitities and players are seperated by an empty line, levels are 
seperated with **** and the end of the file is signified with ----
"""

#This function takes the data from the text file and makes it into a list with three levels. The list is made of lists that 
#represent a single level, that list is conposted of lists that represent each entity or the player
def get_level_data(prefix):
    filename=prefix
    with open(filename) as f:
        CurrentLine="Start"
        Big_List=[]
        while CurrentLine!="----":
            LevelList=[]
            while CurrentLine!="****":
                if CurrentLine!="Player" and CurrentLine!="Entity":
                    CurrentLine=f.readline().rstrip()
                if CurrentLine=="Player":
                    TempList=[]
                    while CurrentLine!="":
                        TempList.append(CurrentLine)
                        CurrentLine=f.readline().rstrip()
                    LevelList.append(TempList)
                if CurrentLine=="Entity":
                    TempList=[]
                    while CurrentLine!="":
                        TempList.append(CurrentLine)
                        CurrentLine=f.readline().rstrip()
                    LevelList.append(TempList)
            CurrentLine=f.readline().rstrip()
            Big_List.append(LevelList)
    return Big_List


from math import atan, pi,sqrt,cos,sin,tan,asin
#This class is used for red cubes and I have future plans to use this to create stationary pillars and obstables to make the map
#more interesting, that is why this is a different class than the one used for player 
class entity:
    """Everything within this class is pretty much just its name and there is a bunch of getters and setters"""
    def __init__(self,x_position,y_position,x_speed,y_speed,entity_width,entity_height,color,player):
        self.x_speed=x_speed
        self.y_speed=y_speed
        self.HP=10
        self.x_position=x_position
        self.y_position=y_position
        self.entity_width=entity_width
        self.entity_height=entity_height
        self.color=color
        self.player=player
    def get_color(self):
        return self.color
    def get_x_speed(self):
        return self.x_speed
    def get_y_speed(self):
        return self.y_speed
    def get_speed(self):
        return self.speed
        return self.max_HP
    def get_HP(self):
        return self.HP
    def damage_health(self,x):
        self.HP=self.HP-x
    def get_x_position(self):
        return self.x_position
    def get_y_position(self):
        return self.y_position
    def get_width(self):
        return self.entity_width
    def get_height(self):
        return self.entity_width
    #This is used to determine if the entity is a player or not 
    def get_player(self):
        return self.player
    def set_x_position(self,x_postion):
        self.x_position=x_postion
    def set_y_position(self,y_postion):
        self.y_position=y_postion
    def set_x_speed(self,x_speed):
        self.x_speed=x_speed
    def set_y_speed(self,y_speed):
        self.y_speed=y_speed
    #This is needed to prevent the players attack from hitting themselves with their attacks
    def is_attack(self):
        return False

#This class is used for the player,it needed to have a few more attributes than a normal entity so I made it into a new class
class player:
    def __init__(self,x_position,y_position,width,height,player):
        self.x_position=x_position
        self.y_position=y_position
        self.width=width
        self.height=height
        self.x_speed=0
        self.y_speed=0
        self.player=player
        self.attacking=False
        self.attack_timer=0
        self.attack=False
        self.color="#AAFF00"
        self.player_health=10

    def get_color(self):
        return self.color
    #Attack timer is used make the attack dissapear after a set amount of time, the following two functions are used to manage this 
    def get_attack_timer(self):
        return self.attack_timer
    def set_attack_timer(self,input):
        self.attack_timer=input
    def update_attack_timer(self,update):
        self.attack_timer=self.attack_timer+update
    def get_x_position(self):
        return self.x_position
    def set_x_position(self,x_position):
        self.x_position=x_position
    def get_y_position(self):
        return self.y_position
    def set_x_position(self,y_position):
        self.x_position=y_position
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width
    def get_x_speed(self):
        return self.x_speed
    def get_y_speed(self):
        return self.y_speed
    def set_y_speed(self,y_speed):
        self.y_speed=0
    def set_x_speed(self,x_speed):
        self.x_speed=0
    #This is used to determine in 
    def get_player(self):
        return self.player
    def move(self,x_move,y_move):
        self.x_position=self.x_position+x_move
        self.y_position=self.y_position+y_move
    def get_attack(self):
        return self.attacking 
    def set_attack(self,attacking):
        self.attacking=attacking
    #This is used to determine if the entity is an attack
    def is_attack(self):
        return False
    def get_HP(self):
        return self.player_health
    def damage_health(self,x):
        self.player_health=self.player_health-x

#This is used for the temporary entities that are created when the player attacks, This is a new class
#because it only needs to contain a small amount of data and they need to be easily found to remove them
class attack:
    def __init__(self,x_position,y_position,width,height):
        self.x_position=x_position
        self.y_position=y_position
        self.width=width
        self.height=height
        self.attack=True
        self.y_speed=0
        self.x_speed=0
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width
    def get_x_position(self):
        return self.x_position
    def get_y_position(self):
        return self.y_position
    def set_y_speed(self):
        pass
    def set_x_speed(self):
        pass
    def get_player(self):
        return False
    def is_attack(self):
        return self.attack
    def get_y_speed(self):
        return self.y_speed
    def get_x_speed(self):
        return self.x_speed
    def set_y_speed(self,x):
        if x is None:
            pass
    def set_x_speed(self,y):
        if y is None:
            pass
color_gradient=["#ff0f0f","#eb0000","#d70000","#c30000","#af0000","#9c0000","#8a0000","#780000","#680000","#000000"]

"""These are the constants"""
WINDOW_HEIGHT=600
#This is the area that the cube can bounce in
BATTLE_AREA_HEIGHT=WINDOW_HEIGHT-100
WINDOW_WIDTH=600
#These variables need to be global because they get changed when the player switches weapon
global ATTACK_HEIGHT,ATTACK_PROP,ATTACK_WIDTH,ATTACK_ANGLE,ATTACK_SIDE_LENGTH,HIT_QUALITY,GAME_OVER
GAME_OVER=False
ATTACK_HEIGHT=100
ATTACK_PROP=0.5
ATTACK_WIDTH=50
ATTACK_ANGLE=atan((ATTACK_WIDTH/2)/(ATTACK_HEIGHT*ATTACK_PROP))*(180/pi)
ATTACK_SIDE_LENGTH=sqrt((ATTACK_WIDTH/2)**2+(ATTACK_HEIGHT*ATTACK_PROP)**2)
#This is how many hitboxes are generated when the player attacks, this doesn't make the attack bigger but instead more acurately 
#tracks where the weapon is hitting, because each box is smaller. Increasing this increases the lag
HIT_QUALITY=10
SHOW_HITBOX=False
#This determines the starting weapon
weapon="Sword"

"""-----------------------------------------------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------------------------------------------"""

"""This is where the actual game runs, up above is all the framework and Boring stored information"""

from pgl import GWindow,GRect,GLine,GPolygon,GLabel
#This list will contain all the entities within the game including attacks,player and entities
entityList=[]
#This dictonary will be used to connect the instances of the classes player and entities 
ConnectionDict={}

"""This function take the list made from the text document uses the data from the level inputted and adds the player 
and entities to the entity list"""
def create_entities(level):
    global entityList
    entityList=[]
    LevelList=get_level_data("Levels.txt")
    for entity_data in LevelList[level]:
        if entity_data[0]=="Player":
            global user
            user=player(int(entity_data[1]),int(entity_data[2]),int(entity_data[3]),int(entity_data[4]),True)
            entityList.append(user)
        else:
            entityList.append(entity(int(entity_data[1]),int(entity_data[2]),int(entity_data[3]),int(entity_data[4]),int(entity_data[5]),int(entity_data[6]),"#ff0f0f",False))

#This whole function is used to check if entities have hit each other and change their attributes accordingly
def collision_checker():
    #This function updates the health graphic with the HP of the inputted
    def update_health_graphic(entity):
        gw.remove(gw.Current_health)
        gw.Current_health=GLabel("Current health: "+str(entity.get_HP()),WINDOW_WIDTH/3+20,29*(WINDOW_HEIGHT/30))
        gw.add(gw.Current_health)
    for entity in entityList:
        for entity2 in entityList:
            if entity is not entity2:
                #The following two if statements check and see if the entities have collided
                if (entity.get_y_position()>=entity2.get_y_position() and entity.get_y_position()<=entity2.get_y_position()+entity2.get_height()) or (entity2.get_y_position()>=entity.get_y_position() and entity2.get_y_position()<=entity.get_y_position()+entity.get_height()):
                    if (entity.get_x_position()>=entity2.get_x_position() and entity.get_x_position()<=entity2.get_x_position()+entity2.get_width()): 
                        #This next line prevents the player from getting hit by their own attack
                        if (entity.is_attack() or entity2.is_attack()) and (entity.get_player() or entity2.get_player()):
                            continue
                        #These next two if statements lower the entities HP
                        if entity.is_attack()==False:
                            entity.damage_health(1)
                        if entity2.is_attack()==False:
                            entity2.damage_health(1)   
                        #these next two if statements update the player health graphic if the player takes damage
                        if entity.get_player():
                            update_health_graphic(entity)                   
                        if entity2.get_player():
                            update_health_graphic(entity2)
                        #This causes the red cubes to bounce off of things, because the players speed is zero the player does not move
                        entity.set_y_speed(-(entity.get_y_speed()))
                        entity.set_x_speed(-(entity.get_x_speed()))
                        entity2.set_y_speed(-(entity2.get_y_speed()))
                        entity2.set_x_speed(-(entity2.get_x_speed()))
                        #The rest of this code is used to bump the player away from the cube that hit them
                        #This is important because before this was implemented the player would get stuck within the other entity
                        if entity2.get_player():
                            if entity2.get_x_position()>=entity.get_x_position():
                                #Bottom right
                                if entity2.get_y_position()>=entity.get_y_position():
                                    if entity2.get_x_position()+10<=WINDOW_WIDTH:
                                        entity2.move(10,10)
                                        ConnectionDict[entity].move(10,10)
                                else:
                                    #Top righ
                                    entity2.move(10,-10)
                                    ConnectionDict[entity2].move(10,-10)
                            else:
                                if entity2.get_y_position()>=entity.get_y_position():
                                    #Bottom Left
                                    entity2.move(-10,10)
                                    ConnectionDict[entity2].move(-10,10)
                                else:
                                    #Top left
                                    entity2.move(-10,-10)
                                    ConnectionDict[entity2].move(-10,-10)
                        if entity.get_player():
                            if entity.get_x_position()>entity2.get_x_position():
                                if entity.get_y_position()>entity2.get_y_position():
                                    #Top left 
                                    entity.move(10,10)
                                    ConnectionDict[entity].move(10,10)
                                else:
                                    #Top right 
                                    entity.move(10,-10)
                                    ConnectionDict[entity].move(10,-10)
                            else:
                                if entity.get_y_position()>entity2.get_y_position():
                                    #Top Left
                                    entity.move(-10,10)
                                    ConnectionDict[entity].move(-10,10)
                                else:
                                    #Bottom Left
                                    entity.move(-10,-10)
                                    ConnectionDict[entity].move(-10,-10)

                        
#This moves the graphics and updates the graphics respective instance of a class
def entity_mover():
    global entityList
    for entity in entityList:
        #This code removes the graphic of the attack and hitboxes 
        if entity.get_player():
            if entity.get_attack():
                entity.update_attack_timer(1)
                if entity.get_attack_timer()>150:
                    entity.set_attack(False)
                    entity.set_attack_timer(0)
                    gw.remove(ConnectionDict["Attack1"])
                    gw.remove(ConnectionDict["Attack2"])
                    for item in gw.Hitbox_list:
                        gw.remove(item)
                    Removal=[]
                    for enitiy in entityList:
                        if enitiy.is_attack()==True:
                            Removal.append(enitiy)
                    for item in Removal:
                        entityList.remove(item)
        #This moves all of the non-attack and non-player entities
        if entity.is_attack()==False and entity.get_player()==False:
            ConnectionDict[entity].move(entity.get_x_speed(),entity.get_y_speed())
            entity.set_x_position(entity.get_x_position()+entity.get_x_speed())
            entity.set_y_position(entity.get_y_position()+entity.get_y_speed())
            #This causes the boxes to bounce on the walls
            if entity.get_x_position()>=WINDOW_WIDTH-entity.get_width() or entity.get_x_position()<=0:
                entity.set_x_speed(-(entity.get_x_speed()))
            if entity.get_y_position()>=BATTLE_AREA_HEIGHT-entity.get_height() or entity.get_y_position()<=0:
                entity.set_y_speed(-(entity.get_y_speed()))
        #This checks to see if a entity has HP<0, if it does it removes it from the game
        #This close the window if there is no red cubes left or the player has 0 HP
        # It also wipes a lot of the data so that the player can play again by responding to the prompt in the terminal
        if entity.is_attack()==False:
            if entity.get_HP()<=0:
                entityList.remove(entity)
                gw.remove(ConnectionDict[entity])
                if entity.get_player()==True:
                    global GAME_OVER
                    GAME_OVER=True
                    secondList=[]
                    for entity in entityList:
                        secondList.append(entity)
                    for entity in secondList:
                        if entity.is_attack()==False:
                            gw.remove(ConnectionDict[entity])
                            entityList.remove(entity)
                    check=ConnectionDict.get("Attack1","No")
                    if check!="No":
                        gw.remove(ConnectionDict["Attack1"])
                    check=ConnectionDict.get("Attack2","No")
                    if check!="No":
                        gw.remove(ConnectionDict["Attack2"])
                    ConnectionDict.clear()
                    entityList=[]
                    gw.close()
                else:
                    Things_left_to_kill=False
                    for object in entityList:
                        if object.get_player()==False and object.is_attack()==False:
                            Things_left_to_kill=True
                    if not Things_left_to_kill:
                        secondList=[]
                        for entity in entityList:
                            secondList.append(entity)
                        for entity in secondList:
                            if entity.is_attack()==False:
                                gw.remove(ConnectionDict[entity])
                                entityList.remove(entity)
                        check=ConnectionDict.get("Attack1","No")
                        if check!="No":
                            gw.remove(ConnectionDict["Attack1"])
                        check=ConnectionDict.get("Attack2","No")
                        if check!="No":
                            gw.remove(ConnectionDict["Attack2"])
                        ConnectionDict.clear()
                        entityList=[]
                        gw.close()               
    collision_checker()

def create_window(level):
    global gw,entityList,ConnectionDict
    #The following lines just add stuff to the graphics window
    gw=GWindow(WINDOW_WIDTH,WINDOW_HEIGHT)
    Background=GRect(0,0,WINDOW_WIDTH,BATTLE_AREA_HEIGHT)
    Background.set_filled(True)
    Shaft=GRect(0,WINDOW_HEIGHT-4*(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/5,100,10)
    Shaft.set_color("#964B00")
    Shaft.set_filled(True)
    gw.add(Shaft)
    Spear_head=GPolygon()
    Spear_head.add_vertex(WINDOW_WIDTH/6,BATTLE_AREA_HEIGHT+20)
    Spear_head.add_vertex(WINDOW_WIDTH/6,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2-20)
    Spear_head.add_vertex(WINDOW_WIDTH/3,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/4)
    Spear_head.set_filled(True)
    Spear_head.set_color("#C0C0C0")
    Sword=GPolygon()
    Sword.add_vertex(WINDOW_WIDTH/2,BATTLE_AREA_HEIGHT+10+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/8)
    Sword.add_vertex(WINDOW_WIDTH/2,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2-10)
    Sword.add_vertex(2*WINDOW_WIDTH/3,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/4)
    Sword.set_filled(True)
    Sword.set_color("#C0C0C0")
    Sword2=GPolygon()
    Sword2.add_vertex(WINDOW_WIDTH/2,BATTLE_AREA_HEIGHT+10+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/8)
    Sword2.add_vertex(WINDOW_WIDTH/2,BATTLE_AREA_HEIGHT+10)
    Sword2.add_vertex(2*WINDOW_WIDTH/3,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/4)
    Sword2.set_filled(True)
    Sword2.set_color("#ffbf00")
    Handle1=GRect(WINDOW_WIDTH/2-WINDOW_WIDTH/30,BATTLE_AREA_HEIGHT+5,WINDOW_WIDTH/30,40)
    Handle2=GRect(WINDOW_WIDTH/2-WINDOW_WIDTH/10,BATTLE_AREA_HEIGHT+15,WINDOW_WIDTH/15,20)
    Handle1.set_filled(True)
    Handle1.set_color("#964B00")
    Handle2.set_filled(True)
    Club=GPolygon()
    Club.add_vertex(WINDOW_WIDTH-10,BATTLE_AREA_HEIGHT+10)
    Club.add_vertex(2*WINDOW_WIDTH/3,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/4)
    Club.add_vertex(WINDOW_WIDTH-10,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2-10)
    Club.set_filled(True)
    Club.set_color("#964B00")
    gw.add(Background)
    gw.add(Spear_head)
    gw.add(Sword)
    gw.add(Sword2)
    gw.add(Handle1)
    gw.add(Handle2)
    gw.add(Club)
    gw.add(GLabel("Show Hitboxes",10,29*(WINDOW_HEIGHT/30)))
    gw.Current_health=GLabel("Current health: 10",WINDOW_WIDTH/3+20,29*(WINDOW_HEIGHT/30))
    gw.add(gw.Current_health)
    #This dictonary contains the name of the levels, This part is not data driven, I have future plans to fix this
    levelnameDict={1:"Tutorial",2:"David vs Goliath",3:"Tall vs Small",4:"Stairs",5:"Good Luck",6:"Just wait"}
    gw.add(GLabel(levelnameDict[level],2*WINDOW_WIDTH/3+20,29*(WINDOW_WIDTH/30)))
    for i in range(2):
        gw.add(GLine((WINDOW_WIDTH/3)*(i+1),BATTLE_AREA_HEIGHT,(WINDOW_WIDTH/3)*(i+1),WINDOW_HEIGHT))
    gw.add(GLine(0,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2,WINDOW_WIDTH,BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2))
    #This list stores the boxes that represent the hitboxes when show hitboxes is turned on
    gw.Hitbox_list=[]
    #This takes the entities from entity list and adds the proper graphics connecting them using ConnectionDict
    for entity in entityList:
        if entity.get_player():
            user=entity
            gw.player=GRect(entity.get_x_position(),entity.get_y_position(),entity.get_width(),entity.get_height())
            gw.player.set_color(user.get_color())
            gw.add(gw.player)
            ConnectionDict[user]=gw.player
        else:
            tempRec=GRect(entity.get_x_position(),entity.get_y_position(),entity.get_height(),entity.get_width())
            tempRec.set_color(color_gradient[9])
            tempRec.set_color(entity.get_color())
            tempRec.set_filled(False)
            ConnectionDict[entity]=tempRec
            gw.add(ConnectionDict[entity])
        gw.first=False
        gw.second=False
    
    def click_event(event):
        if GAME_OVER!=True:
            global ATTACK_HEIGHT,ATTACK_PROP,ATTACK_WIDTH,ATTACK_ANGLE,ATTACK_SIDE_LENGTH,HIT_QUALITY,weapon,SHOW_HITBOX
            """This takes two points and returns the angle they are from each other, calculates the length of the x leg and y leg of a 
             right triangle with an angle of elevation equal to the previously calculated angle and Hypotenuse with a length of 
             ATTACK_HEIGHT.It also says what quadrant the second point is in relitive to the first point. This is nessacary 
             to calculate the hitboxes and graphic of the attack"""
            def analyse(x,y,x2,y2):
                global ATTACK_HEIGHT
                if x>x2:
                    X_positive=True
                else:
                    X_positive=False
                if y>y2:
                    Y_positive=True
                else:
                    Y_positive=False
                if x==x2:
                    if y==y2:
                        return "Null"
                    else:
                        if y>y2:
                            return 270,0,y-y2
                        else:
                            return 90,0,y2-y
                elif y==y2:
                    if x>x2:
                        return 0,x-x2,0
                    else:
                        return 0,x2-x,0
                if not X_positive and Y_positive:
                    angle=-(atan((y-y2)/(x-x2))*(180/pi))
                    return angle,cos(angle*(pi/180))*ATTACK_HEIGHT,sin(angle*(pi/180))*ATTACK_HEIGHT,1
                if X_positive and Y_positive:
                    angle=180+atan((y-y2)/(x2-x))*(180/pi)
                    return angle,cos(angle*(pi/180))*ATTACK_HEIGHT,sin(angle*(pi/180))*ATTACK_HEIGHT,2
                if X_positive and not Y_positive:
                    angle=180-(atan((y2-y)/(x2-x))*(180/pi))
                    return angle,cos(angle*(pi/180))*ATTACK_HEIGHT,sin(angle*(pi/180))*ATTACK_HEIGHT,3
                if not X_positive and not Y_positive:
                    angle=360-(atan((y2-y)/(x2-x)))*(180/pi)
                    return angle,cos(angle*(pi/180))*ATTACK_HEIGHT,sin(angle*(pi/180))*ATTACK_HEIGHT,2
            #This next if statement checks if the click is in the area where the cubes can bounce, to see if attacking would
            # be acceptable
            if gw.first and gw.y<BATTLE_AREA_HEIGHT:
                #This removes the Rectangles representing the hitboxes so they can be replaced new hitboxes that
                # better represent the attack
                if gw.Hitbox_list!=[]:
                    for item in gw.Hitbox_list:
                        gw.remove(item)
                #This starts the timer towards erasing the attack
                user.set_attack(True)
                #This next line checks if there is an attack present it removes it so it can be replaced with a new attack
                if gw.second:
                    gw.remove(gw.tempPolygon)
                    gw.remove(gw.tempPolygon2)
                #These next three if statments create the graphics of the attack changing it if the player chooses a new weapon
                if weapon=="Sword":
                    angle=analyse(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2),gw.x,gw.y)
                    gw.tempPolygon=GPolygon()
                    gw.tempPolygon.add_vertex(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2))
                    gw.tempPolygon.add_polar_edge(ATTACK_HEIGHT-20,angle[0])
                    gw.tempPolygon.add_polar_edge(ATTACK_SIDE_LENGTH,angle[0]+(180-ATTACK_ANGLE))
                    gw.tempPolygon.set_filled(True)
                    gw.tempPolygon.set_color("#C0C0C0")
                    gw.add(gw.tempPolygon)
                    ConnectionDict["Attack1"]=gw.tempPolygon
                    gw.tempPolygon2=GPolygon()
                    gw.tempPolygon2.add_vertex(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2))
                    gw.tempPolygon2.add_polar_edge(ATTACK_HEIGHT-20,angle[0])
                    gw.tempPolygon2.add_polar_edge(ATTACK_SIDE_LENGTH,angle[0]+(180+ATTACK_ANGLE))
                    gw.tempPolygon2.set_filled(True)
                    gw.tempPolygon2.set_color("#ffbf00")
                    gw.add(gw.tempPolygon2)
                    ConnectionDict["Attack2"]=gw.tempPolygon2
                    gw.second=True
                if weapon=="Spear":
                    angle=analyse(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2),gw.x,gw.y)
                    gw.tempPolygon=GPolygon()
                    gw.tempPolygon.add_vertex(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2))
                    gw.tempPolygon.add_polar_edge(ATTACK_HEIGHT-10,angle[0])
                    gw.tempPolygon.add_polar_edge(ATTACK_SIDE_LENGTH-25,angle[0]+(180-ATTACK_ANGLE)+40)
                    gw.tempPolygon.set_filled(True)
                    gw.tempPolygon.set_color("#C0C0C0")
                    gw.add(gw.tempPolygon)
                    ConnectionDict["Attack1"]=gw.tempPolygon
                    gw.tempPolygon2=GPolygon()
                    gw.tempPolygon2.add_vertex(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2))
                    gw.tempPolygon2.add_polar_edge(ATTACK_HEIGHT-10,angle[0])
                    gw.tempPolygon2.add_polar_edge(ATTACK_SIDE_LENGTH-25,angle[0]+(180+ATTACK_ANGLE)-40)
                    gw.tempPolygon2.set_filled(True)
                    gw.tempPolygon2.set_color("#C0C0C0")
                    gw.add(gw.tempPolygon2)
                    ConnectionDict["Attack2"]=gw.tempPolygon2
                    gw.second=True
                if weapon=="Club":
                    angle=analyse(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2),gw.x,gw.y)
                    gw.tempPolygon=GPolygon()
                    gw.tempPolygon.add_vertex(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2))
                    gw.tempPolygon.add_polar_edge(ATTACK_HEIGHT,angle[0])
                    gw.tempPolygon.add_polar_edge(ATTACK_SIDE_LENGTH+20,angle[0]+(180-ATTACK_ANGLE)-30)
                    gw.tempPolygon.set_filled(True)
                    gw.tempPolygon.set_color("#964B00")
                    gw.add(gw.tempPolygon)
                    ConnectionDict["Attack1"]=gw.tempPolygon
                    gw.tempPolygon2=GPolygon()
                    gw.tempPolygon2.add_vertex(user.get_x_position()+(user.get_width()/2),user.get_y_position()+(user.get_height()/2))
                    gw.tempPolygon2.add_polar_edge(ATTACK_HEIGHT,angle[0])
                    gw.tempPolygon2.add_polar_edge(ATTACK_SIDE_LENGTH+20,angle[0]+(180+ATTACK_ANGLE)+30)
                    gw.tempPolygon2.set_filled(True)
                    gw.tempPolygon2.set_color("#964B00")
                    gw.add(gw.tempPolygon2)
                    ConnectionDict["Attack2"]=gw.tempPolygon2
                    gw.second=True
                
                #These next lines calculate the hitboxes with a bunch of annoying cruchy math, the width is always a set proportion of the x leg
                #but the height of the hitboxes is calculated.
                # The formula is the x cordinate is user.get_x_position()+user.get_width()/2+(((length_of_x_leg)/HIT_QUALITY)*i)
                #The formula for the width is very simmalar and simple (length_of_x_leg)/HIT_QUALITY
                #The formula for the height tan(ATTACK_ANGLE*(180*pi))*((length_of_x_leg/HIT_QUALITY)*i) 
                #The formula for y cordinate is user.get_y_position()+user.get_height()/2-((angle[2]/HIT_QUALITY)*i)-(tan(ATTACK_ANGLE*(180*pi))*((angle[1]/HIT_QUALITY)*i)/2)
                #This formula is basically just how far above or below the direct line to the point you clicked the hitbox is 
                # ATTACK_ANGLE is calculated earlier using the ATTACK_WIDTH(the width of the sword at the widest point),ATTACK_HEIGHT(How far the sword goes)
                # and ATTACK_PROP(where along the sword is the widest)
                for i in range(HIT_QUALITY):
                    if i<HIT_QUALITY*(1-ATTACK_PROP):
                        if SHOW_HITBOX==True:
                            tempRec=GRect(user.get_x_position()+user.get_width()/2+((angle[1]/HIT_QUALITY)*i),user.get_y_position()+user.get_height()/2-((angle[2]/HIT_QUALITY)*i)-(tan(ATTACK_ANGLE*(180*pi))*((angle[1]/HIT_QUALITY)*i)/2),angle[1]/HIT_QUALITY,tan(ATTACK_ANGLE*(180*pi))*((angle[1]/HIT_QUALITY)*i))
                            gw.Hitbox_list.append(tempRec)
                            tempRec.set_color("#FFFFFF")
                            gw.add(tempRec)
                        max_height=abs(-(tan(ATTACK_ANGLE*(180*pi))*((angle[1]/HIT_QUALITY)*i)))
                        max_x=user.get_x_position()+user.get_width()/2+((angle[1]/HIT_QUALITY)*i)
                        x_position=user.get_x_position()+user.get_width()/2+((angle[1]/HIT_QUALITY)*i)
                        y_position=(user.get_y_position()+user.get_height()/2-((angle[2]/HIT_QUALITY)*i)-(tan(ATTACK_ANGLE*(180*pi))*((angle[1]/HIT_QUALITY)*i)/2))+(tan(ATTACK_ANGLE*(180*pi))*((angle[1]/HIT_QUALITY)*i))
                        height=-(tan(ATTACK_ANGLE*(180*pi))*((angle[1]/HIT_QUALITY)*i))
                        width=angle[1]/HIT_QUALITY
                        entityList.append(attack(x_position,y_position,width,height))
                    #This part of the code is for calculating the hitbox of the sword when it starts to shrink after reaching its widest point
                    #I kinda cheated a little and took the data from the pervious calculations to find the highest point in the whole attack
                    # Used the distance traveled from that highest point and found the angle in which the attack is now decreasing.
                    #Using both of those found the amount lower that the highest point that the rectange is 
                    # and finally using everything that I found calculated the height of that rectangle 
                    else:
                        Displacement=-(max_x-(user.get_x_position()+user.get_width()/2+((angle[1]/HIT_QUALITY)*i)))
                        Decreasing_angle=asin((ATTACK_HEIGHT*ATTACK_PROP)/ATTACK_SIDE_LENGTH)*(180/pi)
                        amount_lowered=abs(Displacement/(tan(Decreasing_angle)))
                        Current_Height=max_height-amount_lowered
                        x_position=user.get_x_position()+user.get_width()/2+((angle[1]/HIT_QUALITY)*i)
                        y_position=user.get_y_position()+user.get_height()/2-((angle[2]/HIT_QUALITY)*i)-Current_Height/2
                        width=angle[1]/HIT_QUALITY
                        height=Current_Height
                        if Current_Height>0:
                            if SHOW_HITBOX==True:
                                tempRec=GRect(user.get_x_position()+user.get_width()/2+((angle[1]/HIT_QUALITY)*i),user.get_y_position()+user.get_height()/2-((angle[2]/HIT_QUALITY)*i)-Current_Height/2,angle[1]/HIT_QUALITY,Current_Height)
                                tempRec.set_color("#FFFFFF")
                                gw.add(tempRec)
                                gw.Hitbox_list.append(tempRec)
                            entityList.append(attack(x_position,y_position,width,height))
            #The next few lines allow you to change you weapon and turn on and off seeing hitboxes 
            #I change the weapon by changing the ATTACK_HEIGHT,ATTACK_PROP,ATTACK_WIDTH and then recalculating the ATTACK_ANGLE and ATTACK_SIDE_LENGTH with these
            # new variables
            else:
                if gw.x<WINDOW_WIDTH/3 and gw.y<BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2:
                    weapon="Spear"
                    ATTACK_HEIGHT=120
                    ATTACK_PROP=0.5
                    ATTACK_WIDTH=150
                    ATTACK_ANGLE=atan((ATTACK_WIDTH/2)/(ATTACK_HEIGHT*ATTACK_PROP))*(180/pi)
                    ATTACK_SIDE_LENGTH=sqrt((ATTACK_WIDTH/2)**2+(ATTACK_HEIGHT*ATTACK_PROP)**2)
                    HIT_QUALITY=10
                elif gw.x<2*(WINDOW_WIDTH/3) and gw.x>WINDOW_WIDTH/3 and gw.y<BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2:
                    weapon="Sword"
                    ATTACK_HEIGHT=100
                    ATTACK_PROP=0.5
                    ATTACK_WIDTH=50
                    ATTACK_ANGLE=atan((ATTACK_WIDTH/2)/(ATTACK_HEIGHT*ATTACK_PROP))*(180/pi)
                    ATTACK_SIDE_LENGTH=sqrt((ATTACK_WIDTH/2)**2+(ATTACK_HEIGHT*ATTACK_PROP)**2)
                    HIT_QUALITY=10
                elif gw.y<BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2:
                    weapon="Club"
                    ATTACK_HEIGHT=120
                    ATTACK_PROP=0.1
                    ATTACK_WIDTH=30
                    ATTACK_ANGLE=atan((ATTACK_WIDTH/2)/(ATTACK_HEIGHT*ATTACK_PROP))*(180/pi)
                    ATTACK_SIDE_LENGTH=sqrt((ATTACK_WIDTH/2)**2+(ATTACK_HEIGHT*ATTACK_PROP)**2)
                    HIT_QUALITY=10
                if gw.x<WINDOW_WIDTH/3 and gw.y>BATTLE_AREA_HEIGHT+(WINDOW_HEIGHT-BATTLE_AREA_HEIGHT)/2:
                    if SHOW_HITBOX:
                        SHOW_HITBOX=False
                    else:
                        SHOW_HITBOX=True
    def key_action(event):
        #These next four if statements move the graphic in the window and the instance of the class in the proper direction
        if event.get_key()=="<UP>":
            if user.get_y_position()>0:
                entity.move(0,-10)
                ConnectionDict[entity].move(0,-10)
        if event.get_key()=="<DOWN>":
            if user.get_y_position()<WINDOW_HEIGHT:
                user.move(0,10)
                ConnectionDict[user].move(0,10)
        if event.get_key()=="<LEFT>":
            if user.get_x_position()>0:
                user.move(-10,0)
                ConnectionDict[user].move(-10,0)
        if event.get_key()=="<RIGHT>":
            if user.get_x_position()<WINDOW_WIDTH:
                user.move(10,0)
                ConnectionDict[user].move(10,0)
    #This tracks where your mouse is so when you click it can calculate at what angle the attack is going to be
    def mouse_move_event(event):
        gw.x,gw.y=event.get_x(),event.get_y()
        gw.first=True
              
    gw.set_interval(entity_mover,10)
    gw.add_event_listener("click",click_event)
    gw.add_event_listener("mousemove",mouse_move_event)
    gw.add_event_listener("key", key_action)

if __name__ == "__main__":
    #This look exists so you don't have to run the code over and over, you can instead just respond to the prompt in the terminal
    Active=True
    while Active:
        level=input("What level would you like to choose(1-6)")
        if level=="exit":
            Active=False
            continue
        create_entities(int(level)-1)
        create_window(int(level))
