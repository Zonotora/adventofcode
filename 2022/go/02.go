package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	data, err := os.ReadFile("../input/02")

	if err != nil {
		panic(err)
	}

	instructions := strings.Split(string(data), "\n")
	score := [3]int{1, 2, 3}
	var part1 = 0
	var part2 = 0

	for i := 0; i < len(instructions); i++ {
		parts := strings.Split(instructions[i], " ")
		index := strings.Index("ABC", parts[0])
		lose := strings.Index("BCA", parts[0])
		win := strings.Index("CAB", parts[0])
		left := string("XYZ"[index])
		right := parts[1]

		score_index := strings.Index("XYZ", parts[1])

		if left == right {
			part1 += score[score_index] + 3
		} else if (right == "Z" && left == "Y") || (right == "Y" && left == "X") || (right == "X" && left == "Z") {
			part1 += score[score_index] + 6
		} else {
			part1 += score[score_index]
		}

		if right == "X" {
			part2 += score[lose]
		} else if right == "Y" {
			part2 += score[index] + 3
		} else if right == "Z" {
			part2 += score[win] + 6
		}
	}

	fmt.Println(part1)
	fmt.Println(part2)

}
