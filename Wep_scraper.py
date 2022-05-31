#!/usr/bin/env python3"
import sys
import re


def main():
    

    ''' Command line error '''
    
    if(sys.stdin.isatty()):

        print("Error: no input file specified")

        exit(6)


    ''' Reading and storing data '''

    data = ""

    for line in sys.stdin:

        line = re.sub("\s+", " ", line)

        data += line
    
    data = re.sub(" +", " ", data)

    tables = re.findall(r'<table.*?>(.*?)</table.*?>', data, re.IGNORECASE) # Creates list of all tables
    
    n = 0


    ''' Iterating through the table(s) '''

    while(n < len(tables)):
        
        print("TABLE " + str(n + 1) + ":")

        rows = re.findall(r'<tr.*?>(.*?)</tr.*?>', str(tables[n]), re.IGNORECASE) # Creates list of all the rows

        max_cols = 0

        header_list = []


        ''' Finding the maximum column length '''

        for i in range(len(rows)):
            
            row = re.findall(r'<td.*?>(.*?)</td.*?>', str(rows[i]), re.IGNORECASE) # Creates list of cells
    
            header = re.findall(r'<th.*?>(.*?)</th.*?>', str(rows[i]), re.IGNORECASE) # Creates list of headers
       
            if(len(header) != 0):

                header_list.append(header)
            
            if(len(row) > max_cols):
    
                max_cols = len(row)

            if(len(header) > max_cols):
                
                max_cols = len(header)
    
        is_headers = False

        l = 0
        

        ''' Printing header(s) '''

        while(l < len(header_list)):
            
            is_headers = True
            
            k = 0

            while(k < len(header_list[l])):
                
                header = re.sub(" +", " ", str(header_list[l][k])) # Replacing multile spaces by single space
                
                header = re.sub("^ ", "", header) # Getting rid of leading space

                header = re.sub(" $", "", header) # Getting rid of trailing space

                if(re.match(".*?,.*?", header)):

                    sys.stderr.write("Error: Invalid format for csv file : '" + str(header) + "'\n")
                    
                    exit(6)

                if(k != max_cols - 1):

                    print(str(header) + ",", end = "")

                else:

                    print(header, end = "")
                    
                k += 1

            if(k > 0):

                is_headers = True
                
                while(k < max_cols - 1): # Print the rest of the commas

                    print(",", end = "")

                    k += 1

            print("")
            
            l += 1
        

        ''' Printing rows of cells '''

        for i in range(len(rows)):

            row = re.findall(r'<td.*?>(.*?)</td.*?>', str(rows[i]), re.IGNORECASE) # Creates list of cells
             
            i = 0

            while(i < len(row)):
                
                is_headers == False
                
                cell = re.sub(" +", " ", str(row[i])) # Replacing multile spaces by single space
             
                cell = re.sub("^ ", "", cell) # Getting rid of leading space
                
                cell = re.sub(" $", "", cell) # Getting rid of trailing space
                
                if(re.match(".*?,.*?", cell)):

                    sys.stderr.write("Error: Invalid format for csv file : '" + str(cell) + "'\n")

                    exit(6)

                if(i < max_cols - 1):
    
                    print(str(cell) + ",", end = "")

                else:
            
                    print(cell, end = "")

                i += 1

                if(i == len(row)):
                
                    while(i < max_cols - 1): # Print the rest of the commas
                    
                        print(",", end = "")

           
                        i += 1

            if(i != 0):

                print("")

            if(i == 0 and is_headers == False):

                sys.stderr.write("Error: empty row of data\n")

                while(i < max_cols - 1): # Printing commas for an empty row

                    print(",", end = "")

                    i += 1
                
                print("")

            is_header = False

        n += 1

        if(n != len(tables)):
            
            print("")


if __name__ == '__main__':
    main()


