void reverseString(char* s, int sSize){
    int i;
    char* stack = (char*)malloc(sizeof(char) * sSize);
    
    for(i=0;i<sSize;++i){
        stack[i] = s[sSize-1-i];
    }
    for(i=0;i<sSize;++i){
        s[i] = stack[i];
    }
}