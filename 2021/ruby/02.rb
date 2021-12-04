lines = File.readlines("../input/02").map { |line| a, b = line.split; [a, b.to_i] }
# part 1
x = 0
depth = 0

lines.each do |op, val|
    case op
    when 'forward'; x += val;
    when 'down'; depth += val;
    when 'up'; depth -= val;
    end
end
puts x * depth

# part 2
x = 0
depth = 0
aim = 0

lines.each do |op, val|
    case op
    when 'forward'; x += val; depth += aim * val
    when 'down'; aim += val
    when 'up'; aim -= val
    end
end
puts x * depth