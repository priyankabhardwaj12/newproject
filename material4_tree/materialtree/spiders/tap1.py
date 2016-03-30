file_read = open ("matl.text", "r")
file_write = open ("maew1.txt", "w")

for line in file_read :

	line = line.replace ("\n", "")
	updated_line = "'"+line+"',"
	#updated_line = line
	file_write.write (updated_line)
	file_write.write ("\n")

file_read.close ()
file_write.close ()