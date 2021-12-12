#include <iostream>
#include <fstream>
#include <string>
#include <vector>

static void Log(const std::string s){
    std::cout << s << std::endl;
}

void readFile(std::vector<std::string> &array){
    std::string s;
    std::fstream file;
    file.open("sample.txt", std::ios::in);
    if (file.is_open()){
        while(getline(file, s)){
            array.push_back(s);
        }
    }
}

void printVector(std::vector<std::string> &arr){
    for(auto a : arr){
        Log(a);
    }
}

void sortFile(std::vector<std::string> &arrIn, std::vector<std::string> &arrOut){
    for (auto a : arrIn){
        
    }
}

int main(int argc, char* argsv[]){
    std::vector<std::string> inputText;
    readFile(inputText);

    std::vector<std::string> nums;


    std::cout << inputText.size() << std::endl;
    return 0;
}