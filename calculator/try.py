# h="harry"
# print(h[-4:-2])

# #include <iostream>
# using namespace std;
# int *size_array_dyna()
# {
#     int n;
#     cin >> n;
#     int *a = new int[n];
#     int *b = new int[n];
#     int i;
#     i = 0;
#     while (i < n)
#     {
#         cin >> a[i];
#         b[i] = a[i];
#         i++;
#     }
#     int m;
#     cin >> m;
#     a = new int[m + n];
#     for (i = 0; i < n; i++)
#     {
#         a[i] = b[i];
#     }
#     for (i = n; i < m + n; i++)
#     {
#         cin >> a[i];
#     }
#     return a;
# }
# int main()
# {
#     int *array = size_array_dyna();
#     int i;
#     int j;
#     cin >> j;
#     i = 0;
#     while (i < j)
#     {
#         cout << array[i] << " ";
#         i++;
#     }
#     delete[] array;
#     return 0;
# }