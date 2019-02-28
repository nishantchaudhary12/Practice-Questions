#include<stdio.h>
#include<conio.h>
#include<math.h>

void main(){
float step_size = 0.1;
float data[] = {0,0.0998,0.1986,0.2955,0.3894,0.4794,0.5646,0.6442,0.7173,0.7833,0.8414}; //value of function given at 10 time
                                                                                        //intervals starting from 0 having step size 0.1
int i;
float derivative[10];
for(i = 0; i < 10; i++){
    derivative[i] = (data[i+1]-data[i-1])/(2*step_size);
    }
for(i = 0; i<10; i++){
    printf("Derivative at %d time interval = %f\n",i+1,derivative[i]);
}
}
