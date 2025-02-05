#include <stdio.h>

/*
    Fazer um programa em C que pergunta um valor em metros e imprime o
    correspondente em decímetros, centímetros e milímetros
*/

int main() {
    int Metros = 0;
    float decimetros, centimetros, milimetros = 0;
    
    printf("Valor em metros: ");
    scanf("%d", &Metros);
    
    decimetros = Metros * 10;
    centimetros = Metros * 100;
    milimetros = Metros * 1000;
    
    printf("\nResultado\n");
    printf("Decimetros: %.2f", decimetros);
    printf("\nCentimetros: %.2f", centimetros);
    printf("\nMilimetros: %.2f", milimetros);

    return 0;
}
