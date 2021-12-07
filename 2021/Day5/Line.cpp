#include "Line.h"

Line::Line(int ax1, int ay1, int ax2, int ay2)
{
    this->x1=ax1;this->x2=ax2;this->y2=ay2;this->y2=ay2;
}
Line::~Line()
{
}
std::string Line::toString(){
    std::string startx = std::to_string(x1);
    std::string starty = std::to_string(y1);
    std::string endx = std::to_string(x2);
    std::string endy = std::to_string(y2);
    std::string s = startx + "," + starty + " -> " + endx + "," + endy;
    std::cout << this->x1 << std::endl;
    return "";
}
int Line::checkForTouch(Line &l){
    int touches = 0;
    for (int y = y1; y <= y2; y++){
        for (int x = x1; x <= x2; x++){
            if (l.isOn(x, y)){
                touches++;
            }
        }
    }
    
    return touches;
}
bool Line::isOn(int ax, int ay){
    for (int y = y1; y <= y2; y++){
        for (int x = x1; x <= x2; x++){
            if(x == ax && y == ay){
                return true;
            }
        }
    }
    return false;
}