package main

import (
	"fmt"
	"os"
	"strings"
)

func add(set map[string]bool, all map[string]bool, item string) {
	for j := 0; j < len(item); j++ {
		key := string(item[j])
		set[key] = true
		all[key] = true
	}
}

func main() {
	data, err := os.ReadFile("../input/03")

	if err != nil {
		panic(err)
	}

	ascii := ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	rucksacks := strings.Split(string(data), "\n")
	part1 := 0
	part2 := 0

	for i := 0; i < len(rucksacks); i++ {
		rucksack := rucksacks[i]
		n := int(len(rucksack) / 2)
		set1 := map[string]bool{}
		set2 := map[string]bool{}
		for j := 0; j < n; j++ {
			key1 := string(rucksack[j])
			key2 := string(rucksack[j+n])
			set1[key1] = true
			set2[key2] = true
		}
		for j := 0; j < n; j++ {
			key := string(rucksack[j])
			if set1[key] && set2[key] {
				part1 += strings.Index(ascii, key)
				break
			}
		}
	}

	for i := 0; i < len(rucksacks)-2; i += 3 {
		rucksack1 := rucksacks[i]
		rucksack2 := rucksacks[i+1]
		rucksack3 := rucksacks[i+2]
		set1 := map[string]bool{}
		set2 := map[string]bool{}
		set3 := map[string]bool{}
		all := map[string]bool{}
		add(set1, all, rucksack1)
		add(set2, all, rucksack2)
		add(set3, all, rucksack3)

		for key := range all {
			if set1[key] && set2[key] && set3[key] {
				part2 += strings.Index(ascii, key)
				break
			}
		}

	}

	fmt.Println(part1)
	fmt.Println(part2)
}
