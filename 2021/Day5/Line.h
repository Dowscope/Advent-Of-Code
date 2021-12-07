#include <string>
#include <iostream>


class Line
{
private:
    int x1, x2, y1, y2;
public:
    Line(int x1, int y1, int x2, int y2);
    ~Line();
    int checkForTouch(Line &l);
    bool isOn(int x, int y);
    std::string toString();
};