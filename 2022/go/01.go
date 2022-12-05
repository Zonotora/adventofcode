package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("../input/01")
	if err != nil {
		panic(err)
	}

	blocks := strings.Split(string(data), "\n\n")

	var calories []int
	for i := 0; i < len(blocks); i++ {
		lines := strings.Split(blocks[i], "\n")
		s := 0
		for j := 0; j < len(lines); j++ {
			v, err := strconv.Atoi(lines[j])
			if err != nil {
				continue
			}
			s += v
		}
		calories = append(calories, s)
	}

	sort.Sort(sort.IntSlice(calories))
	n := len(blocks)
	fmt.Println(calories[n-1])
	fmt.Println(calories[n-1] + calories[n-2] + calories[n-3])
}
