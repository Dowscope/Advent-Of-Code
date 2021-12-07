#include "Line.h"

Line::Line(int x1, int y1, int x2, int y2):
    x1(x1), x2(x2), y1(y1), y2(y2)
{
}
Line::~Line()
{
}
std::string Line::toString(){
    std::string s = x1 + ", " + y1;
    return s;
}