
# coding: utf-8

# In[ ]:


#6001012630047
#Tummanoon Kitcharas-anan
#For more information ==> http://myblogmysoftware.blogspot.com/

import PySimpleGUI as sg
# create gui
layout = [[sg.Input(size=(31, 2), do_not_clear=True, justification='right', key='input')],
          [sg.ReadFormButton('('), sg.ReadFormButton(')'), sg.ReadFormButton('CE'), sg.ReadFormButton('Delete')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('/')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('*')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')],
          ]

form = sg.FlexForm('Calculator', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=True)
# display caption, buttons size and enable to grab anywhere

form.Layout(layout)

keys_entered = ''  # for input

#---------------------------------------------
#loop while

while True:
    button, values = form.Read()  
    if button is None:  
        break
    if button is 'CE':                   # clear all the numbers and opearation
        keys_entered = ''      
    elif button is 'Delete':             # delete the last number or opearation
        if keys_entered != '':
            keys_entered = keys_entered[:-1]
    elif button in '1234567890().':      # numbers, bracket, point
        keys_entered = values['input']  
        keys_entered += button  
    elif button in '+-*/':               # operation
        if keys_entered[-1:] == '+' or keys_entered[-1:] == '-' or keys_entered[-1:] == '*' or keys_entered[-1:] == '/':
            keys_entered = keys_entered[:-1]
            keys_entered += button        # make double operation to not possible
        elif keys_entered == '':
            if button not in '+*/':
                keys_entered = values['input']
                keys_entered += button     # cannot use + or * or / operation as a first input
        else:
            keys_entered = values['input']
            keys_entered += button
    elif button in '=':                  # SUM
        if '/0' in keys_entered:
            keys_entered = 'ERROR by division zero'
        elif ('(' in keys_entered and ')' not in keys_entered) or (')' in keys_entered and '(' not in keys_entered):
            keys_entered = 'ERROR by not completed bracket'
        elif '..' in keys_entered:
            keys_entered = 'ERROR by points'
        else :
            keys_entered = str(eval(keys_entered))
    form.FindElement('input').Update(keys_entered)

"""
Examples

19-6 = 13
8/5 = 1.6
1.5*3 = 4.5
0/4 = 0.0
12/0 = ERROR by division zero
(5-1 = ERROR by not completed bracket
9/3) = ERROR by not completed bracket
1..5*2 = ERROR by points
5+3*2 = 11
(5+3)*2 = 16


"""

