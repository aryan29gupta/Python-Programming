a=input("File Name  ")
L=a.split(".")
if len(L)!=2:
    print("application/octet-stream")
else:
    if L[1]=="pdf":
        print("application/pdf")
    elif L[1]=="jpg" or L[1]=="jpeg":
        print("image/jpeg")
    elif L[1]=="png":
        print("image/png")
    elif L[1]=="gif":
        print("image/gif")
    elif L[1]=="txt":
        print("text/plain")
    elif L[1]=="zip":
        print("application/zip")
    else:
        print("no such extension exists")
