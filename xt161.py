from sys import argv

script,filename = argv

txt = open(filename)

print(f"We're able to open the file: {filename}")
print(txt.read())

txt.close()