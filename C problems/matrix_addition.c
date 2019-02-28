/*Matrix Addition*/

#include<conio.h>
#include<stdio.h>


void main(){
    //make three arrays one for the first matrix, one for the second one and then one for storing the sum of matrices
    int a[3][3], b[3][3], sum[3][3], i, j;
    //input for first matrix 3x3 matrix
    printf("Enter the elements of the first matrix:");
    printf("\n");
    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            scanf("%d",&a[i][j]);
        }
    }
    //input for second matrix 3x3
    printf("Enter the elements of the second matrix:");
    printf("\n");
    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            scanf("%d",&b[i][j]);
        }
    }
    //prints the sum of two matrices and stores it in sum[3][3]
    printf("The sum of two matrices is:");
    printf("\n");
    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            sum[i][j] = a[i][j] + b[i][j];
            printf("%d\t",sum[i][j]);
        }
        printf("\n");
    }

}
