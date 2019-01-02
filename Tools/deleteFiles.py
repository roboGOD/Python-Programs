import os

path = raw_input("Please enter the path to directory: ")

try:
	f_name = raw_input("Please enter file name: ")
	if f_name[-1] != '*' and f_name[0] != '*':
		os.chdir(path)
		os.remove(f_name)

	else:
		print "Please select mode."
		print "0 : Delete from current directory only."
		print "1 : Delete from all subdirectories also."
		mode = raw_input("Option: ")
		
		if mode == "0":
			os.chdir(path)
			if f_name[0] == '*':
				pattern = f_name[1:]
				l = len(pattern)
				files = [f for f in os.listdir('.') if os.path.isfile(f)]		
				for f_name in files:
					if len(f_name) >= l:
						if f_name[-l:] == pattern:
							os.remove(f_name)
			
			elif f_name[-1] == '*':
				l = len(f_name)-1
				pattern = f_name[:l]
				files = [f for f in os.listdir('.') if os.path.isfile(f)]
				for f_name in files:
					if len(f_name) >= l:
						if f_name[:l] == pattern:
							os.remove(f_name)

		elif mode == "1":
			if f_name[0] == '*':
				pattern = f_name[1:]
				l = len(pattern)		
				for root, dirs, files in os.walk(path):
					for f_name in files:
						if len(f_name) >= l:
							if f_name[-l:] == pattern:
								os.remove(os.path.join(root, f_name))

			elif f_name[-1] == '*':
				l = len(f_name)-1
				pattern = f_name[:l]		
				for root, dirs, files in os.walk(path):
					for f_name in files:
						if len(f_name) >= l:
							if f_name[:l] == pattern:
								os.remove(os.path.join(root, f_name))
	
	print "File(s) removed!"
except Exception:
	print "Error!"
