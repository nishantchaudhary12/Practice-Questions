#include <stdio.h>
#include <conio.h>

int main(){
    int data[] = {1,3,2,5,2,5,8,3};
    int i, j, size, temp;
    size = sizeof(data)/sizeof(int);
    printf("\nBefore\n");
    for(i = 0; i < size; i++){
        printf("%d\t",data[i]);
    }
    printf("\n\n");
    for(i = 0; i < size-1; i++){
        for(j = i+1; j < size; j++){
            if(data[i] > data[j]){
                temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }
    printf("\n\n");
        printf("\nAfter\n");
    for(i = 0; i < size; i++){
        printf("%d\t",data[i]);
    }
    }




