#include <stdio.h>
#include "python3.8/Python.h"
#include "bytesobject.h"

/**
 * print_python_bytes - print
 *
 * @p: PyBytesObject
 *
 * Description: print bytes info
 *
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbo = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (pbo && PyBytes_Check(pbo))
	{
		unsigned int size_9 = 0;
		unsigned int i = 0;

		size_9 = (pbo->ob_base.ob_size >= 10) ? 10 : pbo->ob_base.ob_size + 1;
		printf("  size: %ld\n", pbo->ob_base.ob_size);
		printf("  trying string: %s\n", pbo->ob_sval);
		printf("  first %u bytes:", size_9);
		for (i = 0; i < size_9; i++)
		{
			printf(" %02x", pbo->ob_sval[i] & 0xff);
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - print
 *
 * @p: PyObject
 *
 * Description: print PyObject info
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *object;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			object = list->ob_item[i];
			type = object->ob_type;
			printf("Element %ld: %s\n", i, type->tp_name);
			if (strcmp(type->tp_name, "bytes") == 0)
				print_python_bytes(object);
		}
	}
}
