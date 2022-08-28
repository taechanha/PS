int subtractProductAndSum(int n){
    int sum = 0;
    int product = 1;
    int test = n;
    int count = 0;
    int ex = 1;
    int i;

    while(test != 0){
        test /= 10;
        count++;
    }

    for(i=0;i<count-1;++i){
        ex *= 10;
    }
    sum += n / ex;
    product *= n / ex;

    while(ex != 0){
      printf("%d %d\n",product,sum);
      if(ex == 1){
        return product - sum;
      }
      else{
        sum += (n % ex) / (ex / 10);
        product *= (n % ex) / (ex / 10);
      }
      ex /= 10;
    }

    return product - sum;
}
