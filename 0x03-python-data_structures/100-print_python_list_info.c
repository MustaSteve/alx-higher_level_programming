#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc, j;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(n, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
