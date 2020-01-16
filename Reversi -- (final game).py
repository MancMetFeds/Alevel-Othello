from tkinter import ttk
from tkinter import *
import tkinter as tk
from functools import*
from re import *
import time
import search
from CPU_player import *
import CPU_player as AI
from magic_hat__final_game import *
import magic_hat__final_game as very
from tkinter import messagebox
import os


#variables that are used for numerous settings, no need to touch as they dont affect core functionality
root = Tk()
root.geometry("400x400")
root.title("Reversi")
root.resizable(width=False, height=False)
cpu_present=True
avatar='Guest'
highlight_col="Yellow"
backgroundimg = PhotoImage(file="assets\\wooden_table.gif")
backgroundimg.image = backgroundimg
backgroundcol = Label(image=backgroundimg)
backgroundcol.place(y=0, x=0, relwidth=1, relheight=1)
switch = 0
player_name = "Guest"
theme_values = ['winnative', 'clam', 'alt', 'default', 'vista', 'xpnative']
colours = ['blue','red','green','yellow', 'gray', 'light gray']
song_list = ['jazz','chong man floor smasher','A Cosby Classic','Darude Sandstorm','Manuel Gas', 'A Seinfeld Tune','We Are Number One', 'Running in the 90s']
avatardict={'Guest':['Guest','Guest'], 'Cream of The Crop':['Andrew','Cropper'], 'An Oxford Man':['David','Williams'],'Miss Em Bezzle':['julie', 'smooth'], 'Crazy Crop':['Mike','Wilshire']}
avatarslist=['Cream of The Crop', 'An Oxford Man','Miss Em Bezzle', 'Crazy Crop']
s = ttk.Style() 
current_theme = "vista"
current_player=None
usual=["game", "optionsbut","Rules","login", "player_display"]
#playerimage=None
#avatarimage=PhotoImage("C:\\Users\\Tom Hatton\\Documents\\Visual Studio 2017\\Projects\\NEA reversi\\NEA reversi\\resources\\question mark.gif")
logged_in = False
current_font='font'
current_background='background'
bg_col = 'light gray'
fg_col = None
current_volume=0.5
current_user="Guest"
#print(current_song)
cpu_player="B"
chosen_peice="w"
white=PhotoImage(file="assets\\_white_top.gif")
black=PhotoImage(file="assets\\_black_top.gif")
already_made=["game_board.grid2","game_board.grid3", "game_board.grid0", "game_board.gridqq"]
black_sides=[]
white_sides=[]

#the 3D array that holds values for the porad places aswell as the button names as each place on the board is a induvidual button, i did this for simplicity. for example; the button object called game_board.grido is empty hence the "E", and its x co ordinate is 1 and its y coorrdinate is 2
#x, y coordinates are given backwards inorder to make some nexter iteration easier later on in the code.
#each 2nd dimentional array is a row in the board. 
board= [[["game_board.gridq","E","1","1"],["game_board.gridw","E","1","2"],["game_board.gride","E","1","3"],["game_board.gridr","E","1","4"],["game_board.gridt","E","1","5"],["game_board.gridy","E","1","6"],["game_board.gridu","E","1","7"],["game_board.gridi","E","1","8"]]
                        ,[["game_board.grido","E","2","1"],["game_board.gridp","E","2","2"],["game_board.grida","E","2","3"],["game_board.grids","E","2","4"],["game_board.gridd","E","2","5"],["game_board.gridf","E","2","6"],["game_board.gridg","E","2","7"],["game_board.gridh","E","2","8"]]
                        ,[["game_board.gridj","E","3","1"],["game_board.gridk","E","3","2"],["game_board.gridl","E","3","3"],["game_board.gridz","E","3","4"],["game_board.gridx","E","3","5"],["game_board.gridc","E","3","6"],["game_board.gridv","E","3","7"],["game_board.gridb","E","3","8"]]
                        ,[["game_board.gridn","E","4","1"],["game_board.gridm","E","4","2"],["game_board.grid1","E","4","3"],["game_board.grid2","w","4","4"],["game_board.grid3","b","4","5"],["game_board.grid4","E","4","6"],["game_board.grid5","E","4","7"],["game_board.grid6","E","4","8"]]
                        ,[["game_board.grid7","E","5","1"],["game_board.grid8","E","5","2"],["game_board.grid9","E","5","3"],["game_board.grid0","b","5","4"],["game_board.gridqq","w","5","5"],["game_board.gridww","E","5","6"],["game_board.gridee","E","5","7"],["game_board.gridrr","E","5","8"]]
                        ,[["game_board.gridtt","E","6","1"],["game_board.gridyy","E","6","2"],["game_board.griduu","E","6","3"],["game_board.gridii","E","6","4"],["game_board.gridoo","E","6","5"],["game_board.gridpp","E","6","6"],["game_board.gridaa","E","6","7"],["game_board.gridss","E","6","8"]]
                        ,[["game_board.griddd","E","7","1"],["game_board.gridff","E","7","2"],["game_board.gridgg","E","7","3"],["game_board.gridhh","E","7","4"],["game_board.gridjj","E","7","5"],["game_board.gridkk","E","7","6"],["game_board.gridll","E","7","7"],["game_board.gridzz","E","7","8"]]
                        ,[["game_board.gridxx","E","8","1"],["game_board.gridcc","E","8","2"],["game_board.gridvv","E","8","3"],["game_board.gridbb","E","8","4"],["game_board.gridnn","E","8","5"],["game_board.gridmm","E","8","6"],["game_board.grid11","E","8","7"],["game_board.grid22","E","8","8"]]]
