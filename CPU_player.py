from re import *
import search
from functools import partial
#rename to valid move finder
def CPU(board, cpu_player, expression1, expression2, desire):
	player=cpu_player.upper()
	stringsandcells=[]
	bin=[]
	currentcell=[]
	stringURDiag=""
	stringULDiag=""
	stringDRDiag=""
	stringDLDiag=""
	rowstring=""
	colstring=""
	rowlist=[]
	collist=[]
	diaglist=[]
	celllist=[]
	finalchoices=[]
	vals=""
	def compiler(celllist):
		done=[]
		for i in celllist:
			comparative=i
			if str(comparative[1]) in done:
				None
			else:
				for e in celllist:
					if comparative[1]==e[1] and comparative[2]==e[2] and comparative[3]==e[3] and comparative[4]!=e[4]:
						comparative[0]+=e[0]
					else:
						None
				finalchoices.append(comparative)
				done.append(str(comparative[1]))
		for i in celllist:
			del i
		return

	def rowsearch(y,expression1, expression2, rowstring,board):
		totalpoints=0
		cell=[]
		vals=""
		rowlist=[]
		for p in range(8):
			rowlist.append(board[y][p][1])
		for i in range(8):
			vals=""
			if rowlist[i]=='E':
				rowlist[i]=player
				rowstring=""
				for r in rowlist:
					rowstring+=r
				for sequence in finditer(expression1,rowstring):
					vals=sequence.span()
				try:
					for f in vals:
						cell.append(int(f))
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints, board[y][i][0],y,i, "rowl"])
					stringsandcells.append([board[y][i][0], stringDRDiag])
					cell=[]
				except Exception:
					None
				vals=""
				totalpoints=0
				for sequence in finditer(expression2,rowstring):
					vals=sequence.span()
				try:
					for f in vals:
						cell.append(int(f))
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints, board[y][i][0],y,i, "rowr"])
					stringsandcells.append([board[y][i][0], stringDRDiag])
					cell=[]
				except Exception:
					vals=""
					None
				rowlist[i]='E'
				cell=[]
				totalpoints=0
				rowstring=""
				for e in rowlist:
					rowstring+=e
			else:
				pass
		rowlist=[]
		rowstring=""
		return

	def colsearch(x,expression1, expression2, colstring, board):
		#funcsran.append("colsearch")
		totalpoints=0
		cell=[]
		vals=""
		collist=[]
		for p in range(8):
			collist.append(board[p][x][1])
		for i in range(8):
			vals=""
			if collist[i]=='E':
				collist[i]=player
				colstring=""
				for r in collist:
					colstring+=r
				for sequence in finditer(expression1,colstring):
					vals=sequence.span()
				try:
					for f in vals:
						cell.append(int(f))
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints, board[i][x][0],i,x, "colup"])
					stringsandcells.append([board[i][x][0], stringDRDiag])
					cell=[]
				except Exception:
					None
				vals=""
				totalpoints=0
				for sequence in finditer(expression2,colstring):
					vals=sequence.span()
				try:
					for f in vals:
						cell.append(int(f))
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints, board[i][x][0],i,x, "coldown"])
					stringsandcells.append([board[i][x][0], colstring])
					cell=[]
				except Exception:
					vals=""
					None
				collist[i]='E'
				colstring=""
				cell=[]
				totalpoints=0
				for e in collist:
					colstring+=e
			else:
				pass
		collist=[]
		colstring=""
		return

	def DLDiag(cellname,x,y,expression1, expression2, stringDLDiag, board):
		totalpoints=0
		cell=[]
		diaglist=[]
		vals=""
		try:
			for i in range(8):
				try:
					xcoord=x+i
					if xcoord<=-1:
						raise IndexError
					else:
						pass
					ycoord=y-i
					if ycoord>7:
						raise IndexError
					else:
						pass
					diaglist.append(board[xcoord][ycoord][1])
				except IndexError:
					None
			if diaglist[0]=='E':
				diaglist[0]=player
				stringDLDiag=""
				for r in diaglist:
					stringDLDiag+=r
				for sequence in finditer(expression2,stringDLDiag):
					vals=sequence.span()
				try:
					for i in vals:
						cell.append(int(i))
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints,board[x][y][0],y,x, "DL"])
					stringsandcells.append([board[x][y][0], stringDLDiag])
				except Exception:
					None
				return
			else:
				raise IndexError
		except IndexError:
			return

	def URDiag(cellname,x,y,expression1, expression2, stringURDiag, board):
		totalpoints=0
		cell=[]
		diaglist=[]
		vals=""
		try:
			for i in range(8):
				try:
					xcoord=x+i
					if xcoord>7:
						raise IndexError
					else:
						pass
					ycoord=y-i
					if ycoord<=-1:
						raise IndexError
					else:
						pass
					diaglist.append(board[xcoord][ycoord][1])
				except IndexError:
					None
			if diaglist[0]=='E':
				diaglist[0]=player
				for r in diaglist:
					stringURDiag+=r
				for sequence in finditer(expression1,stringURDiag):
					vals=sequence.span()
				try:
					for i in vals:
						cell.append(i)
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints,board[x][y][0],y,x, "UR"])
					stringsandcells.append([board[x][y][0], stringURDiag])
				except Exception:
					None
				return
			else:
				raise IndexError
		except IndexError:
			return

	def ULDiag(cellname,x,y,expression1, expression2, stringULDiag, board):
		totalpoints=0
		cell=[]
		diaglist=[]
		vals=""
		try:
			for i in range(8):
				try:
					xcoord=x-i
					if xcoord<=-1:
						raise IndexError
					else:
						pass
					ycoord=y-i
					if ycoord<=-1:
						raise IndexError
					else:
						pass
					diaglist.append(board[xcoord][ycoord][1])
				except IndexError:
					None
			if diaglist[0]=='E':
				diaglist[0]=player
				stringULDiag=""
				for r in diaglist:
					stringULDiag+=r
				for sequence in finditer(expression2,stringULDiag):
					vals=sequence.span()
				try:
					for i in vals:
						cell.append(i)
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints,board[x][y][0],y,x, "UL"])
					stringsandcells.append([board[x][y][0], stringULDiag])
				except Exception:
					None
				return
			else:
				raise IndexError
		except IndexError:
			return
	def DRDiag(cellname,x,y,expression1, expression2, stringDRDiag, board):
		totalpoints=0
		cell=[]
		diaglist=[]
		vals=""
		try:
			for i in range(8):
				try:
					xcoord=x+i
					if xcoord>7:
						raise IndexError
					else:
						pass
					ycoord=y+i
					if ycoord>7:
						raise IndexError
					else:
						pass
					diaglist.append(board[xcoord][ycoord][1])
				except IndexError:
					None
			if diaglist[0]=='E':
				diaglist[0]=player
				stringDRDiag=""
				for r in diaglist:
					stringDRDiag+=r
				for sequence in finditer(expression1,stringDRDiag):
					vals=sequence.span()
				try:
					for i in vals:
						cell.append(int(i))
					totalpoints+=cell[1]-cell[0]-1
					celllist.append([totalpoints,board[x][y][0],y,x, "DR"])
					stringsandcells.append([board[x][y][0], stringDRDiag])
				except Exception:
					None
				return
			else:
				raise IndexError
		except IndexError:
			return
	def cpu(board, cpu_player, expression1, expression2):
		for y in range(8):
			rowsearch(y,expression1, expression2, rowstring,board)
			colsearch(y,expression1, expression2, colstring,board)
			for x in range(8):
				currentcell=board[y][x]
				URDiag(currentcell[1],x,y,expression1, expression2, stringURDiag, board)
				ULDiag(currentcell[1],x,y,expression1, expression2, stringULDiag, board)
				DRDiag(currentcell[1],x,y,expression1, expression2, stringDRDiag, board)
				DLDiag(currentcell[1],x,y,expression1, expression2, stringDLDiag, board)
		compiler(celllist)
		return#(finalchoices)
	
	cpu(board, cpu_player, expression1, expression2)
	if desire=='DISABLED':
		bin=[4,3,2,0]
	else:
		bin=[4]
	for i in finalchoices:
		for placevalue in bin:
			del i[placevalue]
	##print("\n\n\n\n\t\t*******************\n\n\n")
	#for i in board:
	#	#pass
	#	row=""
	#	for e in i:
	#		if e[1]=='E':
	#			row+=" "
	#		else:
	#			row+=e[1]
	#	print(row)
	#for i in stringsandcells:
	#	#pass
	#	print(str(i[0])+" "+str(i[1]))
	return(finalchoices)
