#include<stdio.h>
#include<conio.h>
#include<math.h>

int calculate_prime(int x){
    int i, is_divisible;
    double root;
    root = sqrt(x);
    is_divisible = 0;
    for(i = 2; i <= root; i++){
        is_divisible = 0;
        if(x%i == 0){
            is_divisible++;
            break;
        }
    }
    if(is_divisible == 0)
        return 1;
    else
        return 0;
}

int main(){
    int i, first, second, prime;
    printf("Enter the first number: ");  //take the first number of the range
    scanf("%d",&first);
    printf("Enter the second number: ");  //take the second number of the range
    scanf("%d",&second);
    prime = 0; //counter for prime numbers
    for(i = first; i <= second; i++){
        if (calculate_prime(i))
            prime++;
    }

    printf("\nThe total number of prime numbers between %d and %d are: %d",first,second,prime);
    getch();
}
