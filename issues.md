- os dependent path names
	- folder_name = '\\Results_Iteration ' + str(wq_iteration_count)
	- No such file or directory: '/Users/jaykrishnang/Documents/Technion/civil/IITK-EPyT-C/epyt_c/Examples/Python\\epyt_c\\run_epyt_c.py'
	- One way: 
		import os
		mypath = os.path.join(os.path.curdir, 'folder_name')
		if not os.path.isdir(mypath):
			os.makedirs(mypath)'
- make code more readable
	- docstrings to explain a function, inputs and outputs
		- Examples: https://peps.python.org/pep-0257/
	- comments along the code body to give high-level idea of what code following the comment will do 
	- One operation per line. avoid using `;`
	- avoid using long lines
- If you can use PyCharm IDE it provides a code formatter which will restructure the code
- VSCode also has a formatter https://code.visualstudio.com/docs/python/formatting