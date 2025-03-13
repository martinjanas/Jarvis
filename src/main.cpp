#include <iostream>
#include <Windows.h>
#include "utils.h"

int main()
{
    Py_Initialize();

    utils::run_script("speech.py");
    
    Py_Finalize();
    
    return 0;
}
