import os 

class Ccwc:
    def count_bytes(self, file_name):
        file_stats = os.stat(file_name)
        return file_stats.st_size

    def count_lines(self, file_name):
        with open(file_name, "r") as fp:
            for count, line in enumerate(fp):
                pass 
            fp.close()
        return count + 1
    
    def count_words(self, file_name):
        words = 0
        with open(file_name, "r") as fp:
            data = fp.read()
            word_per_line = data.split()
            words += len(word_per_line)
            fp.close()
        return words

    def count_characters(self, file_name):
        file_name = "test.txt"
        char_ctr = 0
        with open(file_name, "r") as fp:
            for line in fp:
                char_ctr += sum(1 for c in line) + 1
            fp.close()
        return char_ctr
    
    def display_results(self, ccwc_input, command_type="default"):
        if command_type == "cat":
            read_filename = ccwc_input[1] if len(ccwc_input) > 3 else False
            read_command = ccwc_input[3] if len(ccwc_input) > 3 else False 
            read_parameter = ccwc_input[4] if len(ccwc_input) > 4 else False
        else:
            read_command = ccwc_input[0] if len(ccwc_input) > 0 else False
            read_parameter = ccwc_input[1] if len(ccwc_input) > 2 else False
            if len(ccwc_input) > 2:
                read_filename = ccwc_input[2]
            elif len(ccwc_input) > 1:
                read_filename = ccwc_input[1]
            else:
                read_filename = False 
    
        if not read_command:
            print("No valid command has been passed.")
        elif read_command != "ccwc":
            print("Incorrect command format received.")
            read_command = False
    
        if not read_filename:
            print("No file atached.")
        if not os.path.exists(read_filename):
            print("Invalid File")
            read_filename = False

        if read_command and read_filename:
            if not read_parameter:
                byte_ctr = self.count_bytes(read_filename)
                line_ctr = self.count_lines(read_filename)
                word_ctr = self.count_words(read_filename)
                print(" ", line_ctr, word_ctr, byte_ctr, read_filename)
            else:
                if read_parameter == "-c":
                    byte_ctr = self.count_bytes(read_filename)
                    print(byte_ctr, read_filename)
                elif read_parameter == "-l":
                    line_ctr = self.count_lines(read_filename)
                    print(line_ctr, read_filename)
                elif read_parameter == "-w":
                    word_ctr = self.count_words(read_filename) 
                    print(word_ctr, read_filename)
                elif read_parameter == "-m":
                    char_ctr = self.count_characters(read_filename)
                    print(char_ctr, read_filename)
                else:
                    print("You have passed an invalid parameter.")

if __name__ == "__main__":
    while True:
        ccwc_input = input().split()
        if ccwc_input[0] == "exit":
            break
        else:
            cc = Ccwc()
            if ccwc_input[0] == "cat":
                cc.display_results(ccwc_input, "cat")
            else:
                cc.display_results(ccwc_input)

    


    
    

    
    
