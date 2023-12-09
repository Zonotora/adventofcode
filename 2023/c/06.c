
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void read(FILE *fp, long long lines[2][5]) {
    int c;
    int i = 0;

    char * line = NULL;
    size_t len = 0;
    size_t read;

    while ((read = getline(&line, &len, fp)) != -1) {
        char *token;
        char all[len - 9];
        int j = 0;
        while ((token = strsep(&line, " "))) {
            if (isdigit(*token)) {
                lines[i][j++] = atoi(token);
                int n = strlen(token);
                strcat(all, token);
            }
        }
        lines[i][j] = atol(all);
        i++;
    }
   fclose(fp);
}

int calculate(long long time, long long record) {
    int count = 0;
    for (long long t = 0; t < time; t++) {
        long long left = time - t;
        if (left * t > record)
            count += 1;
    }
    return count;
}

int main(int argc, char *argv[])
{
    FILE *fp = fopen("../input/06", "r");
    long long lines[2][5] = {0};
    read(fp, lines);

    int part1 = 1;
    for (int j = 0; j < 4; j++) {
        long long time = lines[0][j];
        long long record =  lines[1][j];
        part1 *= calculate(time, record);
    }

    int part2 = calculate(lines[0][4], lines[1][4]);
    printf("%d\n", part1);
    printf("%d\n", part2);

    return 0;
}