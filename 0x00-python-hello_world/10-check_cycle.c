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
	listint_t *current = list;
	listint_t *nocycle = 0;
	listint_t *previous = 0;

	while (current != 0)
	{
		if (nocycle == 0)
		{
			previous = current;
			nocycle = current;
			current = current->next;
			nocycle->next = 0;
		}
		else
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
	}
	return (0);
}
