#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - cycle in liste
 *
 * @list: listint_t variable
 *
 * Description: checks if a singly linked list has a cycle in it
 *
 * Return: 0 if is no cycle 1 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current = 0;
	listint_t *nocycle = list;
	listint_t *previous = list;

	if (list == 0)
		return (0);
	if (list->next == list)
		return (1);
	current = list->next;
	nocycle->next = 0;

	while (current != 0)
	{
		listint_t *is_current = nocycle;

		while (is_current->next != 0 || is_current == current)
		{
			if (is_current == current)
			{
				previous->next = current;
				return (1);
			}
			is_current = is_current->next;
		}
		previous = current;
		is_current->next = current;
		current = current->next;
		is_current->next->next = 0;
	}
	return (0);
}
