#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a linked list contains a cycle
 * @head: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *head)
{
	listint_t *slowPtr = head;
	listint_t *fastPtr = head;

	if (head == NULL)
		return 0;

	while (slowPtr && fastPtr && fastPtr->next)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;
		if (slowPtr == fastPtr)
			return 1;
	}

	return 0;
}

