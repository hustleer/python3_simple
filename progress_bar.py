def progress(current, total, barlength=65):
    percent = (current/total)*100
    hastrik = '#' * int(percent/100 * barlength)
    dash = '-' * int( barlength - len(hastrik) )
    print(str([hastrik + dash]) + str(current) + '  ' + str(int(percent)) + '%',end='\r')

    