#this is unimportant to the core game but is required for scoring purposes DO NOT TOUCH
class profile():
        bg="grey"
        border="black"
        def __init__(self, x, y, firstname, surname, player_image, current_score, countercol, player):
                if player_image=='Guest':
                        #self.player_image='question mark'
                        num=10
                else:
                        #self.player_image=player_image
                        num=4
                self.x=x
                self.y=y
                self.firstname=firstname
                self.surname=surname
                self.current_score=current_score
                self.countercol=countercol
                #avatarimage=PhotoImage(file="C:\\Users\\Tom Hatton\\Documents\\Visual Studio 2017\\Projects\\NEA reversi\\NEA reversi\\resources\\"+str(self.player_image)+".gif")
                #self.tempimg=avatarimage.subsample(num)
        def card(self):
                self.card=Canvas(width=151, height=100, highlightbackground=profile.border, relief=GROOVE)
                self.card.place(x=self.x, y=self.y)
                self.fore=Label(self.card, text=("First Name: "+(avatardict[avatar])[0]))
                self.fore.place(x=5,y=58)
                self.sur=Label(self.card, text=("Last Name: "+(avatardict[avatar])[1]))
                self.sur.place(x=5,y=78)
                self.photoid=Label(self.card, height=50,width=50, image="")
                self.photoid.place(x=4,y=4)
                self.score=Label(self.card,text=str(self.current_score))
                self.score.place(x=100, y=20)
                self.colour=Label(self.card,text=str(self.countercol))
                self.colour.place(x=100, y=40)
                #self.photoid.image=self.tempimg
                #self.photoid.configure(image=self.tempimg)

        def update_score(update, points):
                update.current_score=points

        def configurer(con, widgetname):
                getattr(con, widgetname).configure(text=str(con.current_score))




#this class is for creating message box objects that may appear during game interactions. they come int he form of a pop up window.
class message:

        def error_(message_title, the_message):
                return messagebox.showerror(message_title, the_message)

        def info_(message_title, the_message):
                return messagebox.showinfo(message_title, the_message)

        def warning_(message_title, the_message):
                return messagebox.showwarning(message_title, the_message)

#an example of how the button list will fill up vv           
#button_name_list=["self.gridq", "self.gridw", "self.gride", "self.gridr", "self.gridt", "self.gridy", "self.gridu", "self.gridi", "self.grido", "self.gridp", "self.grida", "self.grids", "self.gridd", "self.gridf", "self.gridg", "self.gridh", "self.gridj", "self.gridk", "self.gridl", "self.gridz", "self.gridx", "self.gridc", "self.gridv", "self.gridb", "self.gridn", "self.gridm", "self.grid1", "self.grid2", "self.grid3", "self.grid4", "self.grid5", "self.grid6", "self.grid7", "self.grid8", "self.grid9", "self.grid0", "self.gridqq", "self.gridww", "self.gridee", "self.gridrr", "self.gridtt", "self.gridyy", "self.griduu", "self.gridii", "self.gridoo", "self.gridpp", "self.gridaa", "self.gridss", "self.griddd", "self.gridff", "self.gridgg", "self.gridhh", "self.gridjj", "self.gridkk", "self.gridll", "self.gridzz", "self.gridxx", "self.gridcc", "self.gridvv", "self.gridbb", "self.gridnn", "self.gridmm", "self.grid11", "self.grid22"]


