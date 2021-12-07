#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "Line.h"

void readFile(std::string filename, std::vector<std::string> &inputs){
    std::fstream newFile;
    newFile.open(filename, std::ios::in);
    std::vector<std::string> inputText;
    if (newFile.is_open()){
        std::string s;
        while(getline(newFile, s)){
            inputText.push_back(s);
        }
        newFile.close();
    }
    inputs = inputText;
}

void printArray(const std::vector<std::string> &array){
    for (auto line: array){
        std::cout << line << std::endl;
    }
}
void printArray(const std::vector<Line> &array){
    for (auto line: array){
        std::cout << line.toString() << std::endl;
    }
}

void createLine(const std::vector<std::string> &inputs, std::vector<Line> &lines){
    for (auto line : inputs){
        std::string startPoint, endPoint;
        startPoint = line.substr(0,3);
        endPoint = line.substr(7);

        lines.push_back(Line(startPoint[0], startPoint[2], endPoint[0], endPoint[2]));
    }
}
int checkTouches(std::vector<Line> &lines){
    int touches = 0;
    for (auto line : lines){
        Line l = lines.back();
        lines.pop_back();
        for (auto lineToCheck : lines){
            touches += l.checkForTouch(lineToCheck);
        }
    }
    return touches;
}
int main(int argc, char* argv[]){
    std::vector<std::string> inputs;
    readFile("sample.txt", inputs);

    std::vector<Line> lines;
    createLine(inputs, lines);

    printArray(lines);
    std::cout << checkTouches(lines) << std::endl;
    return 0;
}