bool judgeCircle(char* moves){
    signed int countUD = 0;
    signed int countRL = 0;
    
    while(*moves){
        switch(*moves){
            case 'U':
                countUD++;
                break;
            case 'D':
                countUD--;
                break;
            case 'R':
                countRL++;
                break;
            default:
                countRL--;
                break;
        }
       
        moves++;
    }
    
   return countUD == 0 && countRL == 0 ? 1 : 0;
}