#below is the largest class in the code,
#this class is the board object.

class Board(object):
	#properties defining the moves that have already been made these are astored as strings in an array of undefined length.
        already_made=["game_board.grid2","game_board.grid3", "game_board.grid0", "game_board.gridqq"]

        #constructor class, __init__ runs automatically.
        def __init__(self):
                self.piece_placed=0
                self.bg="light green"

        def eightbyeight(self,*args,**kwargs):
                for i in range(8):
                                for e in range(8) :
                                        setattr(self, board[i][e][0][11:], Button(width=8, height=4, relief=SUNKEN, bg=self.bg, bd="0.25c", cursor="hand1"
                                                                                          , activebackground="yellow"
                                                                                          , takefocus=1, compound="center"
                                                                                          , state=NORMAL, fg="dark blue"
                                                                                          , command=partial(self.move_checker, (board[i][e][0][11:]), str(i), str(e)))) #add "text=str(board[i][e][0][2:])" to display button names on buttons for testing
                                        (getattr(self, board[i][e][0][11:])).grid(row=i, column=e)
                                        if board[i][e][1]=='w' or board[i][e][1]=='W':
                                                #print(board[i][e][0])
                                                (getattr(self, board[i][e][0][11:])).config(image=white, height= 65, width=60, anchor=CENTER)
                                        elif board[i][e][1]== 'b' or board[i][e][1]=='B':
                                                (getattr(self, board[i][e][0][11:])).config(image=black, height= 65, width=60, anchor=CENTER)
                self.state_changer("w","b")
                return

        def move_checker(win, button_id, rownum, colnum):
                win.button_id="game_board."+button_id
                rownum=int(rownum)
                colnum=int(colnum)
                if win.button_id in game_board.already_made:
                        message.error_("invalid move", "you tried to make a move that had already been made!")
                elif win.button_id not in game_board.already_made:
                        game_board.already_made.append(win.button_id)
                        win.piece(button_id, rownum, colnum)

        def piece (peice, button_id, rownum, colnum):
                peice.piece_placed+=1
                if(peice.piece_placed)%2==0:
                        peice.player="b"
                        board[rownum][colnum][1]=peice.player.upper()
                        peice.change_from="w"
                        mech.rows(button_id, peice.player, rownum, colnum, peice.change_from)
                        mech.columns(button_id, peice.player, rownum, colnum, peice.change_from)
                        mech.diaglr(button_id, peice.player, rownum, colnum, peice.change_from)
                        for row in board:
                                for column in row:
                                        if column[1]=='w' or column[1]=='W':
                                                eval(j[0]).config(image=white, height= 65, width=60, anchor=CENTER)
                                        elif j[1]== 'b' or j[1]=='B':
                                                eval(j[0]).config(image=black, height= 65, width=60, anchor=CENTER)
                        updater()
                        peice.state_changer("w","b")

                else:
                        peice.player="w"
                        board[rownum][colnum][1]=peice.player.upper()
                        peice.change_from="b"
                        mech.rows(button_id, peice.player, rownum, colnum, peice.change_from)
                        mech.columns(button_id, peice.player, rownum, colnum, peice.change_from)
                        mech.diaglr(button_id, peice.player, rownum, colnum, peice.change_from)
                        for k in board:
                                for j in k:
                                        if j[1]=='w' or j[1]=='W':
                                                getattr(game_board, j[0][11:]).config(image=white, height= 65, width=60, anchor=CENTER)
                                        elif j[1]== 'b' or j[1]=='B':
                                                getattr(game_board, j[0][11:]).config(image=black, height= 65, width=60, anchor=CENTER)
                        updater()
                        peice.state_changer("b","w")
                        root.update()
                        opponent.cpu_get(board, cpu_player)

        def state_changer(self, player, change_from):
                self.expression1=re.compile('('+player+'('+change_from+'+)'+player.upper()+')')
                self.expression2=re.compile('('+player.upper()+'('+change_from+'+)'+player+')')
                moves=AI.CPU(board, player, self.expression1, self.expression2, "DISABLED")
                self.valid_moves=[]
                for i in moves :
                        self.valid_moves.append(i[0])
                for i in range(8):
                        for e in range(8):
                                if board[i][e][0]in self.valid_moves:
                                        getattr(self,board[i][e][0][11:]).configure(state=NORMAL, bg="yellow")
                                else:
                                        getattr(self,board[i][e][0][11:]).configure(state=DISABLED,  bg=self.bg)
                del self.valid_moves[:]