#def CPU ():
	
#	#print("#########################################################")    
#	#ai.current_score_B=current_score_B
#	hat=[]
#	upper_player=cpu_player
#	lower_player=cpu_player.lower()
#	change_from='w'
#	current_cell=[]
#	best_cell_diaglr=[0]
#	best_cell_diagrl=[0]
#	best_cell_row=[0]
#	best_cell_column=[0]
#	best_cell=[]
#	imaginary_board=[]
#	imaginary_row_str=""
#	imaginary_column_str=""
#	imaginary_diaglr_str=""
#	imaginary_diagrl_str=""
#	imaginary_diaglr_list=[]
#	imaginary_diagrl_list=[]
#	imaginary_row_list=[]
#	imaginary_column_list=[]
#	imaginary_placevalues=[]
#	imaginary_pvs_plus=""
#	imaginary_pvs_minus=""
#	imaginary_board=board
#	points_available=0
#	points_available_diag=0
#	coords=[]
#	stringsections=[]
#	#print(imaginary_board[6][5][0])
#	#print(expression1)
#	#print(expression2)
#	##print(expression_set)
#	#ai.expression1=re.compile('('+ai.upper_player+'('+ai.change_from+'+)'+ai.lower_player+')')
#	#ai.expression2=re.compile('('+ai.lower_player+'('+ai.change_from+'+)'+ai.upper_player+')')
#	cell_counter=0
#	colmn=search.column_search(current_cell, best_cell, imaginary_column_str, expression1, expression2)
#	for i in range(8):
#		#print("i = "+str(i))
#		column_count=0
#		imaginary_row_str=""
#		imaginary_column_str=""
#		for e in range(8):
#		   # print("e = "+str(e))
#			cell_counter+=1
#			imaginary_row_str+=imaginary_board[i][e][1]
#			#print("imaginary_row_str= "+imaginary_row_str)
#		imaginary_row_list=[]
#		for char in imaginary_row_str:
#			#print("char = "+ char)
#			imaginary_row_list.append(char)
#		#print("imaginary_row_list = "+str(imaginary_row_list))
#		#ensures string is empty
#		imaginary_row_str=""
#		#print("reset imaginary_row_str to: "+imaginary_row_str)
#		#ensures string is empty
#		imaginary_column_str=""
#		#print("reset imaginary_column_str to: "+imaginary_column_str)
#		for letters in imaginary_row_list:
#			#print("current letter: "+letters)
#			if letters==str(skip):
#				imaginary_row_list[column_count]=upper_player
#				#print(imaginary_row_list)
#				for char in imaginary_row_list:
#					imaginary_row_str+=char
#					#print("char in imaginary_row_list: "+char)
#				# shows current cell the board is focused on
#				#print("imaginary_row_str = "+imaginary_row_str)
#				#print("imaginary_column_list: "+str(imaginary_column_list))
#				for char in imaginary_column_list:
#					imaginary_column_str+=char
#					#print("char in imaginary_column_list: "+char)
					
