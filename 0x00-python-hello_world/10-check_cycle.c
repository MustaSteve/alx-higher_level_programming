#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_s = list;
	listint_t *fast_s = list;

	if (!list)
		return (0);

	while (slow_s && fast_s && fast_s->next)
	{
		slow_s = slow_s->next;
		fast_s = fast_s->next->next;
		if (slow_s == fast_s)
			return (1);
	}

	return (0);
}
