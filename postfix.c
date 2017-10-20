#include<stdio.h>
char stack[20];
int top = -1;
void push(char k)
{
    stack[++top] = k;
}

char pop()
{
    if(top == -1)
        return -1;
    else
        return stack[top--];
}

int priority(char k)
{
    if(k == '(')
        return 0;
    if(k == '+' || k == '-')
        return 1;
    if(k == '*' || k == '/')
        return 2;
}

main()
{
    char exp[20];
    char *e, k;
    printf("Enter the expression :: ");
    scanf("%s",exp);
    e = exp;
    while(*e != '\0')
    {
        if(isalnum(*e))
            printf("%c",*e);
        else if(*e == '(')
            push(*e);
        else if(*e == ')')
        {
            while((k = pop()) != '(')
                printf("%c", k);
        }
        else
        {
            while(priority(stack[top]) >= priority(*e))
                printf("%c",pop());
            push(*e);
        }
        e++;
    }
    while(top != -1)
    {
        printf("%c",pop());
    }
}