#				#print(imaginary_board[6][5][0])
#				current_cell.append(imaginary_board[i][column_count][0])
#				#print("i at this point is: "+str(i))
#				#print("column_count at this point is: "+str(column_count))
#				#print("current cell: "+str(current_cell))
#				imaginary_pvs_plus="" 
#				imaginary_pvs_minus=""
#				for sequence in finditer(expression1, imaginary_row_str):
#					#print("sequence:"+str(sequence))
#					#print("imaginary_row_str: "+imaginary_row_str)
#					#potentiall remove 1 from the second integer in the sequence span, and add one to the first integer
#					imaginary_pvs_plus=sequence.span()
#					#print("imaginary_pvs_plus: "+str(imaginary_pvs_plus))
#				for sequence in finditer(expression2, imaginary_row_str):
#					#print("sequence: "+str(sequence))
#					#print("imaginary_row_str: "+imaginary_row_str)
#					imaginary_pvs_minus=sequence.span()
#					#print("imaginary_pvs_minus: "+str(imaginary_pvs_minus))
#				if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
				
#					#print("i found a potential move at "+str(current_cell[0])+"!")
#					try:
#						for things in imaginary_pvs_plus:
#							#print("things in imaginary_pvs_plus: "+str(things))
#							imaginary_placevalues.append(things)
#						#print("imaginary_placevalues: "+ str(imaginary_placevalues))
#					except IndexError:
#						print("cant find expression 1!")
#					try:
#						for stuff in imaginary_pvs_minus:               
#							#print("i in imaginary_pvs_minus: "+str(stuff))
#							imaginary_placevalues.append(stuff)
#							#print("imaginary_placevalues: "+str(imaginary_placevalues))
#					except IndexError:
#						print("cant find expression 2!")
#					finally:
#						points_available=((max(imaginary_placevalues)-min(imaginary_placevalues)-2)+colmn)
#						#print("points_available: "+str(points_available))
#					try:
#						#print("best_cell_row: "+str(best_cell_row))
#						if points_available> int(best_cell_row[0]):
#							for entrys in best_cell_row:
#								#print("Entry in Best_cell_row"+str(entrys))
#								del entrys
#							#print("best_cell_row before adding points available: "+str(best_cell_row))
#							best_cell_row.append(str(points_available))
#							#print("best_cell_row after adding points available: "+str(best_cell_row))
#							#print("column count: "+str(column_count))
#							best_cell_row.append(current_cell[0])
#							#print("best_cell_row: "+str(best_cell_row))
#							#print("imaginary_placevalues: "+str(imaginary_placevalues))
#							imaginary_placevalues=[]
#							#print("imaginary_row_str: "+imaginary_row_str)
#							imaginary_row_str=""
#						else:
#							imaginary_placevalues=[]
#							imaginary_row_str=""
#					except ArithmeticError:
#						imaginary_placevalues=[]
#						print(ArithmeticError)
#						#print("Arithmetic Error, can only use numbers")
#						#print(">imaginary_row_list["+str(column_count)+"] during check: "+imaginary_row_list[column_count])
#						imaginary_row_list[column_count]=str(skip)
#						#print(">imaginary_row_list["+str(column_count)+"] reverted back: "+imaginary_row_list[column_count])
#				else:
					