class mechanics():
        def rows (x, button_id, player, rownum, colnum, change_from, **kwargs):
                x.placevalues=[]
                x.expression1=re.compile('('+player+'('+change_from+'+)'+player.upper()+')')
                x.expression2=re.compile('('+player.upper()+'('+change_from+'+)'+player+')')
                x.row=""
                x.pvs=""
                for i in board[rownum]:
                        x.row+=i[1]        
                for sequence in finditer(x.expression1, x.row):
                        x.pvs=sequence.span()
                if len(x.pvs)>0:
                        for i in x.pvs:                    
                                i=int(i)
                                x.placevalues.append(i)          
                        for i in range ((x.placevalues[0])+1, (x.placevalues[1])-1):                  
                                board[rownum][i][1]=player
                        x.placevalues=[]               
                else:
                        pass
                x.pvs=""                
                for sequence in finditer(x.expression2, x.row):
                        x.pvs=sequence.span()
                if len(x.pvs)>0:
                        for i in x.pvs:                    
                                i=int(i)
                                x.placevalues.append(i)          
                        for i in range ((x.placevalues[0])+1, (x.placevalues[1])-1):                  
                                board[rownum][i][1]=player
                        x.placevalues=[]               
                else:
                        pass
                x.row=""

        def columns (y, button_id, player, rownum, colnum, change_from, **kwargs):
                        y.placevalues=[]
                        y.column=""
                        y.expression1=re.compile('('+player+'('+change_from+'+)'+player.upper()+')')
                        y.expression2=re.compile('('+player.upper()+'('+change_from+'+)'+player+')')
                        y.pvs=""
                        for n in range(0,len(board)):
                                y.column+=board[n][colnum][1]
                        for sequence in finditer(y.expression1, y.column):
                                y.pvs=sequence.span()
                        if len(y.pvs)>0:
                                for v in y.pvs:                    
                                        v=int(v)
                                        y.placevalues.append(v)          
                                for b in range ((y.placevalues[0])+1, (y.placevalues[1])-1):                  
                                        board[b][colnum][1]=player
                                y.placevalues=[]               
                        else:
                                pass
                        y.pvs=""                
                        for sequence in finditer(y.expression2, y.column):
                                y.pvs=sequence.span()
                        if len(y.pvs)>0:
                                for m in y.pvs:
                                        y.placevalues.append(int(m))          
                                for l in range ((y.placevalues[0])+1, (y.placevalues[1])-1):                                          
                                        board[l][colnum][1]=player
                                y.placevalues=[]               
                        else:
                                pass

        def diaglr (xy, button_id, player, rownum, colnum, change_from, **kwargs):
                        def regular_expression(button_id, player, rownum, colnum, change_from, stringsequence, cells):
                                xy.expression1=re.compile('('+player+'('+change_from+'+)'+player.upper()+')')
                                xy.expression2=re.compile('('+player.upper()+'('+change_from+'+)'+player+')')
                                xy.pvs=""                    
                                for sequence in finditer(xy.expression1, stringsequence):
                                        xy.pvs=sequence.span()
                                if len(xy.pvs)>0:
                                        for q in xy.pvs:
                                                q=int(q)
                                                xy.placevalues.append(q)
                                        for w in range (xy.placevalues[0], xy.placevalues[1]):
                                                try:
                                                        board[int(cells[w][2])][w][1]=player
                                                except IndexError:
                                                        None
                                        xy.placevalues=[]               
                                else:
                                        pass
                                xy.pvs=""                
                                for sequence in finditer(xy.expression2, stringsequence):
                                        xy.pvs=sequence.span()
                                if len(xy.pvs)>0:
                                        for r in xy.pvs:                    
                                                r=int(r)
                                                xy.placevalues.append(r)          
                                        for t in range (xy.placevalues[0], xy.placevalues[1]):            
                                                try:
                                                        board[int(cells[t][2])][t][1]=player
                                                except IndexError:
                                                        None
                                        xy.placevalues=[]               
                                else:
                                        pass
                                stringsequence=""
                                cells=[[],[],[],[],[],[],[],[]]
                                return
                        xy.diagLR=""
                        cells=[[],[],[],[],[],[],[],[]]        
                        xy.placevalues=[]
                        x=1
                        if rownum > 7-colnum:
                                x+=7-colnum                
                        elif rownum < 7-colnum:
                                x+=rownum
                        elif rownum == 7-colnum:
                                x+=7-colnum
                        xy.diagLR=""
                        try:
                                for u in range(0 , colnum+1):
                                        xy.diagLR+=board[rownum+u][colnum-u][1]
                                        cells[colnum-u].append(board[rownum+u][colnum-u][0])
                                        cells[colnum-u].append(board[rownum+u][colnum-u][1])
                                        cells[colnum-u].append(str(rownum+u))
                                        cells[colnum-u].append(str(colnum-u))
                                xy.diagLR=xy.diagLR[::-1]
                        except IndexError:
                                xy.diagLR=xy.diagLR[::-1]     
                        try:
                                for a in range(1, x):
                                        xy.diagLR+=board[rownum-a][colnum+a][1]
                                        cells[colnum+a].append(board[rownum-a][colnum+a][0])
                                        cells[colnum+a].append(board[rownum-a][colnum+a][1])
                                        cells[colnum+a].append(str(rownum-a))
                                        cells[colnum+a].append(str(colnum+a))
                        except IndexError:
                                None
                        regular_expression(button_id, player, rownum, colnum, change_from, xy.diagLR, cells)
                        cells=[[],[],[],[],[],[],[],[]]
                        x=1
                        if rownum < colnum:
                                x+=7-rownum                
                        elif rownum > colnum:
                                x+=colnum
                        elif rownum == colnum:
                                x+=7-rownum
                        xy.diagRL=""
                        try:
                                for i in range(colnum, -1, -1):
                                        xy.diagRL+=board[rownum-i][colnum-i][1]
                                        cells[colnum-i].append(board[rownum-i][colnum-i][0])
                                        cells[colnum-i].append(board[rownum-i][colnum-i][1])
                                        cells[colnum-i].append(str(rownum-i))
                                        cells[colnum-i].append(str(colnum-i))
                        except IndexError:
                                None
                        try:
                                e=1
                                for i in range(colnum, 7):
                                        xy.diagRL+=board[rownum+e][colnum+e][1]
                                        cells[colnum+e].append(board[rownum+e][colnum+e][0])
                                        cells[colnum+e].append(board[rownum+e][colnum+e][1])
                                        cells[colnum+e].append(str(rownum+e))
                                        cells[colnum+e].append(str(colnum+e))
                                        e+=1
                        except IndexError:
                                None
                        regular_expression(button_id, player, rownum, colnum, change_from, xy.diagRL, cells)            
                        board[rownum][colnum][1]=player.lower()
                        return
                                
