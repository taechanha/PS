char* freqAlphabets(char* s){
    char* out = (char*)malloc(strlen(s)+1);
    int i = 0;
    
    while(*s != '\0'){
        
        if(*(s+1) != '\0' && *(s+2) == '#'){
            if(*s == '2')
                *(out+i) = (char)(*s + *(s+1) + 18);
            else
                *(out+i) = (char)(*s + *(s+1) + 9);
            if(*(s+3) == '\0'){
                *(out+i+1) = '\0';
                return out;
            }
                s += 3;
                i++;
        }
        else{
            *(out+i) = (char)(*s + 48);
            if(*(s+1) == '\0'){
                *(out+i+1) = '\0';
                return out;
            }
            if(*s != '\0'){
                s++;
                i++;
            }
        }
    }
    return out;
}