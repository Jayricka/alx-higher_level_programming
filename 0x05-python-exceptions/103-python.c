#include <Python.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: Pointer to the PyObject list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *obj;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: Pointer to the PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++)
        printf(" %02x", (unsigned char)string[i]);
    printf("\n");
}

/**
 * print_python_float - Prints some basic info about Python float objects
 * @p: Pointer to the PyObject float object
 */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %f\n", value);
}
