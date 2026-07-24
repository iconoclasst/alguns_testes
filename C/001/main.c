#include <stdio.h>
#include <stdlib.h>
#define pi 3.1415

const int peso = 50;

void questao1(){
    printf("Início de programa\nFim.\n");
}

void questao2(){
    int x;
    scanf("%d", &x);
    printf("%d\n", x);
}

void questao3(){
    int x;
    scanf("%d", &x);
    printf("Valor lido: %d\n", x);
}

void questao4(){
    int x;
    scanf("%d", &x);
    printf("%f\n", x);
}

void questao5(){
    float x;
    scanf("%f", &x);
    printf("%d\n", x);
}

void questao6(){
    double x;
    scanf("%lf", &x);
    printf("%lf\n", x);
    printf("%e\n", x);
}

void questao7(){
    char c;
    c = getchar();
    printf("%d\n", c);
}

void questao8(){
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d %d\n", y, x);
}

void questao9(){
    float x, y;
    scanf("%f %f", &x, &y);
    printf("%f %f\n", y, x);
}

void questao10(){
    int d, m, a;
    scanf("%d %d %d", &d, &m, &a);
    printf("%d/%d/%d\n", d, m, a);
}

void questao13(){
    char c;
    c = getchar();
    printf("\"%c\"\n", c);
}

void questao14(){
    char a, b, c;
    scanf("%c %c %c", &a, &b, &c);
    printf("%c\n%c\n%c\n", a, b, c);
}

void questao15(){
    char c;
    int x;
    float y;

    scanf("%c %d %f", &c, &x, &y);

    printf("%c\b%d\b%f", c, x, y);
    printf("\n");
    printf("%c\t%d\t%f", c, x, y);
    printf("\n");
    printf("%c\n%d\n%f", c, x, y);
    printf("\n");

}

int main() {

    questao15();

    // printf("%f\n", pi);
    return 0;
}