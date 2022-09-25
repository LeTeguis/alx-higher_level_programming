#include "lists.h"
#include <stdio.h>

/**
 * size_list - len
 *
 * @head: head of list
 *
 * Description: determine the len of the list
 *
 * Return: len
 */
size_t size_list(listint_t *head)
{
	if (head == 0)
		return (0);
	return (1 + size_list(head->next));
}

/**
 * getNode - get
 *
 * @node: node list position
 * @index: index
 *
 * Description: go to the node that position is index
 *
 * Return: NULL if node == NULL or index out of range return node if not
 */
listint_t *getNode(listint_t *node, size_t index)
{
	if (node == 0 || index == 0)
		return (node);
	return (getNode(node->next, index - 1));
}

/**
 * is_palindrome - get
 *
 * @head: head of list
 *
 * Description: determine if listint_t is a palindrome or not
 *
 * Return: 1 if is and 0 if is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *gauche = *head;
	listint_t *middle = *head;
	size_t len = size_list(*head);
	size_t i = 0;

	if (head == 0 || *head == 0 || len == 1)
		return (1);
	/*
	 * if (len == 2)
	 * return ((gauche->n == gauche->next->n) ? 1 : 0);
	 * if (len == 3)
	 * return ((gauche->n == gauche->next->next->n) ? 1 : 0);
	 */
	middle = getNode(*head, (len / 2) + ((len % 2 == 1) ? 1 : 0));
	i = len / 2;
	while (i > 0)
	{
		listint_t *actual = getNode(middle, i - 1);

		if (actual == 0 || actual->n != gauche->n)
			return (0);
		gauche = gauche->next;
		i--;
	}
	return (1);
}