class game_player():
        def cpu_get(cpu, board, cpu_player):
                best_cell=[]
                cpu.upper_player=cpu_player.upper()
                cpu.lower_player=cpu_player.lower()
                cpu.change_from='w'
                cpu.expression1=re.compile('('+cpu.upper_player+'('+cpu.change_from+'+)'+cpu.lower_player+')')
                cpu.expression2=re.compile('('+cpu.lower_player+'('+cpu.change_from+'+)'+cpu.upper_player+')')
                final=AI.CPU(board,  cpu_player, cpu.expression1, cpu.expression2, None)
                best_cell=very.decide(final)
                if best_cell!="pass":
                        xco=eval(best_cell[1]).winfo_rootx()
                        yco=eval(best_cell[1]).winfo_rooty()
                        while True:
                                if root.winfo_pointerx() != xco+40 and root.winfo_pointery() != yco+40:
                                        pyautogui.moveTo(int(xco+40), int(yco+40), duration=0.5, pause=0)
                                else:
                                        pyautogui.click()
                                        finalchoices=[]
                                        best_cell=[]
                                        break
                                        root.update()
                else:
                        #edit turn namer label to dispaly word PASS
                        best_cell=[]
                        pass
                return

def updater():
        black=0
        white=0
        for i in range(8):
                for e in range(8):
                        if board[i][e][1] !="E":
                                if board[i][e][1]=="b":
                                        black+=1
                                        
                                elif board[i][e][1]=="w":
                                        white+=1
                                         
                        else:
                                None
        prof1.update_score(black)
        prof2.update_score(white)
        prof1.configurer("score")
        prof2.configurer("score")

