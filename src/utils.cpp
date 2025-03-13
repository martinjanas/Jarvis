#include "utils.h"


namespace utils
{
    void run_script(const char* script)
    {
        std::string format = std::format("scripts/{}", script);
    
        FILE* file = nullptr;   
        fopen_s(&file, format.c_str(), "r");
        if (!file)
            return;
    
        PyRun_SimpleFile(file, format.c_str());
        fclose(file);
    }
}