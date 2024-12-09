#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 1000

long absl(long x) {
  if (x < 0)
    return -x;
  return x;
}

int comparator(const void *e1, const void *e2) {
  long f = *((long *)e1);
  long s = *((long *)e2);
  if (f > s)
    return 1;
  if (f < s)
    return -1;
  return 0;
}

int main() {

  char *line;
  size_t size, i = 0;
  long left[N];
  long right[N];
  while (getline(&line, &size, stdin) != -1) {
    char *end, *p = line;
    left[i] = strtol(p, &end, 10);
    p = end;
    right[i] = strtol(p, &end, 10);
    i += 1;
  }

  qsort(left, sizeof(left) / sizeof(*left), sizeof(*left), comparator);
  qsort(right, sizeof(right) / sizeof(*right), sizeof(*right), comparator);

  long p1 = 0, p2 = 0;
  for (size_t i = 0; i < N; i++) {
    p1 += absl(left[i] - right[i]);
  }

  for (size_t i = 0, j = 0; i < N; i++) {
    long c = 0;
    while (j <= N && right[j] < left[i])
      j += 1;
    if (j >= N)
      continue;
    while (j <= N && right[j] == left[i]) {
      c += 1;
      j += 1;
    }
    if (j >= N)
      continue;
    p2 += left[i] * c;
  }

  printf("%ld\n", p1);
  printf("%ld\n", p2);

  return 0;
}