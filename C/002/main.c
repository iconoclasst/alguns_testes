#include <stdio.h>
#include <stdlib.h>
#include <math.h>

const float pi = 3.141592;

float meu_pow(float base, int expoente){
    float result = base;
    for(int i=1; i<expoente; i++) {
        result = result * base;
    }

    return result;
}

void q1(){
    int a;
    scanf("%d", &a);
    printf("%d, %d\n", a-1, a+1);
}

void q2(){
    float a;
    scanf("%f", &a);
    printf("%f\n", a/5.0);
}

void q3(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d\n", a+b+c);
}

void q4(){
    float a, b, c, d;
    scanf("%f %f %f %f", &a, &b, &c, &d);
    float soma = a + b + c + d;
    float media = soma/4.0;
    printf("%f\n", media);
}

void q5(){
    int idade, ano_atual;
    scanf("%d %d", &idade, &ano_atual);
    int ano = ano_atual - idade;
    printf("Ano de nascença é %d\n", ano);
}

void q6(){
    float velocidade;
    scanf("%f", &velocidade);
    float velocidade_convertida = velocidade / 36.0;
    printf("%f m/s\n", velocidade_convertida);
}

void q7(){
    float valor, cotacao;
    scanf("%f %f", &valor, &cotacao);
    float convertido = valor/cotacao;
    printf("%f\n", convertido);

}

void q8(){
    float graus_celsius;
    scanf("%f", &graus_celsius);
    float graus_fah = graus_celsius * (9.0/5.0) + 32.0;
    printf("%f\n", graus_fah);
}

void q9(){
    
    float angulo, radiano;
    scanf("%f", &angulo);
    
    radiano = angulo * pi/180;
    printf("%f\n", radiano);
}

void q10(){
    const float importancia = 780000.0;
    float a, b, c;
    a = importancia * 0.46;
    b = importancia * 0.32;
    c = importancia - (a+b);

    printf("%f %f %f\n", a, b, c);
}

void q11(){
    float raio;
    scanf("%f", &raio);
    float area = pi * meu_pow(raio, 2);
    printf("%f\n", area);
}

void q12(){
    float altura, raio, volume;
    scanf("%f %f", &altura, &raio);
    volume = pi * meu_pow(raio, 2) * altura;
    printf("%f\n", volume);
}

// void q13(){
//     float a, b, h, soma;
//     scanf("%f %f", &a, &b);
//     soma = meu_pow(a, 2) + meu_pow(b, 2);
//     h = sqrt(soma);
//     printf("%f\n", h);

// }

void q14(){
    char maiuscula, minuscula;
    maiuscula = getchar();
    minuscula = maiuscula + 32;
    printf("%c\n", minuscula);
}

void q15(){
    int valor, inverso = 0;
    scanf("%d", &valor);
    int resto = 0;

    while(valor > 0){
        resto = valor % 10;
        valor /= 10;
        inverso *= 10;
        inverso += resto;
    }

    printf("%d\n", inverso);
}

void q16(){
    int valor, dobro, metade;
    scanf("%d", &valor);
    dobro = valor << 1;
    metade = valor >> 1;
    printf("dobro = %d\nmetade = %d\n", dobro, metade);
}

void q17(){
    int valor, complemento;
    scanf("%d", &valor);
    complemento = ~valor;
    printf("%d\n", complemento);
}

void q18(){
    int a, b, esquerda, direita;
    scanf("%d %d", &a, &b); 
    esquerda = a << b;
    direita = a >> b;
    printf("%d\n%d\n%d\n", a, esquerda, direita);

}

void q19(){
    int a, b;
    scanf("%d %d", &a, &b);
    int xor, bbor, bba;
    xor = a ^ b;
    bbor = a | b;
    bba = a & b;
    printf("%d\n%d\n%d\n", xor, bbor, bba);
}

int main(){

    q19();

    return 0;
}