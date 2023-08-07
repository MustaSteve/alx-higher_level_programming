#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current_s;
    unsigned int n; /* number of nodes in */

    current_s = h;
    n = 0;
    while (current_s != NULL)
    {
        printf("%i\n", current_s->n);
        current = current_s->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to pointer of the start of the list
 * @n: integer to be includ in node
 * Return: address to the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new_s;

    new_s = malloc(sizeof(listint_t));
    if (new_s == NULL)
        return (NULL);

    new_s->n = n;
    new_s->next = *head;
    *head = new_s;

    return (new_s);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current_s = head;
        head = head->next;
        free(current_s);
    }
}
