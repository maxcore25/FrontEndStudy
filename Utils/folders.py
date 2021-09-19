import os

ACCESS_RIGHTS = 0o755

def createFolders(n, base):
    for i in range(1, n):
        path = f'{os.getcwd()}/{base}/Practice{i}'
        try:
            os.mkdir(path, ACCESS_RIGHTS)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)

if __name__ == '__main__':
    createFolders(16, 'Docs/Images')