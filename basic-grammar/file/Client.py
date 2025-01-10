import readfile
import writefile

# writefile.write_file_append("./temp.txt","12345678\n","87654321\n")


readfile.read_file_as_json("./person.json")


writefile.write_file_as_json("./person.json","levi")