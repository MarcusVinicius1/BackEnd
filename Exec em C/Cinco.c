#include <stdio.h>

/*
    Fazer um programa em "C" que solicite 2 números e informe:
     
    a) A soma dos números;
    b) O produto do primeiro número pelo quadrado do segundo;
    c) O quadrado do primeiro número;
    d) A raiz quadrada da soma dos quadrados;
    e) O seno da diferença do primeiro número pelo segundo;
    f) O módulo do primeiro número.
*/

int main() {
    int NumUm, NumDois = 0;
    int Soma, QuadradoPeloSegundo = 0;
    
    printf("1° Valor: ");
    scanf("%d", &NumUm);
    
    printf("2° Valor: ");
    scanf("%d", &NumDois);
    
    Soma = NumUm + NumDois;

    return 0;
}
