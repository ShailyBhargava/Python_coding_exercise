def count_substring(string, sub_string): 
     count=0
     for i in range(len(string)-len(sub_string)+1):
            if string[i:i+len(sub_string)] == sub_string:
                count +=1
     return count
    
   

if __name__ == '__main__':
    string = input()
    sub_string = input()
    
    count = count_substring(string, sub_string)
    print(count)