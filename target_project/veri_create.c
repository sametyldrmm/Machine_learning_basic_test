#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <math.h>
#include <time.h>
#include <fcntl.h>
#include <string.h>
#include <sys/stat.h>
#define MAX_DISTANCE 30

int GLOBAL_X_Y_CIFTLERI_COUNTER = 10;
int veri_sayisi = 1; // sonradan silinecek

typedef struct s_point Point;
typedef struct s_point
{
    int x;
    int y;
    Point *next;
    Point *prev;
} Point;

float calculateDistance(int x1, int y1, int x2, int y2)
{
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

Point *lst_new(int x, int y)
{
    Point *p = (Point *)malloc(sizeof(Point));
    if (p == NULL)
    {
        perror("malloc");
        exit(EXIT_FAILURE);
    }
    p->x = x;
    p->y = y;
    p->next = NULL;
    p->prev = NULL;
    return p;
}

Point *lst_add_front(Point *root, int x, int y)
{
    if (root == NULL)
    {
        return lst_new(x, y);
    }
    Point *p = lst_new(x, y);
    p->next = root;
    root->prev = p;
    return p;
}

Point *lst_add_end(Point *root, int x, int y)
{
    if (root == NULL)
    {
        return lst_new(x, y);
    }
    Point *iter = root;
    while (iter->next != NULL)
    {
        iter = iter->next;
    }
    iter->next = lst_new(x, y);
    iter->next->prev = iter;
    return root;
}

Point *lst_remove(Point *root, Point *p)
{
    if (root == NULL)
    {
        return NULL;
    }
    if (root == p)
    {
        Point *temp = root->next;
        free(root);
        return temp;
    }
    Point *iter = root;
    while (iter->next != NULL && iter->next != p)
    {
        iter = iter->next;
    }
    if (iter->next == NULL)
    {
        return root;
    }
    Point *temp = iter->next;
    iter->next = iter->next->next;
    free(temp);
    return root;
}

int lst_get_x(Point *root, int index)
{
    Point *iter = root;
    for (int i = 0; i < index; i++)
    {
        iter = iter->next;
    }
    return iter->x;
}

int lst_get_y(Point *root, int index)
{
    Point *iter = root;
    for (int i = 0; i < index; i++)
    {
        iter = iter->next;
    }
    return iter->y;
}

int open_write_ret_fd(char *file_name)
{
    int fd = open(file_name, O_RDWR |O_APPEND, 0666);
    if (fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }
    return fd;
}

void write_fd(int fd, char *str)
{
    if (write(fd, str, strlen(str)) == -1)
    {
        perror("write");
        exit(EXIT_FAILURE);
    }
}

void write_all_area(int kd)
{
    for (int i = 0; i < 400; i++)
    {
        for (int j = 0; j < 400; j++)
        {
            char test_verileri_in[25] = {0};
            sprintf(test_verileri_in, "%d,%d ", i, j);
            write_fd(kd, test_verileri_in);
        }
        write_fd(kd, "\n");
    }
    write_fd(kd, "\n");
}

Point *create_x_y_ciftleri(int kd, Point *first, int test_veri)
{
    for (int i = 0; i < GLOBAL_X_Y_CIFTLERI_COUNTER; i++)
    {
        first = lst_add_front(first, rand() % 400 + 1, rand() % 400 + 1);
        char test_verileri_in[25] = {0};
        sprintf(test_verileri_in, "%d %d ", lst_get_x(first, 0), lst_get_y(first, 0));
        write_fd(kd, test_verileri_in);
        write_fd(kd, "\n");
    }
    write_fd(kd, "\n");
    return first;
}

Point *puanlama(int (*test)[400], Point *first)
{
    for (int i = 0; i < 400; i++)
    {
        for (int j = 0; j < 399; j++)
        {
            Point *iter = first;
            for (int h = 0; h < GLOBAL_X_Y_CIFTLERI_COUNTER; h++)
            {
                float distance = calculateDistance(i, j, iter->x, iter->y);
                if (distance < MAX_DISTANCE)
                {
                    test[i][j]++;
                }
                iter = iter->next;
            }
        }
    }
    return first;
}

void max_puan_x_y_find(int *max_puan, int *max_x, int *max_y, int (*test)[400])
{
    for (int i = 0; i < 400; i++)
    {
        for (int j = 0; j < 399; j++)
        {
            if (test[i][j] > *max_puan)
            {
                *max_puan = test[i][j];
                *max_x = i;
                *max_y = j;
            }
        }
    }
}

void write_test_verileri_out(char(*test_verileri_out), int test_veri, int max_puan, int max_puan_x, int max_puan_y, int fd)
{
    for (size_t i = 0; i < 25; i++)
    {
        test_verileri_out[i] = 0;
    }
    sprintf(test_verileri_out, "%d,%d,%d,%d\n", test_veri, max_puan, max_puan_x, max_puan_y);
    write(fd, test_verileri_out, strlen(test_verileri_out));
}

Point *remove_point_in_cycle(int max_puan_x, int max_puan_y, Point *first)
{
    int temp = 0;
    Point *iter;
    iter = first;
    for (int h = 0; h < GLOBAL_X_Y_CIFTLERI_COUNTER; h++)
    {
        float distance = calculateDistance(max_puan_x, max_puan_y, iter->x, iter->y);
        if (distance < MAX_DISTANCE && temp < 3)
        {
            first = lst_remove(first, iter);
            iter = first;
            GLOBAL_X_Y_CIFTLERI_COUNTER--;
            h = 0; // h-- de olabilir galiba
            temp++;
        }
        if (iter)
            iter = iter->next;
    }
    return first;
}

Point *lst_remove_all_list(Point *first)
{
    while(first)
    {
        first = lst_remove(first, first);
    }
    return first;
}

int main()
{
    srand(time(NULL));
    char *test_verileri_out = calloc(25, sizeof(char));
    // test_verileri_output.txt için int fd oluştur varsa dosya yenisini oluşturma yoksa oluştur içerisinde veri var ise üzerine yaz
    int fd = open_write_ret_fd("test_verileri_output2.txt");
    // test_verileri_input.txt için int kd oluştur varsa dosya yenisini oluşturma yoksa oluştur içerisinde veri var ise üzerine yaz
    int kd = open_write_ret_fd("test_verileri_input2.txt");
    int test_veri = 0;

    write_fd(fd, "Adim,Puan,X,Y\n");

    // input.txt ye alan verileri verilmesi gerekir
    write_all_area(kd);
    // input.txt ye var olan x_y çiftleri verilmesi gerekir

    while (test_veri < 10000)
    {
        GLOBAL_X_Y_CIFTLERI_COUNTER = 10;
        // test_verileri_input.txt için bir kaçıncı adım olduğunu yazdır
        // Random x-y çiftleri oluşturma
        Point *first = NULL;

        first = create_x_y_ciftleri(kd, first,test_veri);

        while (GLOBAL_X_Y_CIFTLERI_COUNTER > 0)
        {
            int test[400][400] = {0};
            first = puanlama(test, first);

            int max_puan = 0;
            int max_puan_x = 0;
            int max_puan_y = 0;
            // En yüksek puanı ve koordinatları bulma
            max_puan_x_y_find(&max_puan, &max_puan_x, &max_puan_y, test);
            // max puan max x max y tek satırda yazdırma
            // test_verileri_out.txt yazma
            write_test_verileri_out(test_verileri_out, test_veri, max_puan, max_puan_x, max_puan_y, fd);
            first = remove_point_in_cycle(max_puan_x, max_puan_y, first);
        }
        first = lst_remove_all_list(first);
        test_veri++;
    }
    return 0;
}