class buttons():
        style='TButton'
        def __init__(self, x, y,text,commands, width):
                self.x=x
                self.y=y
                self.text=text
                self.commands=commands
                self.width=width
                self.but=ttk.Button(root, text=self.text, command=self.commands, style=buttons.style,width=self.width)
                self.but.place(x=self.x, y=self.y)

        def destroy(dest):
                dest.but.destroy()

class labels():
        style='TLabel'
        def __init__(self, x, y, text, font_options, width):
                self.x=x
                self.y=y
                self.text=text
                self.width=width
                self.font_options=font_options
                self.lab=ttk.Label(text=self.text, style=labels.style, width=self.width, font=self.font_options)
                self.lab.place(x=self.x, y=self.y)

        def destroy(dest):
                dest.lab.destroy()

        def binder_(bind__, action, command):
                bind__.action=action
                bind__.command=command
                bind__.lab.bind(bind__.action,bind__.command)

        def configurer(self, options):
                self.options=options
                self.lab(self.options)

class entrys():
        def __init__(self, x, y, show_):
                self.x=x
                self.y=y
                self.show=show_
                self.ent=Entry(show=self.show)
                self.ent.place(x=self.x,y=self.y)

        def getter(get_):
                return (get_.ent.get())

        def destroy(dest):
                dest.ent.destroy()

class combo():
        style='TCombobox'
        def __init__(self, x,y,values, eventname, title, current):
                self.x=x
                self.y=y
                self.values=values
                self.eventname=eventname
                self.title=title
                self.current=current
                self.combobox=ttk.Combobox(values=self.values)
                self.combobox.place(x=self.x,y=self.y)
                #print(title)
                self.combobox.set(self.title)
                self.combobox.bind("<<ComboboxSelected>>", self.getmethod)

        def destroy(dest):
                dest.combobox.destroy()

        def getmethod(self, event):
                if self.eventname=="__get_theme":
                        self.__get_theme(event)
                elif self.eventname=="get_music":
                        val=self.combobox.get()
                        self.get_music(event, val)
                elif self.eventname=="__get_bg_colour":
                        self.__get_bg_colour(event)

        def __get_theme(this, event):
                try:
                        global current_theme
                        current_theme= this.combobox.get()
                        this.combobox.set(current_theme)
                except:
                        pass
                finally:
                        s.theme_use(str(current_theme))
                return
        """
        def get_music(self, event, val):
                global current_song
                current_song=val
                pygame.mixer.stop()
                pygame.mixer.init()
                backgroundsound = pygame.mixer.Sound('C:\\Users\\Tom Hatton\\Documents\\Visual Studio 2017\\Projects\\NEA reversi\\NEA reversi\\resources\\'+str(current_song)+'.wav')
                backgroundsound.play()
                backgroundsound.set_volume(current_volume)
        """
        def __get_bg_colour(that, event):
                widgets = ['TButton','TScale','TLabel','TCombobox']
                try:
                        global bg_col
                        bg_col = that.combobox.get()
                except Exception:
                        None
                for i in widgets:
                        s.theme_settings(current_theme, {i:{"map":{"background":[("!disabled", bg_col)]}}})
                        root.update()
                return
        """
        def set_avatar(self, event):
                global avatarimage, avatar
                avatar=self.combobox.get()
                avatarimage= PhotoImage(file='C:\\Users\\Tom Hatton\\Documents\\Visual Studio 2017\\Projects\\NEA reversi\\NEA reversi\\resources\\'+avatar+'.gif')
                self.combobox.set(avatar)
        """
