#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *currentnode;

	currentnode = *head;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->s = number;
	newnode->next = NULL;

	if (!*head)
		*head = newnode;
	else if (currentnode->s >= number)
	{
		*head = newnode;
		newnode->next = currentnode;
	}
	else if (currentnode->next)
	{
		while (currentnode->next)
		{
			if (currentnode->next->s >= number)
			{
				newnode->next = currentnode->next;
				currentnode->next = newnode;
				return (newnode);
			}
			if (!currentnode->next->next)
				break;
			currentnode = currentnode->next;
		}
		currentnode->next->next = newnode;
	}
	else
		currentnode->next = newnode;
	return (newnode);
}
