lines = File.readlines("../input/03").map { |line| line.strip.chars }

# part 1
gamma = lines.transpose.map { |row| row.count('1') > row.count('0') ? '1' : '0' }.join
epsilon = lines.transpose.map { |row| row.count('0') > row.count('1') ? '1' : '0' }.join
puts gamma.to_i(2) * epsilon.to_i(2)

# part 2
n = lines[0].length
o2 = lines.map(&:clone)
co2 = lines.map(&:clone)
for i in 0..n-1 do
    if o2.length != 1
        c1 = o2.transpose[i].count('1') >= o2.transpose[i].count('0') ? '0' : '1'
        o2 = o2.reject { |row| row[i] == c1 }
    end
    if co2.length != 1
        c2 = co2.transpose[i].count('1') >= co2.transpose[i].count('0') ? '1' : '0'
        co2 = co2.reject { |row| row[i] == c2 }
    end
end

puts o2.join.to_i(2) * co2.join.to_i(2)