class sliders():
        from_=0
        to=1
        def __init__(self, x, y, orient, length, current):
                self.x=x
                self.y=y
                self.current=current
                self.orient=orient
                self.length=length
                self.slide=ttk.Scale(from_=sliders.from_, to=sliders.to, command=partial(self.switched), orient=eval(self.orient), length=self.length, value=self.current)
                self.slide.place(x=self.x, y=self.y)
        def destroy(dest):
                dest.slide.destroy()
        def switched(click, slide):
                try:
                        click.current=click.slide.get()
                except Exception:
                        pass
                backgroundsound.set_volume(float(click.current))
                return

def gameboard():
        root.geometry("800x690")
        root.title("Reversi")
        root.resizable(width=False, height=False)
        backgroundimg = PhotoImage(file="assets\\wooden_table.gif")
        backgroundimg.image = backgroundimg
        backgroundcol = Label(root, image=backgroundimg)
        backgroundcol.place(y=0, x=0, relwidth=1, relheight=1)
        prof1.card()
        prof2.card()
        game_board.eightbyeight()
        
        #print("AAAAAAAAAAAAA")

def Rules():
        cleaner()#usual
        back = buttons(60,60 ,"back", (lambda:[back.destroy(), rulelist.destroy(), screen()]), 20)
        rulelist = labels(50, 60, "", None, 20)
        
def options():
        cleaner()#usual
        subtitle0 = labels(120,40,"Music volume", None, 20)
        music = sliders(10, 60, 'HORIZONTAL', 300, current_volume)
        themes = combo(10,90,theme_values,"__get_theme", current_theme, current_theme)
        bgcolour = combo(180, 90, colours, "__get_bg_colour", bg_col, bg_col)
        avatarimage = combo( 10, 150, avatarslist, 'set_avatar', avatar, avatar)
        musicchoice=combo(10,130,song_list,"get_music",current_song, str(current_song))
        savebutton=buttons(95,280,"Save", (lambda:[save_file()]), 10)
        back = buttons(175,280, "back", (lambda:[cleaner(), screen()]), 10)

def cleaner():
        list = root.winfo_children()
        #print(list)
        for widgets in list:
                widgets.destroy()
        backgroundimg = PhotoImage(file="assets\\wooden_table.gif")
        backgroundimg.image = backgroundimg
        backgroundcol = Label(image=backgroundimg)
        backgroundcol.place(y=0, x=0, relwidth=1, relheight=1)
        return

def switchmode(event):
        cleaner()
        log_in("create account")
        return

def load(account):
        current_background=account['background']
        current_font=account['font']
        current_volume=account['Volume']
        current_theme=account['Theme']
        current_user=account['Username']
        bg_col=account['backgroundcol']
        get_theme(None)
        music.switched(None)
        get_bg_colour(None)
        logged_in=True
        cleaner()
        screen()

def unload():
        current_background='background'
        current_font='font'
        current_volume=0.5
        current_theme='vista'
        current_user="Guest"
        bg_col='light gray'
        get_theme(None)
        music.switched(None)
        get_bg_colour(None)
        logged_in=False
        cleaner()
        screen()

def log_in(mode):
        alertlabel=labels(180,180,None,None, 20)
        try:
                cleaner()
        except Exception:
                pass
        usernamelabel=labels(85,70,"Username:",None, 20)
        usernameentry=entrys(145,70,None)
        passwordlabel=labels(85,90,"Password:",None, 20)
        passwordentry=entrys(145,90,"*")
        if mode == "login":
                signinbutton=buttons(150,120, "Sign in", (lambda:[csver(str(usernameentry.getter()),str(passwordentry.getter()), str(None), "login")]), 20)
                createaccountlabel=labels(85,110,"Create account", None, 20)
                createaccountlabel.binder_('<Button-1>', partial(switchmode))
        elif mode == "create account":
                passwordconfirmationlabel = labels(85,110, "Confirm\nPassword:",  (None, 10), 20)
                passwordconfirmationentry = entrys(145,110,"*")
                signinbutton = buttons(150,150,"Create account", (lambda:[csver(str(usernameentry.getter()),str(passwordentry.getter()), str(passwordconfirmationentry.getter()), mode)]), 20)
                return
        return

