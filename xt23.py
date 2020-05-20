import sys
script,encoding,error = sys.argv

#解码字节(有原始字节必须用.decode()获取字符串)，编码字符串(有字符串必须用.encode()获取字节)
def main(language_file,encoding,errors):
    line = language_file.readline()

    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)


def print_line(line,encoding,errors):
    next_lang = line.strip()   #strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    raw_bytes = next_lang.encode(encoding,errors = errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes,"<===>",cooked_string)


languages = open("languages.txt",encoding="utf-8")

main(languages,encoding,error)