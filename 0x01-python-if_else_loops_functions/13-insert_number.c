#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inser
 *
 * @head: head list
 * @number: value
 *
 * Description: inserts a number into a sorted singly linked list
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_element = 0;
	listint_t *tmp = *head;

	new_element = (listint_t *)malloc(sizeof(listint_t));
	if (new_element == 0)
		return (0);
	new_element->next = 0;
	new_element->n = number;
	if (head == 0)
		return (new_element);
	if (*head == 0)
	{
		*head = new_element;
		return (new_element);
	}
	if (tmp->n > number)
	{
		new_element->next = tmp;
		*head = new_element;
		return (new_element);
	}
	while (tmp->next != 0)
	{
		if (tmp->next->n > number)
		{
			new_element->next = tmp->next;
			tmp->next = new_element;
			return (new_element);
		}
		tmp = tmp->next;
	}
	if (tmp->next == 0)
		tmp->next = new_element;
	return (new_element);
}
