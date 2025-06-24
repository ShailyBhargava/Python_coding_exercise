import textwrap
def wraptext(string,max_width):
    return "\n".join(textwrap.wrap(string,max_width))
if __name__=="__main__":
    string ,max_width = input(),int(input())
    result = wraptext(string,max_width)
    print(result)