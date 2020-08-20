# run it with the comman 'python working_with_files.py'
# in first running the expected output is: file 'some-file.txt' doesn't exists
# in the second runing the expected output is 10 lines with the prefix 'This is line' 

def create_file():
    f= open("some-file.txt","w+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()

def main():
    try:
        exmp_file = open('some-file.txt', 'r')
        lines = exmp_file.readlines()
    except FileNotFoundError:
        print("file 'some-file.txt' doesn't exists")
        create_file()
    else:
        for line in lines:
            print(line)
        exmp_file.close()

if __name__ == '__main__':
    main()

