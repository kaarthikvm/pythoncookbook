#include<iostream>
#include"example.h"

int main(){

    base b1 = base(100);
    b1.display();
    b1.set_a(333);
    std::cout << b1.get_a() << std::endl;
    b1.display();
return 0;
}



