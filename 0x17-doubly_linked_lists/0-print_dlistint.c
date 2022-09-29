#include "lists.h"
#include <stdio.h>

size_t print_prev(const dlistint_t *h)
{
	size_t t = 0;

	if (h == 0)
		return (0);
	if (h->prev != 0)
	{
		t = 1 + print_prev(h->prev);
		printf("%d\n", h->prev->n);
	}
	return (t);
}

size_t print_next(const dlistint_t *h)
{
	size_t t = 0;
	if (h == 0)
		return (0);
	if (h->next != 0)
	{
		printf("%d\n", h->next->n);
		t = 1 + print_next(h->next);
	}
	return (t);
}

size_t print_dlistint(const dlistint_t *h)
{
	size_t taille = 1;

	if (h == 0)
		return (0);
	taille += print_prev(h);
	printf("%d\n", h->n);
	taille += print_next(h);

	return (taille);
}
