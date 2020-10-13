# UART Hacking

A universal asynchronous receiver transmitter (UART) is a computer hardware standard for asynchronous serial communication in which data is encoded in a serial format and tramitted at configuratbale speed. The following tools are aimed at the hardware Security Tester and a written in Python 3.8 and make use of a the PYSerial and dbus modules. Information on hardware hacking and information security courses can be found at merimetso.net.
## Installation of pyserial module in Python 3.8
We can install the pyserial module using PIP
```sh
$ pip install pyserial
$ pip install dbus-python
```
Or we can install the modules using the Conda utility.
```sh
$ conda install pyserial
$ conda install dbus-python
```
We can then test that the module has been installed correctly by importing it in Python.
```sh
$ python
Python 3.8.3 (default, Jul  2 2020, 11:26:31)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information
>>> 
>>> import serial
>>>
>>> import dbus
>>>
```
## UART Hacking Tools in Python
The following are the tools that we can use when hacking a UART connection on a embedded system.
  - sbrute.py
  - miniterm.py
  - sscript.py
  - rfc2217_server.py
  - port_publisher.py
  - tcp_serial_redirect.py

## sbrute
This is login bruteforing tool for UART. Most UART connected are used to login to an embedded system. This tool is designed to allow a user to brute forece that authentication process. The program has been developed by Merimetso.
```sh
$ python sbrute.py -h
usage: sbrute.py [-h] [-d device] [-b baudrate] [-U username] [-f passwordfile]
                 [-v] [ -s loginsuccessstring] [-l usernameprompt]
                 [-P passwordprompt] [-t timeoutvalue]

 Optional Arguments:
    -h    Show this help message and exit.
    -d    This is the serial device to connect to. The default is:/dev/USB0
    -b    This is the baud rate to be used. The default is: 115200
    -f    This is the password file to be used. The default is: pass.txt
    -l    This is string that defines the username logon prompt.
              The default is 'Login:'
    -p    This is string that defines the login password prompt. The default
              is 'Password:'
    -s    This is string that defines a successful login. The default value:
              is 'admin@localhost$'
    -t    This is the timeout value for the serial connection. The default
              value is 1.
    -u    This is the username that is to be used for the brute forcing.
              The default value is: admin
    -v    This is verbose reporting. By default this is turned: OFF.

 Example Usage:
    $ sbrute.py -d /dev/ttyACM0 -b 115200 -u root -p default.txt -t 1
    or
    $ sbrute.py -d /dev/ttyACM0 -s 'root@beaglebone$' -u root
$
```
## miniterm
This is a simple terminal emulator. The user can select the device to connect to and baudrate of the communication.
```sh
$ python miniterm.py -h
usage: miniterm.py [-h] [--parity {N,E,O,S,M}] [--rtscts] [--xonxoff] [--rts RTS] 
                   [--dtr DTR] [--non-exclusive] [--ask] [-e][--encoding CODEC] [-f NAME] 
                   [--eol {CR,LF,CRLF}] [--raw] [--exit-char NUM] [--menu-char NUM] [-q] 
                   [--develop][port] [baudrate]

Miniterm - A simple terminal program for the serial port.

positional arguments:
  port                  serial port name ("-" to show port list)
  baudrate              set baud rate, default: 9600

optional arguments:
  -h, --help            show this help message and exit

port settings:
  --parity {N,E,O,S,M}  set parity, one of {N E O S M}, default: N
  --rtscts              enable RTS/CTS flow control (default off)
  --xonxoff             enable software flow control (default off)
  --rts RTS             set initial RTS line state (possible values: 0, 1)
  --dtr DTR             set initial DTR line state (possible values: 0, 1)
  --non-exclusive       disable locking for native ports
  --ask                 ask again for port when open fails

data handling:
  -e, --echo            enable local echo (default off)
  --encoding CODEC      set the encoding for the serial port (e.g. hexlify, Latin1, UTF-8), 
                            default: UTF-8
  -f NAME, --filter NAME
                        add text transformation
  --eol {CR,LF,CRLF}    end of line mode
  --raw                 Do no apply any encodings/transformations

hotkeys:
  --exit-char NUM       Unicode of special character that is used to exit the application, 
                            default: 29
  --menu-char NUM       Unicode code of special character that is used to control miniterm 
                            (menu), default: 20

diagnostics:
  -q, --quiet           suppress non-error messages
  --develop             show Python traceback on error
$
```
Further information on this tool can be located in the PYSerial module documemtation.  https://pyserial.readthedocs.io/en/latest/examples.html
## sscript
This is the UART script execution engine. Once you know a username and a password for a UART connection then you can start executing command on the embedded system. To do this you can use miniterm and enter the commands at the keyboard, or you can place them all in a file (like a batch job) and then get the contents of the file executed.

