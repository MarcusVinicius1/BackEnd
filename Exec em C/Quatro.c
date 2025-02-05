#include <stdio.h>

/*
    Fazer um programa em "C" que pergunte um valor em graus Fahrenheit e
    imprime no vídeo o correspondente em graus Celsius usando as fórmulas que
    seguem.
    
    a) Usar uma variável double para ler o valor em Fahrenheit e a fórmula
    C=(f-32.0) * (5.0/9.0).
    
    b) Usar uma variável int para ler o valor em Fahrenheit e a fórmula
    C=(f-32)*(5/9).
*/

int main() {
    double Fahrenheit = 0;
    double CelsiusDouble = 0;
    int CelsiusInt = 0;
    
    printf("Fahrenheit: ");
    scanf("%lf", &Fahrenheit);
    
    CelsiusDouble = (Fahrenheit - 32.0) * (5.0 / 9.0);
    CelsiusInt = (int)((Fahrenheit - 32) * (5.0 / 9.0));
    
    printf("\nResultado\n");
    printf("\nCelsius double: %.2lf", CelsiusDouble);
    printf("\nCelsiusInt: %d", CelsiusInt);

    return 0;
}
