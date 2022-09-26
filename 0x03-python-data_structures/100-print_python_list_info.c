#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - print
 *
 * @p: OyObject structure
 *
 * Description: print the info of pyObject
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	if (PyList_CheckExact(p) > 0)
	{
		Py_ssize_t i = 0;
		Py_ssize_t len = 1;

		len = PyList_Size(p);
		printf("[*] Size of the Python List = %lu\n", len);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < len; i++)
		{
			PyObject *obj = PyList_GetItem(p, i);

			if (obj != 0)
			{
				printf("Element %lu: %s\n", i, Py_TYPE(obj)->tp_name);
			}
		}
	}
}
