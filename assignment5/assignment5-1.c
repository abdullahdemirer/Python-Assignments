/*
 ============================================================================
 Name        : assignment5-1.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

	int sayi= atoi(argv[1]);
	int i,j;
	int t=0;
	int bosluk=sayi+3;
	  	/*
		   /\ 	#3 bosluk basta
		  /  \	#2 boşuk basta 2 bosluk ortada
		 /    \	#1 boşluk başta 4 boşluk ortada
		/      \0 boşluk başta 6 boşluk ortada
		\      /0 ''      ''   ''  ''     ''
		 \    /	1
		  \  /
		   \/


	*/
	printf("input:%d\n",sayi);

	printf("output:\n");
	for (i=0; i<sayi; i++)
	{
		for (j=0; j<bosluk; j++)
		{
			printf(" ");
		}
		printf("/");
		for (j=0; j<t; j++)
		{
			printf(" ");
		}

		printf("\\ \n");
		t=t+2;
		bosluk=bosluk-1;
	}
	bosluk=4;
	t=t-2;
		for (i=0; i<sayi; i++)
	{
		for (j=0; j<bosluk; j++)
		{
			printf(" ");
		}
		printf("\\");
		for (j=0; j<t; j++)
		{
			printf(" ");
		}

		printf("/ \n");
		t=t-2;
		bosluk=bosluk+1;
	}

	return 0;
	getchar();

}
