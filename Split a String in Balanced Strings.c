    int balancedStringSplit(char * s){
        int countR = 0;
        int countL = 0;
        int output = 0;

        while(*s != '\0'){
            if(*s++ == 'R'){
                countR++;
            }
            else{
                countL++;
            }

            if(countR == countL){
                output++;

                countR = 0;
                countL = 0;
            }
        }

        return output;
    }

