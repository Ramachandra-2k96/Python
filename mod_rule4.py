def rule4(s1,timeout):
    import datetime as dt
    timeout=timeout
    today1=dt.datetime.now()
    input1=input(s1+str(timeout)+": ")
    today2=dt.datetime.now()
    diff1=(today2-today1).seconds
    return(diff1,input1)