def busca_Binaria(v = 5,n = 10,elem = 40):
    inicio = 0
    final = n - 1
    while(inicio <= final):
        meio = (inicio + final)/2
        if(elem < v[meio]):
            final = meio -1
        elif(elem > v[meio]):
            inicio = meio + 1
        else:
            return meio
    return -1


int
main()
{
    int
V[TAM] = {6, 3, 9, 2, 7, 1, 0, 4, 8, 5};
int
i, x, n = 10;

ordenacao_insercao(V, n);

for (i = 0; i < n; i++)
{
    printf("%d ", V[i]);
}
printf("\n");

printf("Digite x: ");
scanf("%d", & x);
if (pertence(x, V, n))
printf("%d pertence\n", x);
else
printf("%d não pertence\n", x);

return 0;
}