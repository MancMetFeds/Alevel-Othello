from re import *
def column_search (current_cell, best_cell, imaginary_column_str,expression1, expression2):
    imaginary_placevalues=[]
    imaginary_pvs_plus=""
    imaginary_pvs_minus=""
    imaginary_column_str=""
    points_available=0
    for sequence in finditer(expression1, imaginary_column_str):
                    #print("check 01")
                    #print(imaginary_column_str)
                    imaginary_pvs_plus=sequence.span()
                    #print(imaginary_pvs_plus)
    for sequence in finditer(expression2, imaginary_column_str):
                    #print("check 02")
                    #print(imaginary_column_str)
                    imaginary_pvs_minus=sequence.span()
                    #print(imaginary_pvs_minus)
    if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
                    points_available=(max(imaginary_placevalues)-min(imaginary_placevalues)-2)
                    return points_available
    else:
                    return 0

                        
                        
def row_search (current_cell, best_cell, imaginary_row_str,expression1, expression2):
    imaginary_placevalues=[]
    imaginary_pvs_plus=""
    imaginary_pvs_minus=""
    imaginary_row_str=""
    points_available=0
    for sequence in finditer(expression1, imaginary_row_str):
                    #print("check 01")
                    #print(imaginary_row_str)
                    imaginary_pvs_plus=sequence.span()
                    #print(imaginary_pvs_plus)
    for sequence in finditer(expression2, imaginary_row_str):
                    #print("check 02")
                    #print(imaginary_row_str)
                    imaginary_pvs_minus=sequence.span()
                    #print(imaginary_pvs_minus)
    if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
                    points_available_2=(max(imaginary_placevalues)-min(imaginary_placevalues)-2)
                    return points_available_2
    else:
                    return 0


def diaglr_search (current_cell, best_cell, imaginary_diaglr_str,expression1, expression2):
    imaginary_placevalues=[]
    imaginary_pvs_plus=""
    imaginary_pvs_minus=""
    imaginary_diaglr_str=""
    points_available=0
    for sequence in finditer(expression1, imaginary_diaglr_str):
                    imaginary_pvs_plus=sequence.span()
    for sequence in finditer(expression2, imaginary_diaglr_str):
                    imaginary_pvs_minus=sequence.span()
    if len(imaginary_pvs_plus)>0 or len(imaginary_pvs_minus)>0:
                    points_available_diag=(max(imaginary_placevalues)-min(imaginary_placevalues)-2)
                    return points_available_diag
    else:
                    return 0