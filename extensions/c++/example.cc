#include"example.h"
#include<iostream>

base::base(int a) {
    std::cout<< "Base class constructor " << std::endl;
    this->a = a;
}

void base::set_a (int a) {

    this->a = a;
}


int base::get_a (){

   return a;
}

void base::display() {
    std::cout<< "Output : " << a << std::endl;
}

base::~base() {
    std::cout<< "Base class destructor" <<std::endl;

}