def csver(username, password, confirmed_password, mode):
        fieldnames = ['Username', 'Password', 'Volume', 'background', 'backgroundcol','Theme','font']
        if mode == "create account":
                if password == confirmed_password:
                        with open('\\resources\\LOG.csv', 'r') as csvfile:
                                #print(csvfile)
                                readfromfile = csv.DictReader(csvfile, fieldnames=fieldnames)
                                for i in readfromfile:
                                        if i['Username'] == username:
                                                #print("username already taken")
                                                alertlabel.configurer(("username already taken", "#FF0000"))
                                                return
                                        else:
                                                pass
                        current_user=username
                        with open('\resources\LOG.csv', 'a') as csvfile:
                                writetofile = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                writetofile.writerow({'Username': str(username),
                                                                                'Password':str(password),
                                                                                'Volume':str(current_volume),
                                                                                'background':str(current_background),
                                                                                'backgroundcol':str(bg_col),
                                                                                'Theme':str(current_theme),
                                                                                'font':str(current_font)})
                                cleaner(["usernamelabel","usernameentry",
                                                                        "passwordlabel","passwordentry",
                                                                        "createaccountlabel","signinbutton",
                                                                        "passwordconfirmationlabel",
                                                                        "passwordconfirmationentry","alertlabel"])
                                screen()
                                                
                else:
                        #print("passwords don't match")
                        return
        elif mode == "login":
                        try:
                                with open('\\resources\\LOG.csv', 'r') as csvfile:
                                        readfromfile = csv.DictReader(csvfile, fieldnames=fieldnames)
                                        for registered_user in readfromfile:
                                                #print(registered_user)
                                                if registered_user['Username'] == username and registered_user['Password'] == password:
                                                        load(registered_user)
                                                        return(username)
                                                else:
                                                        raise Exception
                        except Exception:
                                alertlabel.configurer(("username not found or password incorrect", "#FF0000"))
                                return

def quitgame(true):
        if true==True:
                quit()
        else:
                quit=True

def save_file():
        fieldnames = ['Username','Password', 'Volume', 'background', 'backgroundcol','Theme','font']
        if current_user != "Guest":
                with open('\\resources\\LOG.csv', 'r') as csvfile:
                        with open('\\resources\\LOG.csv', 'w') as template:
                                writer= csv.DictWriter(template, fieldnames=fieldnames)    
                                reader= csv.DictReader(csvfile, fieldnames=fieldnames)
                                for i in reader:
                                        if i['Username']!=current_user:
                                                #print(i['Username'])
                                                pass                    
                                        elif i['Username']==current_user:
                                                #print(i, i['Volume'])
                                                writer.writerow({'Username':str(current_user),'Password':i['Password'], 'Volume':str(current_volume), 'background':str(current_background), 'backgroundcol':str(bg_col),'Theme':str(current_theme),'font':str(current_font)})
                csvfile.close(),
                template.close()
        else:
                pass
        return

def screen():
        player_display = labels(0,0,current_user, None, len(current_user))
        game = buttons(145,146, "start game", (lambda:[cleaner(), gameboard(), player_name]), 15)
        optionsbut = buttons(145,173, "Options", (partial(options)), 15)
        rules = buttons(145, 200, "Rules of Reversi", (partial(Rules)), 15)
        if logged_in == False:
                login = buttons(5, 370, "Log In", (lambda:[log_in("login"), print(current_user)]), 10)
        elif logged_in == True:
                login = buttons(5, 370, "Sign Out", (partial(unload)), 10)

cpu_present=True
prof1=profile(640, 20, "David","Williams", str(avatar), 0, "Black", "1")
prof2=profile(640, 500, "Andrew", "Cropper", str(avatar), 0, "White", "2")
mech=mechanics()
opponent=game_player()
game_board=Board()
screen()
mainloop()
