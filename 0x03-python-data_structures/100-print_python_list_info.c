#include <stdio.h>
#include <python3.8/Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len = 1;
	
	if (PyList_CheckExact(p) > 0)
	{
		PyObject *obj = 0;
		Py_ssize_t i = 0;

		len = PyList_Size(p);
		printf("[*] Size of the Python List = %lu\n", len);
		for (i = 0; i < len; i++)
		{
			PyObject *obj = PyList_GetItem(p, i);

			switch (obj->type)
			{
				case T_STRING:
					printf("Element %lu: str\n", i);
					break;
				case T_FLOAT:
					printf("Element %lu: float\n", i);
					break;
			}
		}
	}
}
