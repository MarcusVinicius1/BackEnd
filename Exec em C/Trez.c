#include <stdio.h>

/*
    Fazer um programa que solicita um número decimal e imprime o
    correspondente em hexa e octal.
*/

int main() {
    int Decimal = 0;
    float Hexa, Octal = 0;
    
    printf("Metros: ");
    scanf("%d", &Decimal);
    
    Hexa = Decimal * 16;
    Octal = Decimal * 8;
    
    printf("\nResultado\n");
    printf("\nHexa: %.2f", Hexa);
    printf("\nOctal: %.2f", Octal);

    return 0;
}
