#include <stdio.h>

// Fazer um programa em C que imprime uma tabela com a tabuada de 1 a 9

int main() {
    int Multiplo = 2;
    
    for (int i = 0; i <= 9; i++) {
        printf("%d * %d = %d\n", i, Multiplo, i * Multiplo);
    }

    return 0;
}
