import PySimpleGUI as sg
import ast
import operator

sg.theme('Dark')
sg.set_options(font = 'Franklin 14', button_element_size = (6,3))
button_size = (6,3)
layout = [
			[sg.Text('Result', font = 'Franklin 25', justification = 'right', expand_x = True, pad = (10,30), key = '-TEXT-')],
			[sg.Button('C',expand_x = True),sg.Button('/', size = button_size)],
			[sg.Button(7, size = button_size),sg.Button(8, size = button_size),sg.Button(9, size = button_size),sg.Button('*', size = button_size)],
			[sg.Button(4, size = button_size),sg.Button(5, size = button_size),sg.Button(6, size = button_size),sg.Button('-',size = button_size)],
			[sg.Button(1, size = button_size),sg.Button(2, size = button_size),sg.Button(3,size = button_size),sg.Button('+', size = button_size)],
			[sg.Button(0, expand_x = True),sg.Button('.', size = button_size),sg.Button('=', size = button_size)],
		 ]
		 

win = sg.Window('Calculator-dEfy',layout)

current_num = []
full_operation = []

while True:
	event,values = win.read()
	if event == sg.WIN_CLOSED:
		break

	if event in ['0','1','2','3','4','5','6','7','8','9','.']:
		current_num.append(event)
		num_strg = ''.join(current_num)
		win['-TEXT-'].update(num_strg)

	if event in ['*','/','-','+']:
		full_operation.append(''.join(current_num))
		current_num = []
		full_operation.append(event)
		win['-TEXT-'].update(event)

	if event == '=':
		full_operation.append(''.join(current_num))
		expr = ' '.join(full_operation)
		ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
		nums = expr.split()
		result = ast.literal_eval(nums[0])
		for i in range(1, len(nums), 2):
			op = ops[nums[i]]
			result = op(result, ast.literal_eval(nums[i + 1]))
		win['-TEXT-'].update(result)
		full_operation = []


	if event == 'C':
		current_num = []
		full_operation = []
		win['-TEXT-'].update('')


win.close()