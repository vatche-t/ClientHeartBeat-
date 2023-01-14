from filehandler import FileModified


def file_modifed():
    print("modified")
    return False

filehandler = FileModified(r"app/client.log",file_modifed)

filehandler.start()
