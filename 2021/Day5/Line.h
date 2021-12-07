#include <string>

class Line
{
private:
    int x1, x2, y1, y2;
public:
    Line(int x1, int y1, int x2, int y2);
    ~Line();
    std::string toString();
};