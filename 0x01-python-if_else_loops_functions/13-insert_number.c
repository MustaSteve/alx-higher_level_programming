#include "lists.h"

/**
  *insert_node - Insert a number into a singly-linked list
  * @head: A pointer the head.
  * @number: Number to insert.
  * Return: If the function fails - NULL
  * Otherwise - a pointer to the n node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node, *y_node;
	if (head == NULL)
		return(NULL);

	n_node = malloc(sizeof(listint_t));

	if (n_node == NULL)
		return (NULL);
	y_node = *head;
	n_node->p = number;
	n_node->next = NULL;
	if (*head == NULL)
	{
		*head = n_node;
		return(n_node);
	}
	if (y_node->p > number)
	{
		n_node->next = y_node;
		*head = n_node;
		return(n_node);
	}
	
	while (y_node->next != NULL)
	{
		if(y_node->next->p > number)
		{
			n_node->next = y_node->next;
			y_node->next = n_node;
			return(n_node);
		}
		y_node = y_node->next;
	}
	y_node->next = n_node;
	return(n_node);

}