#					#print(">resetting imaginary_placevalues from:"+str(imaginary_placevalues))
#					imaginary_placevalues=[]
#					#print(">reset imaginary_placevalues to:"+str(imaginary_placevalues))
#				#ready for next cell
#				#print("<resetting imaginary_placevalues from:"+str(imaginary_placevalues))
#				imaginary_placevalues=[]
#				current_cell=[]
#				#print("best_cell_str: "+str(best_cell_row))
#				imaginary_row_str=""
#				#print("<imaginary_row_list["+str(column_count)+"] during check: "+imaginary_row_list[column_count])
#				imaginary_row_list[column_count]=str(skip)
#				#print("<imaginary_row_list["+str(column_count)+"] reverted back: "+imaginary_row_list[column_count])
#			else:
#				#print("column_count: "+str(column_count))
#				#print("i in range(8): "+str(i))
#				#index error on second run through
#				#print(str(imaginary_board[i][column_count][0][2:])+" not available!")
#				imaginary_placevalues=[]
#			column_count+=1
#			#print("column count:"+str(column_count))
#	#print("reset imaginary_column_str")
#	imaginary_column_str=""
#	#print("reset imaginary_row_list")
#	imaginary_row_list=[]
#	#print("reset imaginary_column_list")
#	imaginary_column_list=[]
#	#print("reset imaginary_placevalues")
#	imaginary_placevalues=[]
#	#print("reset points_available to 0")
#	#points_available_2=0
#	cell_counter=0
#	rw=search.row_search(current_cell, best_cell, imaginary_row_str, expression1, expression2)
#	for o in range(8):
#		row_count=0
#		imaginary_column_str=""
#		for c in range(8):
#			imaginary_column_str+=imaginary_board[c][o][1]
#		imaginary_column_list=[]
#		base_number=0
#		next_number=0
#		for char in imaginary_column_str:
#			imaginary_column_list.append(char)
#		imaginary_column_str=""
#		for letters in imaginary_column_list:
#			if letters==str(skip):
#				imaginary_column_list[row_count]=upper_player
#				for char in imaginary_column_list:
#					imaginary_column_str+=char
#				current_cell.append(imaginary_board[row_count][o][0])
#				imaginary_pvs_plus="" 
#				imaginary_pvs_minus=""
#				for sequence in finditer(expression1, imaginary_column_str):
#					imaginary_pvs_plus=sequence.span()
#				for sequence in finditer(expression2, imaginary_column_str):
#					imaginary_pvs_minus=sequence.span()
#				if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
#					try:
#						for particles in imaginary_pvs_plus:               
#							imaginary_placevalues.append(particles)
#					except IndexError:
#						None
#					try:
#						for matter in imaginary_pvs_minus:               
#							imaginary_placevalues.append(matter)
#					except IndexError:
#						None
#					finally:
#						points_available_2=((max(imaginary_placevalues)-min(imaginary_placevalues)-2)+rw)
#					try:
#						print("+++++++++++++++++++++++++++++++++"+str(best_cell_column))
#						if points_available_2> int(best_cell_column[0]):
#							#deletes any older moves
#							for entrys in best_cell_column:
#								del entrys
#							#error checking purposes
#							#adds the best move found in column to list
#							best_cell_column.append(str(points_available))
#							#error checking
#							best_cell_column.append(current_cell[0])
#							imaginary_placevalues=[]
#							imaginary_column_str=""
#						else:
#							imaginary_placevalues=[]
#							imaginary_column_str=""
#						#       print("check 52")
#						#   print("check 54")
#					except ArithmeticError:
#						#   print("check 55")
#						imaginary_placevalues=[]
#						print(ArithmeticError)
#						#print("Arithmetic Error, can only use numbers")
#						imaginary_column_list[row_count]=str(skip)
#						#  print("check 56")
#					#print("check 57")
#				else:
#					#print("check 58")
#					imaginary_placevalues=[]
#				#print("check 59")
#				imaginary_placevalues=[]
#				current_cell=[]
#				imaginary_column_str=""
#				imaginary_column_list[row_count]=str(skip)
#				#print("check 60")
#			else:
#				#print("check 61")
#				imaginary_placevalues=[]
#				#print("check 62")
#			print(best_cell_column)
#			row_count+=1
#			#print("row count:"+str(row_count))
	
