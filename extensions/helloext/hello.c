#include <Python.h>

static PyObject* myfunc_noarg(PyObject* self) {
   return Py_BuildValue("s", "Hello, Python extensions - Function with No args ");
}

// documentation string
static char help_message_1[] =
   "Help message : Function with no argument !!\n";


// function with arguments (int, string)
static PyObject* myfunc_witharg(PyObject* self, PyObject *args) {
   int qty;
   char* item_desc;
   
   // parse input arguments
   // i denotes integer
   // s denotes string
   if(!PyArg_ParseTuple(args, "is", &qty,&item_desc)) {
      return NULL;
   }

   printf("Item Desc:       %s\n",item_desc);
   printf("Total Quantity:  %d\n",qty); 
   Py_RETURN_NONE; // this is #define which has inbuild return keyword added already
}


static char help_message_2[] =
   "Help message : Function with argument !!\n";



// function with arguments and return value (list)
static PyObject* myfunc_witharg_returnlist(PyObject* self, PyObject *args) {
   char* item_desc;
   
   // parse input arguments
   // s denotes string
   if(!PyArg_ParseTuple(args, "s", &item_desc)) {
      return NULL;
   }

   printf("Item Desc:       %s\n",item_desc);
   return Py_BuildValue("ss", item_desc, "full of sugar"); // multipe return values can be sent as python list
}


static char help_message_3[] =
   "Help message : Function with argument  and return value !!\n";


// function with arguments and return value (dict)
static PyObject* myfunc_witharg_returndict(PyObject* self, PyObject *args) {
   char* item_desc;
   
   // parse input arguments
   // s denotes string
   if(!PyArg_ParseTuple(args, "s", &item_desc)) {
      return NULL;
   }

   printf("Item Desc:       %s\n",item_desc);
   return Py_BuildValue("{sisi}", item_desc,10,"hulk",20); // multipe return values can be sent as python list
}

// mapping between C functions and python functions
static PyMethodDef helloext_API[] = {
   {"myfunc_noarg", (PyCFunction)myfunc_noarg,METH_NOARGS, help_message_1},
   {"myfunc_witharg", (PyCFunction)myfunc_witharg,METH_VARARGS, help_message_2},
   {"myfunc_witharg_returnlist", (PyCFunction)myfunc_witharg_returnlist,METH_VARARGS, help_message_2},
   {"myfunc_witharg_returndict", (PyCFunction)myfunc_witharg_returndict,METH_VARARGS, help_message_2},
   {NULL}
};

PyMODINIT_FUNC inithelloext(void) {
   Py_InitModule3("helloext", helloext_API,"Extension module example!");
}
