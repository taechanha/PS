char * defangIPaddr(char * address){
    char* p = (char*)malloc(sizeof(address) * 26);
    int i = 0;
    int j = 0;
    
    while(address[i] != '\0'){
        if(address[i] == '.'){
            p[j] = '[';
            p[j+1] = '.';
            p[j+2] = ']';
            
            j += 3;
        }
        else{
            p[j] = address[i];
            j++;
        }
        i++;
    }
    p[j] = '\0';
    return p;
}