#	dg=search.diaglr_search(current_cell, best_cell, imaginary_diaglr_str, expression1, expression2)
#	for c in range(8):
#		diag_rownum=c
#		imaginary_diaglr_str=""
#		imaginary_diaglr_list=[]
#		for k in range(8):
#			diagcol_count=0
#			x=1
#			imaginary_diaglr_str=""
#			diag_colnum=k
#			if diag_rownum > 7 - diag_colnum:
#				x+=7-diag_colnum
#			elif diag_rownum < 7 - diag_colnum:
#				x+=diag_rownum
#			elif diag_rownum == 7 - diag_colnum:
#				x+=7-diag_colnum
#			cellcoords=[k,c]
#			if imaginary_board[c][k][1]==str(skip):
#				imaginary_board[c][k][1]=upper_player
#				print(imaginary_board[c][k][0])
#				coords.append(cellcoords)
#				current_cell.append(imaginary_board[c][k][0])
#				try:
#					for aa in range(0, diag_colnum+1):
#						#print(diag_rownum+aa)
#						#print(diag_colnum-aa)
#						imaginary_diaglr_str+=(imaginary_board[diag_rownum+aa][diag_colnum-aa][1])
#					imaginary_diaglr_str=imaginary_diaglr_str[::-1]
#					stringsections.append(imaginary_diaglr_str)
#				except IndexError:
#					imaginary_diaglr_str=imaginary_diaglr_str[::-1]
#					stringsections.append(imaginary_diaglr_str)
#				imaginary_diaglr_str=""
#				try:
#					for a in range(1, x):
#						#print(diag_rownum-a)
#						#print(diag_colnum+a)
#						imaginary_diaglr_str+=(imaginary_board[diag_rownum-a][diag_colnum+a][1])
#					stringsections.append(imaginary_diaglr_str)
#				except IndexError:
#					#stringsections.append(imaginary_diaglr_str)
#					None
#				print(stringsections)
#				for sections in stringsections:
#					for sequence in finditer(expression1, sections):
#							imaginary_pvs_plus=sequence.span()
#					for sequence in finditer(expression2, sections):
#							imaginary_pvs_minus=sequence.span()
#					if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
#						try:
#							for ribbons in imaginary_pvs_plus:
#								imaginary_placevalues.append(ribbons)
#						except IndexError:
#							print(IndexError)
#							None
#						try:
#							#print(imaginary_pvs_minus)
#							for ribbons in imaginary_pvs_minus:
#								imaginary_placevalues.append(ribbons)
#						except IndexError:
#							print(IndexError)
#							None
#						finally:
#							#print(max(imaginary_placevalues))
#							#print(min(imaginary_placevalues))
#							points_available_diag=((max(imaginary_placevalues)-min(imaginary_placevalues)-2)+dg)
#							print(dg)
#						try:
#							print("points available diag: "+str(points_available_diag))
#							print(best_cell_diaglr)
#							if points_available_diag>int(best_cell_diaglr[0]):
#								for i in best_cell_diaglr:
#									#del i
#									best_cell_diaglr.remove(i)
#								#best_cell_diaglr=[0]
#								best_cell_diaglr.append(str(points_available_diag))
#								best_cell_diaglr.append(current_cell[0])
#								print(best_cell_diaglr)
#								imaginary_placevalues=[]
#								#print(stringsections)
#								#del best_cell_diaglr[0]
#								del stringsections[0]
#							else:
#								#print("++++++++++++++++++++++++++++++++++++++")
#								imaginary_placevalues=[]
#								#print(stringsections)
#								del stringsections[0]
#						except ArithmeticError:
#							imaginary_placevalues=[]
#							imaginary_board[c][k]=str(skip)
#					else:
#						imaginary_placevalues=[]
#					imaginary_placevalues=[]
#					current_cell=[]
#					stringsections=[]
#					imaginary_board[c][k][1]=str(skip)
				   
