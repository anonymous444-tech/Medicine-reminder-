//made by Vardhan😎
//to calculate SI
#include <stdio.h>
int main() {
	printf("enter the principal,rate and year\n");
	float pri;
	float rate;
	float yer;
	scanf("%f %f %f" ,&pri, &rate, &yer);
	float Si = (pri*rate*yer)/100;
	printf("hello world\n");
	printf("the sum is %f\n", Si);
	return 0;
	}