So if we look at the contents of batch.txt we can see a set of UNIX commands.
```sh
$ cat batch.txt
touch output.txt
ls -lisa >> output.txt
logoff
$
```
We can now get the contents of this file executed using the sscript.py tool.
```sh
$ python sscript.py -h
Program: sscript.py - Version: 1.0 - Author: ab@merimetso.net - Date: 2020/10/21

USAGE: sscript.py [-h] [-d device] [-b baudrate] [-U username] [-f commandfile]
                 [-v] [ -s loginsuccessstring] [-l usernameprompt]
                 [-p passwordprompt] [-t timeoutvalue] [-P password]

 Optional Arguments:
    -h    Show this help message and exit.
    -d    This is the serial device to connect to. The default is:/dev/USB0
    -b    This is the baud rate to be used. The default is: 115200
    -f    This is the command file to be used. The default is: command.txt
    -l    This is string that defines the username logon prompt.
              The default is 'Login:'
    -p    This is string that defines the login password prompt. The default
              is 'Password:'
    -P    This is the password to login. The default is: letmein
    -s    This is string that defines a successful login. The default value:
              is 'admin@localhost$'
    -t    This is the timeout value for the serial connection. The default
              value is 1.
    -U    This is the username that is to be used for the brute forcing.
              The default value is: admin
    -v    This is verbose reporting. By default this is turned: OFF.

 Example Usage:
    $ sscript.py -d /dev/ttyACM0 -b 115200 -U root -P Admin123 -f batch.txt
$
```
## rfc2217_server
Simple cross platform RFC 2217 serial port server. It uses threads and is portable (runs on POSIX, Windows, etc).

```sh
$ python rfc2217_server.py -h
usage: rfc2217_server.py [-h] [-p TCPPORT] [-v] SERIALPORT

RFC 2217 Serial to Network (TCP/IP) redirector.

positional arguments:
  SERIALPORT

optional arguments:
  -h, --help            show this help message and exit
  -p TCPPORT, --localport TCPPORT
                        local TCP port, default: 2217
  -v, --verbose         print more diagnostic messages (option can be given multiple times)
$
```
Further information on this tool can be located in the PYSerial module documemtation.  https://pyserial.readthedocs.io/en/latest/examples.html
## port_publisher
This example implements a TCP/IP to serial port service that works with multiple ports at once. It uses select, no threads, for the serial ports and the network sockets and therefore runs on POSIX systems only. 
```sh
$ python port_publisher.py -h
usage: port_publisher.py [options]

Announce the existence of devices using zeroconf and provide
a TCP/IP <-> serial port gateway (implements RFC 2217).

If running as daemon, write to syslog. Otherwise write to stdout.

optional arguments:
  -h, --help            show this help message and exit

serial port settings:
  --ports-regex REGEX   specify a regex to search against the serial devices
                        and their descriptions (default: /dev/ttyUSB[0-9]+)

network settings:
  --tcp-port PORT       specify lowest TCP port number (default: 7000)

daemon:
  -d, --daemon          start as daemon
  --pidfile FILE        specify a name for the PID file

diagnostics:
  -o FILE, --logfile FILE
                        write messages file instead of stdout
  -q, --quiet           suppress most diagnostic messages
  -v, --verbose         increase diagnostic messages
$
```
Further information on this tool can be located in the PYSerial module documemtation.  https://pyserial.readthedocs.io/en/latest/examples.html
## tcp_serial_redirect
This program opens a TCP/IP port. When a connection is made to that port (e.g. with telnet) it forwards all data to the serial port and vice versa. This program only exports a raw socket connection.
```sh
$ python -h tcp_serial_redirect.py
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : dont write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser; also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the users environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-q     : dont print version and copyright messages on interactive startup
-s     : dont add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : dont imply 'import site' on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
$
```
Further information on this tool can be located in the PYSerial module documemtation.  https://pyserial.readthedocs.io/en/latest/examples.html
## License
  - MIT