#			else:
#				pass
#			stringsections=[]
#			cell_counter+=1
#				#sect=""
#				#for letters in sections:
#				#	sect+=letters
#					#print(letters)
#				#print(letters)
#			#	if letters==str(skip):
#			#		imaginary_diaglr_list[diagcol_count]=upper_player
#			#		for char in imaginary_diaglr_list:
#			#			imaginary_diaglr_str+=char
#			#		current_cell.append(imaginary_board[int(coords[diag_colnum][0])][int(coords[diag_colnum][1])][0])
#			#		imaginary_pvs_plus="" 
#			#		imaginary_pvs_minus=""
#			#		for sequence in finditer(expression1, imaginary_diaglr_str):
#			#			imaginary_pvs_plus=sequence.span()
#			#		for sequence in finditer(expression2, imaginary_diaglr_str):
#			#			imaginary_pvs_minus=sequence.span()
#			#		if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
#			#			try:
#			#				for ribbons in imaginary_pvs_plus:               
#			#					imaginary_placevalues.append(ribbons)
#			#			except IndexError:
#			#				None
#			#			try:
#			#				for cloth in imaginary_pvs_minus:               
#			#					imaginary_placevalues.append(cloth)
#			#			except IndexError:
#			#				None
#			#			finally:
#			#				points_available_diag=((max(imaginary_placevalues)-min(imaginary_placevalues)-2)+dg)
#			#				print("diagonal points available: "+str(points_available_diag))
#			#			try:
#			#				if points_available_diag> int(best_cell_diaglr[0]):
#			#					#deletes any older moves
#			#					for entrys in best_cell_diaglr:
#			#						del entrys
#			#					#error checking purposes
#			#					#adds the best move found in column to list
#			#					best_cell_diaglr.append(str(points_available))
#			#					#error checking
#			#					best_cell_diaglr.append(current_cell[0])
#			#					imaginary_placevalues=[]
#			#					imaginary_diaglr_str=""
#			#				else:
#			#					imaginary_placevalues=[]
#			#					imaginary_diaglr_str=""
#			#			except ArithmeticError:
#			#				imaginary_placevalues=[]
#			#				imaginary_diaglr_list[diagcol_count]=str(skip)
#			#		else:
#			#			imaginary_placevalues=[]
#			#		imaginary_placevalues=[]
#			#		current_cell=[]
#			#		imaginary_diaglr_str=""
#			#		imaginary_diaglr_list[diagcol_count]=str(skip)
#			#	else:
#			#		imaginary_placevalues=[]
#			#diagcol_count+=1

