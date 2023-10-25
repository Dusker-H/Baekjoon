#define _CRT_SECURE_NO_WARNINGS
# include<stdio.h>

int main(void) {
	
	int inp[2] = { 0 };
	int	test, ea = 0;
	int result, temp = 0;
	
	scanf("%d", &result);
	temp = result;

	do {
		inp[0] = temp / 10;	//십의 자리
		inp[1] = temp % 10;	//일의 자리
		test = inp[0] + inp[1];	//십의자리 + 일의자리
		temp = inp[1] * 10 + test%10;	//일의자리 * 10 + test값의 일의자리
		ea++;
	} while (temp != result);	//temp와 입력값이 동일할 때 까지 반복

	printf("%d", ea);

}