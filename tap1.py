file_read = open ("s1.text", "r")
file_write = open ("snew1.txt", "w")

for line in file_read :

	line = line.replace ("\n", "")
	updated_line = "'"+line+"',"
	#updated_line = line
	file_write.write (updated_line)
	file_write.write ("\n")

file_read.close ()
file_write.close ()