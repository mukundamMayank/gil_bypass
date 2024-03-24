#include <Python.h>

PyObject* fibonacci_with_gil(PyObject* self, PyObject* args) {
    int n;
    
    long long a = 0, b = 1, temp;
    PyObject* result = PyList_New(0);
    for (int i = 0; i < n; i++) {
        PyList_Append(result, PyLong_FromLongLong(a));
        temp = a;
        a = b;
        b += temp;
    }

    return result;
}


PyObject* fibonacci_without_gil(PyObject* self, PyObject* args) {
    int n;
    
    long long a = 0, b = 1, temp;
    PyObject* result = PyList_New(0);
    PyGILState_STATE gil_state = PyGILState_Ensure();
    for (int i = 0; i < n; i++) {
        PyList_Append(result, PyLong_FromLongLong(a));
        temp = a;
        a = b;
        b += temp;
    }
    PyGILState_Release(gil_state);

    return result;
}

static PyMethodDef methods[] = {
    {"fibonacci_without_gil", fibonacci_without_gil, METH_VARARGS, "Calculate the Fibonacci without GIL"},
    {"fibonacci_with_gil", fibonacci_with_gil, METH_VARARGS, "Calculate the Fibonacci with the GIL"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "fibonacci_ext",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_fibonacci_ext(void) {
    return PyModule_Create(&module);
}
