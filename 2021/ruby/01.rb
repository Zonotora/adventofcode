lines = File.readlines("../input/01").map(&:to_i)
# part 1
p lines.each_cons(2).count { | a, b| b > a}
# part 2
p lines.each_cons(4).count { | a, b, c, d| d > a}


