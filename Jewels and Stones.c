int numJewelsInStones(char * J, char * S){
    int j_len = strlen(J);
    int s_len = strlen(S);
    int i,j;
    int count = 0;

    for(i=0;i<j_len;++i){
        for(j=0;j<s_len;++j){
            if(S[j] == J[i]){
                count++;
              }
            }
        }

    return count;
}