#include "lists.h"

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

	if (list == 0)
		return (0);
	if (list->next == list)
		return (1);
	current = list->next;

	while (current != 0)
	{
		listint_t *is_current = list;
		int number_count = 0;

		while (is_current->next != 0)
		{
			if (is_current == current)
				number_count++;
			if (number_count > 1)
				return (1);
			is_current = is_current->next;
		}
		current = current->next;
	}
	return (0);
}
