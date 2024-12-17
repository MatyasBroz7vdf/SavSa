import psutil
import re
import os

def filter(par, l, port=None):
    if port == None:
        pass
    else:
        h = par
        par = port
    d = {}
    match par:
        case "udp":
            for g in l:
                if l[g]["Type"] == "UDP":
                    d[g] = l[g]
            return d

        case "tcp":
            for g in l:
                if l[g]["Type"] == "TCP":
                    d[g] = l[g]
            return d

        case "ipv4":
            for g in l:
                if l[g]["Communication_protocol"] == "IPV4":
                    d[g] = l[g]
            return d

        case "ipv6":
            for g in l:
                if l[g]["Communication_protocol"] == "IPV6":
                    d[g] = l[g]
            return d

        case "est":
            for g in l:
                if l[g]["Status"] == "ESTABLISHED":
                    d[g] = l[g]
            return d

        case "lis":
            for g in l:
                if l[g]["Status"] == "LISTEN":
                    d[g] = l[g]
            return d

        case "clo_wa":
            for g in l:
                if l[g]["Status"] == "CLOSE_WAIT":
                    d[g] = l[g]
            return d


        case "port":
            for g in l:
                if int(l[g]["Port"]) == int(h):
                    d[g] = l[g]
            return d

        case "address": #address_logic
            for g in l:
                if str(l[g]["Address"]) == str(h):
                    d[g] = l[g]
            return d



def list_connections():
    a = psutil.net_connections('tcp')
    f = {}
    for z in a:
        y = []
        for i in z:
            y.append(i)
        if y[1] == 2:
            y[1] = "TCP"
        else:
            y[1] = "UDP"

        if y[3][0] == "::":
            y[2] = "IPV6"
        
        elif len(y[3][0]) <16 and ":" not in y:
            y[2] = "IPV4"
        
        else:
            y[2] = "IPV6"

        f[y[0]] = {
            "Type": y[1],
            "Communication_protocol": y[2], #PŘEDĚLAT
            "Address": y[3][0], 
            "Port": y[3][1], 
            "Status": y[5], 
            "Pid:": y[6]
        }
    return f

if __name__ == "__main__":
    a = list_connections()
    print("UDP/TCP/IPV4/IPV6/#SPECIFIC_ADRESS/#SPECIFIC_PORT/ESTABLISHED/LISTEN/CLOSE_WAIT/None")
    o = input("udp/tcp/ipv4/ipv6/address=/port=/est/lis/clo_wa/none\n")
    while True:

        if o == "none":
            break
        elif o == "udp" or o == "tcp" or o == "ipv4" or o == "ipv6" or o == "est" or o == "lis" or o == "clo_wa":
            a = filter(o, a)
            break
        
        else:
            i = o.replace("address=", "")
            if i == o:
                pass
            else:
                a = filter(i, a, port="address")
                break

            i = o.replace("port=", "")
            if i == o:
                pass
            else:
                a = filter(i, a, port="port")
                break

        print("invalid")
        os.exit()

    for i in a:
        print(a[i])


"""                for g in l:
                if l[g]["Status"] == "LISTEN":
                    d[g] = l[g]
            return d"""

"""                print(l[g])
                print(l[g].keys())
                print(l[g]["Port"])"""