#			#imaginary_diaglr_list=[]
#			#imaginary_diaglr_str=""
#			#cell_counter+=1
#	#count=0
#	#for c in range(8):
#	#	diag_rownum=c
#	#	imaginary_diaglr_str=""
#	#	imaginary_diaglr_list=[]
#	#	for k in range(8):
#	#		diagcol_count=0
#	#		x=1
#	#		imaginary_diaglr_str=""
#	#		diag_colnum=k
#	#		if diag_rownum > 7 - diag_colnum:
#	#			x+=7-diag_colnum
#	#		elif diag_rownum < 7 - diag_colnum:
#	#			x+=diag_rownum
#	#		elif diag_rownum == 7 - diag_colnum:
#	#			x+=7-diag_colnum
#	#		try:
#	#			for aa in range(0, diag_colnum+1):
#	#				temp_coord_list=[]
#	#				imaginary_diaglr_str+=(imaginary_board[diag_rownum+aa][diag_colnum-aa][1])
#	#				temp_coord_list.append(str((diag_rownum+aa)))
#	#				temp_coord_list.append(str((diag_rownum-aa)))
#	#				coords.insert(0,temp_coord_list)
#	#				temp_coord_list=[]
#	#			imaginary_diaglr_str=imaginary_diaglr_str[::-1]
#	#		except IndexError:
#	#			imaginary_diaglr_str=imaginary_diaglr_str[::-1]
#	#		try:
#	#			for a in range(1, x):
#	#				temp_coord_list=[]
#	#				imaginary_diaglr_str+=(imaginary_board[diag_rownum-a][diag_colnum+a][1])
#	#				temp_coord_list.append(str((diag_rownum-a)))
#	#				temp_coord_list.append(str((diag_rownum+a)))
#	#				coords.append(temp_coord_list)
#	#				temp_coord_list=[]
#	#		except IndexError:
#	#			None
#	#		for char in imaginary_diaglr_str:
#	#			imaginary_diaglr_list.append(char)
#	#		imaginary_diaglr_str=""
#	#		for letters in imaginary_diaglr_list:
#	#			if letters==str(skip):
#	#				imaginary_diaglr_list[diagcol_count]=upper_player
#	#				for char in imaginary_diaglr_list:
#	#					imaginary_diaglr_str+=char
#	#				current_cell.append(imaginary_board[int(coords[diag_colnum][0])][int(coords[diag_colnum][1])][0])
#	#				imaginary_pvs_plus="" 
#	#				imaginary_pvs_minus=""
#	#				for sequence in finditer(expression1, imaginary_diaglr_str):
#	#					imaginary_pvs_plus=sequence.span()
#	#				for sequence in finditer(expression2, imaginary_diaglr_str):
#	#					imaginary_pvs_minus=sequence.span()
#	#				if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
#	#					try:
#	#						for ribbons in imaginary_pvs_plus:               
#	#							imaginary_placevalues.append(ribbons)
#	#					except IndexError:
#	#						None
#	#					try:
#	#						for cloth in imaginary_pvs_minus:               
#	#							imaginary_placevalues.append(cloth)
#	#					except IndexError:
#	#						None
#	#					finally:
#	#						points_available_diag=((max(imaginary_placevalues)-min(imaginary_placevalues)-2)+dg)
#	#						print("diagonal points available: "+str(points_available_diag))
#	#					try:
#	#						if points_available_diag> int(best_cell_diaglr[0]):
#	#							#deletes any older moves
#	#							for entrys in best_cell_diaglr:
#	#								del entrys
#	#							#error checking purposes
#	#							#adds the best move found in column to list
#	#							best_cell_diaglr.append(str(points_available))
#	#							#error checking
#	#							best_cell_diaglr.append(current_cell[0])
#	#							imaginary_placevalues=[]
#	#							imaginary_diaglr_str=""
#	#						else:
#	#							imaginary_placevalues=[]
#	#							imaginary_diaglr_str=""
#	#					except ArithmeticError:
#	#						imaginary_placevalues=[]
#	#						imaginary_diaglr_list[diagcol_count]=str(skip)
#	#				else:
#	#					imaginary_placevalues=[]
#	#				imaginary_placevalues=[]
#	#				current_cell=[]
#	#				imaginary_diaglr_str=""
#	#				imaginary_diaglr_list[diagcol_count]=str(skip)
#	#			else:
#	#				imaginary_placevalues=[]
#	#		diagcol_count+=1

