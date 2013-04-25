# -*- coding: utf-8 -*-

def delblankline(infile, outfile):

    """ Delete blanklines of infile """
    infp = open(infile, "r")
    outfp = open(outfile, "w")
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()

if __name__ == "__main__":
    delblankline("readme.txt.bak","readme.txt")
