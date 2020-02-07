#include "sort.h"
/**
* bubble_sort - sort list with bubble
* @array: the array to print
* @size: number of elements in the array
*/
void bubble_sort(int *array, size_t size)
{
int temp;
size_t i, j;
if (array == NULL)
return;
for (i = 0; i < size; i++)
{
for (j = 0; j < size - i - 1; j++)
{
if (array[j] > array[j + 1])
{
temp = array[j];
array[j] = array[j + 1];
array[j + 1] = temp;
print_array(array, size);
}
}
}
}