#	#		imaginary_diaglr_list=[]
#	#		imaginary_diaglr_str=""
#	#		cell_counter+=1
			
#	try:
#		while cell_counter==64: 
#			#del best_cell_diaglr[0]
#			del best_cell_row[0]
#			del best_cell_column[0]
#			#print("best_cell_row: "+str(best_cell_row))
#			#print("best_cell_column: "+str(best_cell_column))
#			print("\n"*10)
#			print("\nbest_cell_diaglr: "+str(best_cell_diaglr)+"\n\n\n\n\n\n\n\n")
#			best_cell.append(best_cell_diaglr)
#			best_cell.append(best_cell_row)
#			best_cell.append(best_cell_column)
#			return best_cell
#	except IndexError:
#		print("check 66")
#		cell_counter=0


#"""
			
#			###########
#			#################
#			###############
#			#########separate code
#						for i in imaginary_diaglr_list:

#							imaginary_diaglr_str+=i
#						for i in range(len(imaginary_diaglr_str)):
#							if imaginary_diaglr_str[i] == str(skip):
#								imaginary_diaglr_str[i]=upper_player
#								for sequence in finditer(expression1, imaginary_diaglr_str):
#									diag_pvs=sequence.span()
#									print("*")
#									print(diag_pvs)
#									print("*")
#								for sequence in finditer(expression2, imaginary_diaglr_str):
#									diag_pvs=sequence.span()
#									print("*")
#									print(diag_pvs)
#									print("*")
#							else:
#						#print(imaginary_diaglr_str)

#						#imaginary_diagrl_str=imaginary_diagrl_str[::-1]		
#						#imaginary_diagrl_str+=imaginary_diaglr_str
#						#print(imainary_diaglr_list)
#						print(imaginary_diaglr_str)
#						diag_pvs=""

#						imaginary_diaglr_str=""
#						imaginary_diaglr_list=[]
#						x=1
#"""





#"""
#	movesandcounter=[[0],[0],[0],[0],0]
#	for c in range(len(imaginary_board)):
#		for k in range(len(imaginary_board[c])):
#			if c > 7 - k:
#				x+=7-k
#			elif c < 7 - k:
#				x+=c
#			elif c == 7 - k:
#				x+=7-k
#			try:
#				for i in range(x):
#					imaginary_board[c+i][k-i]=imaginary_board[c+i][k-i]

#					print("i: "+str(i))
#					#imaginary_board[i-k][i+k]
#					print(imaginary_board[k-x][c+x])
#					print("movescounterbefore: "+str(movesandcounter[4]))
#					movesandcounter[4]+=1
#					print("movescounterafter: "+str(movesandcounter[4]))
#					#print(movesandcounter[4])
#			except IndexError:
#				print("urbefore: "+str(movesandcounter[1][0]))
#				movesandcounter[1][0]=movesandcounter[4]
#				print(movesandcounter[1][0])
#				movesandcounter[4]=0
#				print("blanked")
				
#			print(str(imaginary_board[c][k][0])+" "+str(movesandcounter[1][0])+" up right")
#			movesandcounter=[[0],[0],[0],[0],0]
	
#"""
#		""""