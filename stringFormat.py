#coding:utf-8
# 2016 8.4 author:windgodvc

import sys

def readFile(file):
    return open(file, 'r').read();

def saveFile(file,content):
    file = open(file,'w')
    file.write(content)

def help():
    print "请把要转换的 内容放入content.txt 中 转换成功后 会输出文件 result.txt."
    print "Please enter content to content.text file. foramt result content will output to  result.txt file."
    print "Command"
    print "\t\tformat"
    print "\t\trestore"

class StringFormat:

    def escapeString(self,content):
        result = ""
        for itor in content:
            if itor == '\"':
                result += "\\\"";
            elif itor == '\'':
                result += "\\\'";
            elif itor == '\\':
                result += "\\\\";
            elif itor == '\t':
                result += "\\t";
            elif itor == '\n':
                result += "\\n";
            elif itor == '\r':
                result += "\\r";
            elif itor == '\b':
                result += "\\b";
            elif itor == '\f':
                result += "\\f";
            else :
                result += itor;
        return result;


        ######
    def unescapeString(self,content):
        result = ""
        length = len(content)
        itor = "";
        i = 0;
        result += content[0];
        while i < range(length):
            i+=1;
            if i >= length:
                break;            
            itor = content[i]
            if itor == '\\':
                i+= 1;
                if i >= length:
                    break;
                itor = content[i];
                if itor == '\"':
                    result += "\"";
                elif itor == '\'':
                    result += "\'";
                elif itor == '\\':
                    result += "\\";
                elif itor == 't':
                    result += "\t";
                elif itor == 'n':
                    result += "\n";
                elif itor == 'r':
                    result += "\r";
                elif itor == 'b':
                    result += "\b";
                elif itor == 'f':
                    result += "\f";
                else :
                    result += itor;
            else :
                result += itor;
        return result;

                
                



def main():
    if len(sys.argv) == 1:
        help();
        return ;
    elif  sys.argv[1] == "--help":
        help();
    elif sys.argv[1] == "format":

        string = StringFormat();
        filecontent = readFile(sys.path[0] + "/content.txt");
        result = string.escapeString(filecontent)
        saveFile(sys.path[0] + "/result.txt",result)
        print "succeed!"
    elif sys.argv[1] == "restore":

        string = StringFormat();
        filecontent = readFile(sys.path[0] + "/content.txt");
        result = string.unescapeString(filecontent)
        saveFile(sys.path[0] + "/result.txt",result)
        print "succeed!"
    else :
        help();

main();